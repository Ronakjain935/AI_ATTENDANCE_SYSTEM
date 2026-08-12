import streamlit as st
from PIL import Image
import numpy as np
import time

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import (
    get_all_students, create_student, get_student_subjects, 
    get_student_attendance, unenroll_student_to_subject
)
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"Welcome, {student_data['name']}")
        if st.button("Logout 🚪", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            if 'student_data' in st.session_state:
                del st.session_state.student_data
            st.rerun()

    st.write("")

    c1, c2 = st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('➕ Enroll in Subject', type='primary', use_container_width=True):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects...'):
        subjects = get_student_subjects(student_id) or []
        logs = get_student_attendance(student_id) or []

    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    if subjects:
        cols = st.columns(2)
        for i, sub_node in enumerate(subjects):
            sub = sub_node['subjects']
            sid = sub['subject_id']
            stats = stats_map.get(sid, {"total": 0, "attended": 0})
            
            def unenroll_button():
                if st.button("🗑️ Unenroll from this course", type='tertiary', use_container_width=True, key=f"unenroll_{sid}"):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f'Unenrolled from {sub["name"]} successfully!')
                    st.rerun()

            with cols[i % 2]:
                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=[
                        ('📅', 'Total', stats['total']),
                        ('✅', 'Attended', stats['attended']),
                    ],
                    footer_callback=unenroll_button
                )
    else:
        st.info("You are not enrolled in any subjects yet. Click 'Enroll in Subject' above!")

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("⬅️ Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header('Student Portal & Login')
    st.markdown("<p style='color: #475569; font-size: 1rem;'>Log in using FaceID, upload your face photo, or select your registered profile.</p>", unsafe_allow_html=True)
    st.write("")

    if "student_login_mode" not in st.session_state:
        st.session_state.student_login_mode = 'face_id'

    m1, m2, m3 = st.columns(3)
    with m1:
        t1_type = "primary" if st.session_state.student_login_mode == 'face_id' else "tertiary"
        if st.button('📷 Camera FaceID', type=t1_type, use_container_width=True):
            st.session_state.student_login_mode = 'face_id'
            st.rerun()
    with m2:
        t2_type = "primary" if st.session_state.student_login_mode == 'upload_photo' else "tertiary"
        if st.button('📁 Upload Photo', type=t2_type, use_container_width=True):
            st.session_state.student_login_mode = 'upload_photo'
            st.rerun()
    with m3:
        t3_type = "primary" if st.session_state.student_login_mode == 'select_profile' else "tertiary"
        if st.button('👤 Select Profile', type=t3_type, use_container_width=True):
            st.session_state.student_login_mode = 'select_profile'
            st.rerun()

    st.write("")
    show_registration = False
    captured_img_np = None

    # MODE 1: CAMERA SCAN
    if st.session_state.student_login_mode == 'face_id':
        photo_source = st.camera_input("Position your face in the center")
        if photo_source:
            captured_img_np = np.array(Image.open(photo_source))

    # MODE 2: UPLOAD PHOTO FILE
    elif st.session_state.student_login_mode == 'upload_photo':
        uploaded_file = st.file_uploader("Choose your profile photo image file", type=['jpg', 'jpeg', 'png'], key="std_upload_login")
        if uploaded_file:
            captured_img_np = np.array(Image.open(uploaded_file))

    # MODE 3: SELECT REGISTERED PROFILE
    elif st.session_state.student_login_mode == 'select_profile':
        all_students = get_all_students() or []
        if all_students:
            std_options = {s['name']: s for s in all_students}
            selected_name = st.selectbox("Select your registered name", options=list(std_options.keys()))
            if st.button("🔑 Log In as Selected Student", type="primary", use_container_width=True):
                selected_std = std_options[selected_name]
                st.session_state.is_logged_in = True
                st.session_state.user_role = 'student'
                st.session_state.student_data = selected_std
                st.toast(f"Welcome Back {selected_std['name']}! 👋")
                time.sleep(0.5)
                st.rerun()
        else:
            st.info("No registered students found. Register your profile below!")
            show_registration = True

    # Process photo login if camera or photo uploaded
    if captured_img_np is not None:
        with st.spinner('AI scanning face...'):
            detected, all_ids, num_faces = predict_attendance(captured_img_np)

            if num_faces == 0:
                st.warning('No face detected in the image! Please provide a clear face photo.')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students() or []
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}! 🎉")
                        time.sleep(0.8)
                        st.rerun()
                else:
                    st.info('Face not recognized in our database! Register a new profile below or select your registered profile.')
                    show_registration = True

    st.divider()

    # REGISTRATION EXPANDER / CONTAINER
    if show_registration or st.checkbox("🆕 Register as a New Student Profile", value=show_registration):
        with st.container(border=True):
            st.header('Register New Profile')
            st.markdown("<p style='color: #475569;'>Your profile and face photo will be saved permanently so you can log in anytime!</p>", unsafe_allow_html=True)
            
            new_name = st.text_input("Enter your full name", placeholder='E.g. Hamza Rizvi')

            reg_photo = st.file_uploader("Upload Profile Photo for Registration", type=['jpg', 'jpeg', 'png'], key="reg_photo_uploader")
            if reg_photo is None and captured_img_np is not None:
                st.info("Using captured photo for registration.")

            st.subheader('Optional: Voice Profile Enrollment')
            audio_data = None
            try:
                audio_data = st.audio_input('Record a short phrase like: "I am present, My name is Hamza"')
            except Exception:
                pass

            if st.button('✨ Create Account & Save Profile', type='primary', use_container_width=True):
                if new_name:
                    target_img_np = None
                    if reg_photo is not None:
                        target_img_np = np.array(Image.open(reg_photo))
                    elif captured_img_np is not None:
                        target_img_np = captured_img_np

                    if target_img_np is not None:
                        with st.spinner('Saving face profile permanently...'):
                            encodings = get_face_embeddings(target_img_np)
                            if encodings:
                                face_emb = encodings[0].tolist()
                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())

                                response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)
                                if response_data:
                                    train_classifier()
                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = 'student'
                                    st.session_state.student_data = response_data[0]
                                    st.toast(f'Profile Created Permanently! Hi {new_name}! 🎉')
                                    time.sleep(1)
                                    st.rerun()
                            else:
                                st.error("Couldn't detect facial features in the photo. Please use a clearer face picture.")
                    else:
                        st.warning("Please take a camera snapshot or upload a face photo file for registration.")
                else:
                    st.warning('Please enter your full name!')

    footer_dashboard()
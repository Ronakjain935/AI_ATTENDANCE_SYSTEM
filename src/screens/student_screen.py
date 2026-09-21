import streamlit as st
from PIL import Image
import numpy as np
import time
import textwrap

from src.ui.base_layout import style_background_dashboard, style_base_layout, render_theme_toggle, get_current_theme
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
    theme = get_current_theme()
    is_dark = (theme == "dark")

    card_bg = "#1E293B" if is_dark else "#FFFFFF"
    card_border = "#334155" if is_dark else "#CBD5E1"
    text_color = "#FFFFFF" if is_dark else "#0F172A"
    sub_color = "#94A3B8" if is_dark else "#475569"

    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    student_name = student_data.get('name', 'Student')
    initials = "".join([part[0] for part in student_name.split()][:2]).upper() if student_name else "ST"

    top_col1, top_col2 = st.columns([1.1, 1.2], vertical_alignment='center')
    with top_col1:
        header_dashboard()
    with top_col2:
        u_col0, u_col1, u_col2 = st.columns([1.1, 1.7, 0.9], vertical_alignment='center')
        with u_col0:
            render_theme_toggle("student_top_theme_toggle")
        with u_col1:
            st.markdown(textwrap.dedent(f"""\
<div style="display: flex; align-items: center; justify-content: flex-end; gap: 8px;">
<div style="text-align: right;">
<div style="font-size: 0.92rem; font-weight: 800; color: {text_color}; white-space: nowrap;">{student_name}</div>
<span style="font-size: 0.70rem; background: {'#2563EB' if is_dark else '#0F172A'}; color: #FFFFFF; padding: 2px 6px; border-radius: 4px; font-weight: 800; letter-spacing: 0.04em;">STUDENT</span>
</div>
<div style="width: 38px; height: 38px; border-radius: 6px; background: linear-gradient(135deg, #2563EB 0%, #065F46 100%); color: #FFFFFF; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; justify-content: center;">
{initials}
</div>
</div>\
"""), unsafe_allow_html=True)
        with u_col2:
            if st.button("Log Out", type='secondary', key='student_logout_btn', use_container_width=True):
                st.session_state['is_logged_in'] = False
                if 'student_data' in st.session_state:
                    del st.session_state.student_data
                st.rerun()

    with st.spinner('Loading enrolled courses...'):
        subjects = get_student_subjects(student_id) or []
        logs = get_student_attendance(student_id) or []

    stats_map = {}
    total_attended_all = 0
    total_sessions_all = 0

    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        total_sessions_all += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1
            total_attended_all += 1

    overall_attendance_pct = int((total_attended_all / total_sessions_all * 100)) if total_sessions_all > 0 else 100

    # High-Contrast Student KPI Row
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.markdown(textwrap.dedent(f"""\
<div style="background: {card_bg}; border: 1.5px solid {card_border}; border-top: 4px solid #2563EB; border-radius: 8px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(0,0,0,0.06);">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
<span style="color: {sub_color}; font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">Enrolled Courses</span>
<span style="font-size: 1.2rem;">📚</span>
</div>
<div style="font-size: 1.85rem; font-weight: 800; color: {text_color};">{len(subjects)}</div>
</div>\
"""), unsafe_allow_html=True)

    with kpi2:
        st.markdown(textwrap.dedent(f"""\
<div style="background: {card_bg}; border: 1.5px solid {card_border}; border-top: 4px solid #16A34A; border-radius: 8px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(0,0,0,0.06);">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
<span style="color: {sub_color}; font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">Classes Attended</span>
<span style="font-size: 1.2rem;">✅</span>
</div>
<div style="font-size: 1.85rem; font-weight: 800; color: {text_color};">{total_attended_all} / {total_sessions_all}</div>
</div>\
"""), unsafe_allow_html=True)

    with kpi3:
        pct_color = "#16A34A" if overall_attendance_pct >= 75 else "#D97706"
        st.markdown(textwrap.dedent(f"""\
<div style="background: {card_bg}; border: 1.5px solid {card_border}; border-top: 4px solid {pct_color}; border-radius: 8px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(0,0,0,0.06);">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
<span style="color: {sub_color}; font-size: 0.78rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">Attendance Rate</span>
<span style="font-size: 1.2rem;">📊</span>
</div>
<div style="font-size: 1.85rem; font-weight: 800; color: {pct_color};">{overall_attendance_pct}%</div>
</div>\
"""), unsafe_allow_html=True)

    st.write("")

    c1, c2 = st.columns([3, 1], vertical_alignment='center')
    with c1:
        st.markdown(textwrap.dedent("""\
<div>
<h2 style="font-size: 1.45rem; font-weight: 700; font-family: 'Lora', Georgia, serif; color: #0F172A; margin: 0 0 4px 0;">My Registered Courses</h2>
<p style="color: #475569; font-size: 0.88rem; margin: 0;">Institutional subjects and your real-time attendance standing.</p>
</div>\
"""), unsafe_allow_html=True)
    with c2:
        if st.button('➕ Enroll in Course', type='primary', use_container_width=True):
            enroll_dialog()

    st.divider()

    if subjects:
        cols = st.columns(2)
        for i, sub_node in enumerate(subjects):
            sub = sub_node.get('subjects')
            if not sub:
                continue
            sid = sub.get('subject_id')
            stats = stats_map.get(sid, {"total": 0, "attended": 0})
            
            def unenroll_button():
                if st.button("Drop Course", type='tertiary', use_container_width=True, key=f"unenroll_{sid}"):
                    unenroll_student_to_subject(student_id, sid)
                    st.toast(f'Unenrolled from {sub["name"]}')
                    st.rerun()

            with cols[i % 2]:
                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=[
                        ('📋', 'Total Sessions', stats['total']),
                        ('✅', 'Attended', stats['attended']),
                    ],
                    footer_callback=unenroll_button
                )
    else:
        st.info("You are not enrolled in any courses yet. Click 'Enroll in Course' above to join your class.")

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    theme = get_current_theme()
    is_dark = (theme == "dark")
    title_color = "#FFFFFF" if is_dark else "#0F172A"
    sub_color = "#94A3B8" if is_dark else "#475569"

    c1, c2, c3 = st.columns([1.5, 0.7, 0.8], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        render_theme_toggle('slogin_theme_toggle')
    with c3:
        if st.button("← Home", type='secondary', key='loginbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.write("")

    with st.container(border=True):
        st.markdown(textwrap.dedent(f"""\
<div style="margin-bottom: 14px;">
<div style="display: inline-block; background: {'#1E293B' if is_dark else '#EEF2FF'}; color: {'#38BDF8' if is_dark else '#4338CA'}; border: 1px solid {'#334155' if is_dark else '#E0E7FF'}; padding: 2px 8px; border-radius: 6px; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px;">
Biometric Verification
</div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: {title_color}; margin: 0 0 4px 0;">Student Check-In</h2>
<p style="color: {sub_color}; font-size: 0.88rem; margin: 0;">Sign in using FaceID, photo verification, or choose your profile.</p>
</div>\
"""), unsafe_allow_html=True)

        if "student_login_mode" not in st.session_state:
            st.session_state.student_login_mode = 'face_id'

        m1, m2, m3 = st.columns(3)
        with m1:
            t1_type = "primary" if st.session_state.student_login_mode == 'face_id' else "secondary"
            if st.button('📷 Camera FaceID', type=t1_type, use_container_width=True):
                st.session_state.student_login_mode = 'face_id'
                st.rerun()
        with m2:
            t2_type = "primary" if st.session_state.student_login_mode == 'upload_photo' else "secondary"
            if st.button('📁 Upload Photo', type=t2_type, use_container_width=True):
                st.session_state.student_login_mode = 'upload_photo'
                st.rerun()
        with m3:
            t3_type = "primary" if st.session_state.student_login_mode == 'select_profile' else "secondary"
            if st.button('👤 Select Profile', type=t3_type, use_container_width=True):
                st.session_state.student_login_mode = 'select_profile'
                st.rerun()

        st.write("")
        show_registration = False
        captured_img_np = None

        # MODE 1: CAMERA SCAN
        if st.session_state.student_login_mode == 'face_id':
            photo_source = st.camera_input("Align your face within the frame")
            if photo_source:
                captured_img_np = np.array(Image.open(photo_source))

        # MODE 2: UPLOAD PHOTO FILE
        elif st.session_state.student_login_mode == 'upload_photo':
            uploaded_file = st.file_uploader("Upload profile face photo", type=['jpg', 'jpeg', 'png'], key="std_upload_login")
            if uploaded_file:
                captured_img_np = np.array(Image.open(uploaded_file))

        # MODE 3: SELECT REGISTERED PROFILE
        elif st.session_state.student_login_mode == 'select_profile':
            all_students = get_all_students() or []
            if all_students:
                std_options = {s['name']: s for s in all_students}
                selected_name = st.selectbox("Choose registered student name", options=list(std_options.keys()))
                st.write("")
                if st.button("Sign In as Selected Student", type="primary", use_container_width=True):
                    selected_std = std_options[selected_name]
                    st.session_state.is_logged_in = True
                    st.session_state.user_role = 'student'
                    st.session_state.student_data = selected_std
                    st.toast(f"Welcome back, {selected_std['name']}!")
                    time.sleep(0.5)
                    st.rerun()
            else:
                st.info("No registered students found. Register your profile below.")
                show_registration = True

        # Process photo login if camera or photo uploaded
        if captured_img_np is not None:
            with st.spinner('Scanning facial features...'):
                detected, all_ids, num_faces = predict_attendance(captured_img_np)

                if num_faces == 0:
                    st.warning('No face was detected. Please ensure good lighting and face the camera directly.')
                else:
                    if detected:
                        student_id = list(detected.keys())[0]
                        all_students = get_all_students() or []
                        student = next((s for s in all_students if s['student_id'] == student_id), None)

                        if student:
                            st.session_state.is_logged_in = True
                            st.session_state.user_role = 'student'
                            st.session_state.student_data = student
                            st.toast(f"Welcome back, {student['name']}!")
                            time.sleep(0.5)
                            st.rerun()
                    else:
                        st.info('Face not recognized in our database. Register below to save your profile permanently.')
                        show_registration = True

        st.divider()

        # REGISTRATION
        if show_registration or st.checkbox("Register as a New Student Profile", value=show_registration):
            st.markdown(textwrap.dedent("""\
<div style="margin-top: 8px; margin-bottom: 12px;">
<div style="display: inline-block; background: #ECFDF5; color: #047857; border: 1px solid #A7F3D0; padding: 2px 8px; border-radius: 6px; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px;">
Student Registration
</div>
<h3 style="font-size: 1.25rem; font-weight: 800; color: #0F172A; margin: 0 0 4px 0;">New Profile Enrollment</h3>
<p style="color: #64748B; font-size: 0.88rem; margin: 0;">Save your face and voice profile permanently for automated class check-in.</p>
</div>\
"""), unsafe_allow_html=True)
            
            new_name = st.text_input("Full Name", placeholder='e.g. Hamza Rizvi')

            reg_photo = st.file_uploader("Upload Face Photo for Registration", type=['jpg', 'jpeg', 'png'], key="reg_photo_uploader")
            if reg_photo is None and captured_img_np is not None:
                st.info("Using snapshot from camera for registration.")

            st.markdown("<p style='font-size: 0.9rem; font-weight: 600; color: #334155; margin-top: 10px; margin-bottom: 4px;'>Optional: Voice Profile Enrollment</p>", unsafe_allow_html=True)
            audio_data = None
            try:
                audio_data = st.audio_input('Record roll-call phrase (e.g. "I am present")')
            except Exception:
                pass

            st.write("")
            if st.button('Save Profile & Enter Portal', type='primary', use_container_width=True):
                if new_name:
                    target_img_np = None
                    if reg_photo is not None:
                        target_img_np = np.array(Image.open(reg_photo))
                    elif captured_img_np is not None:
                        target_img_np = captured_img_np

                    if target_img_np is not None:
                        with st.spinner('Analyzing facial vectors...'):
                            encodings = get_face_embeddings(target_img_np)
                            if encodings:
                                face_emb = encodings[0].tolist()
                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())

                                try:
                                    response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)
                                    if response_data:
                                        train_classifier()
                                        st.session_state.is_logged_in = True
                                        st.session_state.user_role = 'student'
                                        st.session_state.student_data = response_data[0]
                                        st.toast(f'Profile created! Welcome {new_name}.')
                                        time.sleep(0.5)
                                        st.rerun()
                                except Exception as e:
                                    st.error(f"Database error: {e}")
                            else:
                                st.error("No distinct face detected. Please use a clearer photo with good lighting.")
                    else:
                        st.warning("Please capture or upload a face photo for registration.")
                else:
                    st.warning('Please enter your full name.')

    footer_dashboard()
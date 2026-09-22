import streamlit as st
from PIL import Image
import numpy as np
import time
from datetime import datetime

from src.ui.base_layout import style_page_background, style_base_layout
from src.components.header import header_dashboard
from src.database.db import (
    get_all_students, create_student, get_student_subjects, 
    get_student_attendance, unenroll_student_to_subject
)
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    student_name = student_data.get('name', 'Student')
    initials = "".join([part[0] for part in student_name.split()][:2]).upper() if student_name else "ST"
    today_str = datetime.now().strftime("%A, %b %d, %Y")

    # Fixed Dashboard Header
    top_c1, top_c2 = st.columns([3, 1], vertical_alignment='center')
    with top_c1:
        header_dashboard(page_title="Student Portal", user_name=student_name, role="Student")
    with top_c2:
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

    total_missed_all = total_sessions_all - total_attended_all
    overall_attendance_pct = int((total_attended_all / total_sessions_all * 100)) if total_sessions_all > 0 else 100
    pct_color = "#218739" if overall_attendance_pct >= 75 else ("#B7791F" if overall_attendance_pct >= 60 else "#C53030")

    # STUDENT IDENTITY CARD (High Contrast, Classic Academic Card)
    id_card_html = f"""<div style="background: #FFFFFF; border: 1px solid #D9DEE7; border-radius: 12px; padding: 1.5rem; margin-top: 1.25rem; margin-bottom: 1.75rem; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);">
<div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 14px; border-bottom: 1px solid #D9DEE7; padding-bottom: 14px; margin-bottom: 16px;">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 10px; background: #172B4D; color: #FFFFFF; font-weight: 800; font-size: 1.15rem; display: flex; align-items: center; justify-content: center; font-family: 'Plus Jakarta Sans', sans-serif;">
{initials}
</div>
<div>
<div style="font-size: 0.72rem; font-weight: 700; color: #218739; text-transform: uppercase; letter-spacing: 0.06em;">
● VERIFIED BIOMETRIC IDENTITY
</div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: #172B4D; margin: 2px 0 2px 0;">{student_name}</h2>
<span style="font-size: 0.78rem; font-weight: 600; color: #667085;">STUDENT ID: #{student_id} &bull; {today_str}</span>
</div>
</div>

<div style="text-align: right;">
<div style="font-size: 2.3rem; font-weight: 800; color: {pct_color}; font-family: 'Plus Jakarta Sans', sans-serif; line-height: 1;">
{overall_attendance_pct}%
</div>
<span style="font-size: 0.74rem; font-weight: 700; color: #667085; text-transform: uppercase; letter-spacing: 0.04em;">
OVERALL ATTENDANCE
</span>
</div>
</div>

<div style="margin-bottom: 14px;">
<div style="display: flex; justify-content: space-between; font-size: 0.72rem; font-weight: 600; color: #667085; margin-bottom: 4px;">
<span>◯ 75% ACADEMIC BENCHMARK</span>
<span>100% MAXIMUM</span>
</div>
<div style="height: 7px; width: 100%; background: #F0EFEA; border-radius: 999px; overflow: hidden;">
<div style="height: 100%; width: {min(max(overall_attendance_pct, 0), 100)}%; background: {pct_color}; border-radius: 999px;"></div>
</div>
</div>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; text-align: center; border-top: 1px solid #D9DEE7; padding-top: 12px;">
<div>
<span style="font-size: 0.74rem; font-weight: 600; color: #667085; display: block; text-transform: uppercase;">Classes Attended</span>
<strong style="font-size: 1.3rem; color: #218739; font-family: 'Plus Jakarta Sans', sans-serif;">{total_attended_all} <span style="font-size: 0.85rem; font-weight: 500; color: #667085;">classes</span></strong>
</div>
<div>
<span style="font-size: 0.74rem; font-weight: 600; color: #667085; display: block; text-transform: uppercase;">Classes Missed</span>
<strong style="font-size: 1.3rem; color: #C53030; font-family: 'Plus Jakarta Sans', sans-serif;">{total_missed_all} <span style="font-size: 0.85rem; font-weight: 500; color: #667085;">classes</span></strong>
</div>
<div>
<span style="font-size: 0.74rem; font-weight: 600; color: #667085; display: block; text-transform: uppercase;">Registered Subjects</span>
<strong style="font-size: 1.3rem; color: #172B4D; font-family: 'Plus Jakarta Sans', sans-serif;">{len(subjects)}</strong>
</div>
</div>
</div>"""
    st.markdown(id_card_html, unsafe_allow_html=True)

    # SUBJECT TILES SECTION
    c1, c2 = st.columns([3, 1], vertical_alignment='center')
    with c1:
        st.markdown("""<div>
<h3 style="font-size: 1.3rem; font-weight: 700; color: #172B4D; margin: 0 0 2px 0;">My Registered Subject Tiles</h3>
<p style="color: #667085; font-size: 0.86rem; margin: 0;">Classroom subjects and your real-time attendance standing.</p>
</div>""", unsafe_allow_html=True)
    with c2:
        if st.button('➕ Join Course', type='primary', use_container_width=True):
            enroll_dialog()

    st.write("")

    if subjects:
        cols = st.columns(2)
        for i, sub_node in enumerate(subjects):
            sub = sub_node.get('subjects')
            if not sub:
                continue
            sid = sub.get('subject_id')
            stats = stats_map.get(sid, {"total": 0, "attended": 0})
            sub_pct = int(stats['attended'] / stats['total'] * 100) if stats['total'] > 0 else 100

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
                        ('Sessions', f"{stats['attended']} / {stats['total']} Classes"),
                    ],
                    footer_callback=unenroll_button,
                    progress_pct=sub_pct,
                    tile_index=i + 1
                )
    else:
        empty_box = """<div style="background: #FFFFFF; border: 1.5px dashed #D9DEE7; border-radius: 12px; padding: 2.5rem 1.5rem; text-align: center; margin: 1rem 0;">
<div style="font-size: 2.2rem; margin-bottom: 0.75rem;">📚</div>
<h4 style="font-size: 1.15rem; font-weight: 700; color: #172B4D; margin: 0 0 4px 0;">No subjects enrolled yet</h4>
<p style="color: #667085; font-size: 0.88rem; max-width: 440px; margin: 0 auto 1.25rem auto;">
You haven't joined any classes. Click the button below to enroll using your instructor's course code.
</p>
</div>"""
        st.markdown(empty_box, unsafe_allow_html=True)
        btn_c1, btn_c2, btn_c3 = st.columns([1, 1.4, 1])
        with btn_c2:
            if st.button('➕ Join Your First Course', type='primary', use_container_width=True, key="empty_enroll_btn"):
                enroll_dialog()


def student_screen():
    style_page_background()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns([3, 1], vertical_alignment='center')
    with c1:
        header_dashboard(page_title="Student Authentication")
    with c2:
        if st.button("← Home", type='secondary', key='loginbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.write("")

    with st.container(border=True):
        checkin_header_html = """<div style="margin-bottom: 14px;">
<div style="display: inline-block; background: #EEF4FF; color: #2F6FED; border: 1px solid #CFE0FC; padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; margin-bottom: 6px;">
Biometric Verification
</div>
<h2 style="font-size: 1.4rem; font-weight: 800; color: #172B4D; margin: 0 0 4px 0;">Student Sign In</h2>
<p style="color: #667085; font-size: 0.88rem; margin: 0;">Authenticate using FaceID, portrait photo, or select your registered profile.</p>
</div>"""
        st.markdown(checkin_header_html, unsafe_allow_html=True)

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

        if st.session_state.student_login_mode == 'face_id':
            photo_source = st.camera_input("Align your face within the frame")
            if photo_source:
                captured_img_np = np.array(Image.open(photo_source))

        elif st.session_state.student_login_mode == 'upload_photo':
            uploaded_file = st.file_uploader("Upload clear face portrait", type=['jpg', 'jpeg', 'png'], key="std_upload_login")
            if uploaded_file:
                captured_img_np = np.array(Image.open(uploaded_file))

        elif st.session_state.student_login_mode == 'select_profile':
            all_students = get_all_students() or []
            if all_students:
                std_options = {s['name']: s for s in all_students}
                selected_name = st.selectbox("Select your registered student name", options=list(std_options.keys()))
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

        if captured_img_np is not None:
            with st.spinner('Scanning facial vectors...'):
                from src.pipelines.face_pipeline import predict_attendance
                detected, all_ids, num_faces = predict_attendance(captured_img_np)

                if num_faces == 0:
                    st.warning('No face detected. Please face the camera directly with good lighting.')
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
                        st.info('Face not recognized in database. Register below to save your profile.')
                        show_registration = True

        st.divider()

        if show_registration or st.checkbox("Register as a New Student Profile", value=show_registration):
            reg_header_html = """<div style="margin-top: 8px; margin-bottom: 12px;">
<div style="display: inline-block; background: #EAF6ED; color: #218739; border: 1px solid #BFE3C7; padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; margin-bottom: 6px;">
Profile Enrollment
</div>
<h3 style="font-size: 1.25rem; font-weight: 700; color: #172B4D; margin: 0 0 4px 0;">New Profile Enrollment</h3>
<p style="color: #667085; font-size: 0.86rem; margin: 0;">Save your face and optional voice profile permanently for automated roll-call.</p>
</div>"""
            st.markdown(reg_header_html, unsafe_allow_html=True)
            
            new_name = st.text_input("Full Name", placeholder='e.g. Alex Morgan')

            reg_photo = st.file_uploader("Upload Face Photo for Biometrics", type=['jpg', 'jpeg', 'png'], key="reg_photo_uploader")
            if reg_photo is None and captured_img_np is not None:
                st.info("Using camera snapshot above for registration.")

            st.markdown("<p style='font-size: 0.88rem; font-weight: 600; color: #172B4D; margin-top: 10px; margin-bottom: 4px;'>Optional: Voice Profile Enrollment</p>", unsafe_allow_html=True)
            audio_data = None
            try:
                audio_data = st.audio_input('Record roll-call phrase (e.g. "I am present")')
            except Exception:
                pass

            st.write("")
            if st.button('Save Profile & Enter Student Portal', type='primary', use_container_width=True):
                if new_name:
                    target_img_np = None
                    if reg_photo is not None:
                        target_img_np = np.array(Image.open(reg_photo))
                    elif captured_img_np is not None:
                        target_img_np = captured_img_np

                    if target_img_np is not None:
                        with st.spinner('Analyzing facial vectors...'):
                            from src.pipelines.face_pipeline import get_face_embeddings, train_classifier
                            encodings = get_face_embeddings(target_img_np)
                            if encodings:
                                face_emb = encodings[0].tolist()
                                voice_emb = None
                                if audio_data:
                                    from src.pipelines.voice_pipeline import get_voice_embedding
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
                                st.error("No distinct face detected. Please ensure clear lighting.")
                    else:
                        st.warning("Please capture or upload a face photo for registration.")
                else:
                    st.warning('Please enter your full name.')
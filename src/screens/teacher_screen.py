import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import time
import textwrap

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import (
    check_teacher_exists, create_teacher, teacher_login, 
    get_teacher_subjects, get_attendance_for_teacher,
    delete_attendance_session, delete_all_attendance_for_teacher,
    get_enrolled_students_for_subject,
    delete_subject, claim_subject, get_all_existing_subjects
)
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog
from src.pipelines.face_pipeline import predict_attendance
from src.components.dialog_attendance_results import attendance_result_dialog
from src.components.dialog_voice_attendance import voice_attendance_dialog
from src.database.config import supabase

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    teacher_id = teacher_data['teacher_id']
    teacher_name = teacher_data.get('name', 'Instructor')
    initials = "".join([part[0] for part in teacher_name.split()][:2]).upper() if teacher_name else "IN"

    # Top App Shell Header
    top_col1, top_col2 = st.columns([1.5, 1], vertical_alignment='center')
    with top_col1:
        header_dashboard()
    with top_col2:
        u_col1, u_col2 = st.columns([2.2, 1], vertical_alignment='center')
        with u_col1:
            st.markdown(textwrap.dedent(f"""\
<div style="display: flex; align-items: center; justify-content: flex-end; gap: 10px;">
<div style="text-align: right;">
<div style="font-size: 0.92rem; font-weight: 700; color: #0F172A; white-space: nowrap;">{teacher_name}</div>
<span style="font-size: 0.72rem; background: #0F172A; color: #F8FAFC; border: 1px solid #1E293B; padding: 2px 7px; border-radius: 4px; font-weight: 700; letter-spacing: 0.04em;">FACULTY</span>
</div>
<div style="width: 38px; height: 38px; border-radius: 6px; background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%); color: #FFFFFF; font-weight: 700; font-size: 0.88rem; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 4px rgba(15, 23, 42, 0.2);">
{initials}
</div>
</div>\
"""), unsafe_allow_html=True)
        with u_col2:
            if st.button("Log Out", type='secondary', key='teacher_logout_btn', use_container_width=True):
                st.session_state['is_logged_in'] = False
                if 'teacher_data' in st.session_state:
                    del st.session_state.teacher_data
                st.rerun()

    # Pre-fetch stats for top KPI row
    subjects = get_teacher_subjects(teacher_id) or []
    records = get_attendance_for_teacher(teacher_id) or []
    total_students_enrolled = sum(s.get('total_students', 0) for s in subjects)
    
    sessions_keys = set((r.get('timestamp'), r.get('subject_id')) for r in records if r.get('timestamp'))
    total_sessions_count = len(sessions_keys)

    # Classic Executive KPI Metric Bar
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.markdown(textwrap.dedent(f"""\
<div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 3px solid #1E3A8A; border-radius: 8px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
<span style="color: #475569; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">Active Courses</span>
<span style="font-size: 1.1rem;">📚</span>
</div>
<div style="font-size: 1.75rem; font-weight: 700; color: #0F172A; font-family: 'Lora', Georgia, serif;">{len(subjects)}</div>
</div>\
"""), unsafe_allow_html=True)

    with kpi2:
        st.markdown(textwrap.dedent(f"""\
<div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 3px solid #047857; border-radius: 8px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
<span style="color: #475569; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">Total Enrolled</span>
<span style="font-size: 1.1rem;">👥</span>
</div>
<div style="font-size: 1.75rem; font-weight: 700; color: #0F172A; font-family: 'Lora', Georgia, serif;">{total_students_enrolled}</div>
</div>\
"""), unsafe_allow_html=True)

    with kpi3:
        st.markdown(textwrap.dedent(f"""\
<div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-top: 3px solid #B45309; border-radius: 8px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
<span style="color: #475569; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em;">Sessions Logged</span>
<span style="font-size: 1.1rem;">📋</span>
</div>
<div style="font-size: 1.75rem; font-weight: 700; color: #0F172A; font-family: 'Lora', Georgia, serif;">{total_sessions_count}</div>
</div>\
"""), unsafe_allow_html=True)

    st.write("")

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    # Segmented Tab Navigation Bar
    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "secondary"
        if st.button('📷 Take Attendance', type=type1, use_container_width=True):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "secondary"
        if st.button('📚 Manage Courses', type=type2, use_container_width=True):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "secondary"
        if st.button('📋 Attendance History', type=type3, use_container_width=True):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance(subjects)
    elif st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects(subjects)
    elif st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records(records)

    footer_dashboard()


def teacher_tab_take_attendance(subjects):
    st.markdown(textwrap.dedent("""\
<div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: #0F172A; margin: 0 0 4px 0;">Take Attendance</h2>
<p style="color: #64748B; font-size: 0.9rem; margin: 0 0 1.25rem 0;">Select a course and upload classroom photos or record roll-call audio.</p>
</div>\
"""), unsafe_allow_html=True)

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    if not subjects:
        st.info('You have not created any courses yet. Go to "Manage Courses" to set up your first class.')
        return
    
    subject_options = {f"{s['name']} ({s['subject_code']})": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3, 1], vertical_alignment='bottom')

    with col1:
        selected_subject_label = st.selectbox('Select Course', options=list(subject_options.keys()))

    with col2:
        if st.button('Add Photos', type='primary', use_container_width=True):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.write("")

    if st.session_state.attendance_images:
        st.markdown(textwrap.dedent(f"""\
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
<span style="font-size: 0.95rem; font-weight: 700; color: #0F172A;">Classroom Photos ({len(st.session_state.attendance_images)})</span>
</div>\
"""), unsafe_allow_html=True)
        gallery_cols = st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, use_container_width=True, caption=f'Photo {idx+1}')

    has_photos = bool(st.session_state.attendance_images)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('Clear Photos', use_container_width=True, type='tertiary', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()

    with c2:
        if st.button('🔍 Run Face Recognition', use_container_width=True, type='primary', disabled=not has_photos):
            with st.spinner('Scanning classroom photos...'):
                all_detected_ids = {}
                total_faces_scanned = 0

                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np = np.array(img.convert('RGB'))
                    detected, _, num_faces = predict_attendance(img_np)
                    total_faces_scanned += num_faces

                    if detected:
                        for sid in detected.keys():
                            student_id = int(sid)
                            all_detected_ids.setdefault(student_id, []).append(f"Photo {idx+1}")

                enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id', selected_subject_id).execute()
                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('No students are enrolled in this course yet. Share your course code to have students join.')
                elif total_faces_scanned == 0:
                    st.warning('No faces were detected in the uploaded photos. Please upload clearer photos.')
                else:
                    results, attendance_to_log = [], []
                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                    for node in enrolled_students:
                        student = node['students']
                        sources = all_detected_ids.get(int(student['student_id']), [])
                        is_present = len(sources) > 0

                        results.append({
                            "Name": student['name'],
                            "ID": student['student_id'],
                            "Source": ", ".join(sources) if is_present else "-",
                            "Status": "Present" if is_present else "Absent"
                        })

                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestamp,
                            'is_present': bool(is_present)
                        })

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        if st.button('🎙️ Voice Attendance', type='secondary', use_container_width=True):
            voice_attendance_dialog(selected_subject_id)


def teacher_tab_manage_subjects(subjects):
    teacher_id = st.session_state.teacher_data['teacher_id']
    col1, col2 = st.columns([3, 1], vertical_alignment='center')
    with col1:
        st.markdown(textwrap.dedent("""\
<div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: #0F172A; margin: 0 0 4px 0;">Manage Courses</h2>
<p style="color: #64748B; font-size: 0.9rem; margin: 0;">Create and organize your active classes and student rosters.</p>
</div>\
"""), unsafe_allow_html=True)

    with col2:
        if st.button('➕ Create Course', use_container_width=True, type='primary'):
            create_subject_dialog(teacher_id)

    st.write("")
    if subjects:
        for sub in subjects:
            stats = [
                ("👥", "Students", sub['total_students']),
                ("📋", "Sessions", sub['total_classes']),
            ]
            def action_buttons():
                bcol1, bcol2 = st.columns(2)
                with bcol1:
                    if st.button(f"🔗 Share Code: {sub['subject_code']}", key=f"share_{sub['subject_code']}", type='secondary', use_container_width=True):
                        share_subject_dialog(sub['name'], sub['subject_code'])
                with bcol2:
                    if st.button("🗑️ Delete Course", key=f"del_{sub['subject_id']}", type='tertiary', use_container_width=True):
                        delete_subject(sub['subject_id'])
                        st.toast(f"Deleted {sub['name']} successfully!")
                        time.sleep(0.5)
                        st.rerun()
                st.write("")

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=stats,
                footer_callback=action_buttons
            )

            with st.expander(f"View Enrolled Students ({sub['total_students']})", expanded=False):
                enrolled = get_enrolled_students_for_subject(sub['subject_id'])
                if enrolled:
                    std_list = []
                    for idx, e in enumerate(enrolled, 1):
                        std = e.get('students', {})
                        std_name = std.get('name', 'Unknown') if std else 'Unknown'
                        std_id = std.get('student_id', 'N/A') if std else 'N/A'
                        enrolled_at = e.get('created_at', '')
                        if enrolled_at:
                            try:
                                enrolled_at = datetime.fromisoformat(enrolled_at).strftime("%b %d, %Y")
                            except Exception:
                                pass
                        std_list.append({
                            "#": idx,
                            "Student Name": std_name,
                            "Student ID": std_id,
                            "Enrolled On": enrolled_at or "N/A"
                        })
                    st.dataframe(pd.DataFrame(std_list), use_container_width=True, hide_index=True)
                else:
                    st.info(f"No students enrolled in {sub['name']} yet. Click 'Share Code' above to invite students.")
            st.write("")
    else:
        st.info("No courses registered under your account. Click 'Create Course' above to get started.")

    # Other existing subjects in system
    all_subs = get_all_existing_subjects()
    other_subs = [s for s in all_subs if s.get('teacher_id') != teacher_id]
    if other_subs:
        st.write("")
        with st.expander(f"System Courses Available to Claim ({len(other_subs)})", expanded=False):
            st.markdown("<p style='color: #64748B; font-size: 0.88rem;'>Courses from previous test accounts. You can transfer them to your account with one click:</p>", unsafe_allow_html=True)
            for oth in other_subs:
                c_info, c_btn = st.columns([3, 1.2], vertical_alignment='center')
                with c_info:
                    owner = oth.get('teachers', {}).get('name', 'Another account') if oth.get('teachers') else 'Another account'
                    st.markdown(f"**{oth['name']}** (`{oth['subject_code']}`) — Section: {oth.get('section', 'N/A')} | Owner: *{owner}* | Enrolled: **{oth.get('total_students', 0)} students**")
                with c_btn:
                    if st.button("Claim Course", key=f"claim_other_{oth['subject_id']}", type="primary", use_container_width=True):
                        claim_subject(oth['subject_code'], teacher_id)
                        st.toast(f"Transferred '{oth['name']}' to your account!")
                        time.sleep(0.5)
                        st.rerun()
                st.divider()


def teacher_tab_attendance_records(records):
    st.markdown(textwrap.dedent("""\
<div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: #0F172A; margin: 0 0 4px 0;">Attendance History</h2>
<p style="color: #64748B; font-size: 0.9rem; margin: 0;">Comprehensive log of past class sessions and attendance rosters.</p>
</div>\
"""), unsafe_allow_html=True)

    if not records:
        st.info("No attendance records found yet.")
        return
    
    sessions_map = {}
    for r in records:
        ts = r.get('timestamp')
        sub = r.get('subjects', {})
        sid = r.get('subject_id')
        session_key = (ts, sid)

        if session_key not in sessions_map:
            formatted_time = "N/A"
            if ts:
                try:
                    formatted_time = datetime.fromisoformat(ts).strftime("%b %d, %Y - %I:%M %p")
                except Exception:
                    formatted_time = str(ts)

            sessions_map[session_key] = {
                'timestamp': ts,
                'subject_id': sid,
                'subject_name': sub.get('name', 'Unknown'),
                'subject_code': sub.get('subject_code', 'N/A'),
                'formatted_time': formatted_time,
                'logs': []
            }
        
        student_res = supabase.table('students').select('name').eq('student_id', r['student_id']).execute()
        student_name = student_res.data[0]['name'] if (student_res and student_res.data) else f"Student #{r['student_id']}"
        
        sessions_map[session_key]['logs'].append({
            'Name': student_name,
            'ID': r['student_id'],
            'Status': "Present" if r.get('is_present') else "Absent"
        })

    col1, col2 = st.columns([2.5, 1.5], vertical_alignment='center')
    with col1:
        st.markdown(f"<p style='color: #475569; font-weight: 600; margin: 0;'>Total Logged Sessions: <span style='color: #4F46E5; font-weight: 700;'>{len(sessions_map)}</span></p>", unsafe_allow_html=True)
    with col2:
        if st.button("Clear All History", type="tertiary", use_container_width=True):
            teacher_id = st.session_state.teacher_data['teacher_id']
            if st.session_state.get('confirm_clear_all'):
                delete_all_attendance_for_teacher(teacher_id)
                st.session_state.confirm_clear_all = False
                st.toast("All attendance records deleted successfully.")
                st.rerun()
            else:
                st.session_state.confirm_clear_all = True
                st.warning("Click again to confirm deleting all attendance history.")

    st.write("")

    for (ts, sid), sess in sorted(sessions_map.items(), key=lambda x: str(x[0][0]), reverse=True):
        logs = sess['logs']
        present_count = sum(1 for l in logs if l['Status'] == "Present")
        total_count = len(logs)
        
        with st.expander(f"{sess['formatted_time']} — {sess['subject_code']} {sess['subject_name']} ({present_count}/{total_count} Present)"):
            c_info, c_del = st.columns([2.5, 1.5], vertical_alignment='center')
            
            with c_info:
                st.markdown(f"**Course:** {sess['subject_name']} (`{sess['subject_code']}`)")
                st.markdown(f"**Roster Summary:** {present_count} Present · {total_count - present_count} Absent")
            
            with c_del:
                clean_ts_id = str(ts).replace("-", "_").replace(":", "_").replace(".", "_")
                delete_key = f"del_sess_{clean_ts_id}_{sid}"
                if st.button("Delete Session", key=delete_key, type="tertiary", use_container_width=True):
                    delete_attendance_session(ts, sid)
                    st.toast(f"Deleted attendance session for {sess['formatted_time']}")
                    time.sleep(0.5)
                    st.rerun()
            
            st.markdown("<p style='margin-top: 10px; margin-bottom: 6px; font-weight: 600; color: #0F172A; font-size: 0.88rem;'>Roster Details:</p>", unsafe_allow_html=True)
            df_sess = pd.DataFrame(logs)
            st.dataframe(df_sess, use_container_width=True, hide_index=True)


def login_teacher(username, password):
    if not username or not password:
        return False
    
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False


def teacher_screen_login():
    c1, c2 = st.columns([1.5, 1], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Back to Home", type='secondary', key='loginbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.write("")
    with st.container(border=True):
        st.markdown(textwrap.dedent("""\
<div style="margin-bottom: 14px;">
<div style="display: inline-block; background: #EEF2FF; color: #4338CA; border: 1px solid #E0E7FF; padding: 2px 8px; border-radius: 6px; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px;">
Instructor Authentication
</div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: #0F172A; margin: 0 0 4px 0;">Teacher Sign In</h2>
<p style="color: #64748B; font-size: 0.88rem; margin: 0;">Access your classroom rosters and take attendance.</p>
</div>\
"""), unsafe_allow_html=True)

        teacher_username = st.text_input("Username", placeholder='e.g. ronakjain')
        teacher_pass = st.text_input("Password", type='password', placeholder="Enter your password")

        st.write("")
        btnc1, btnc2 = st.columns(2)

        with btnc1:
            if st.button('Sign In', use_container_width=True, type='primary'):
                if login_teacher(teacher_username, teacher_pass):
                    st.toast("Welcome back!", icon="👋")
                    time.sleep(0.5)
                    st.rerun()
                else:
                    st.error("Invalid username or password.")

        with btnc2:
            if st.button('Register New Account', type="secondary", use_container_width=True):
                st.session_state.teacher_login_type = 'register'
                st.rerun()

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All fields are required."
    if check_teacher_exists(teacher_username):
        return False, "Username is already taken."
    if teacher_pass != teacher_pass_confirm:
        return False, "Passwords do not match."
    
    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Account created successfully! Please sign in."
    except Exception:
        return False, "Unexpected error creating account."


def teacher_screen_register():
    c1, c2 = st.columns([1.5, 1], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Back to Home", type='secondary', key='loginbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.write("")
    with st.container(border=True):
        st.markdown(textwrap.dedent("""\
<div style="margin-bottom: 14px;">
<div style="display: inline-block; background: #ECFDF5; color: #047857; border: 1px solid #A7F3D0; padding: 2px 8px; border-radius: 6px; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px;">
New Account Setup
</div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: #0F172A; margin: 0 0 4px 0;">Instructor Registration</h2>
<p style="color: #64748B; font-size: 0.88rem; margin: 0;">Set up your educator account to manage classroom attendance.</p>
</div>\
"""), unsafe_allow_html=True)

        teacher_username = st.text_input("Username", placeholder='e.g. ronakjain')
        teacher_name = st.text_input("Full Name", placeholder='e.g. Ronak Jain')
        teacher_pass = st.text_input("Password", type='password', placeholder="Choose a password")
        teacher_pass_confirm = st.text_input("Confirm Password", type='password', placeholder="Re-enter password")

        st.write("")
        btnc1, btnc2 = st.columns(2)

        with btnc1:
            if st.button('Create Account', use_container_width=True, type='primary'):
                success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
                if success:
                    st.success(message)
                    time.sleep(1)
                    st.session_state.teacher_login_type = "login"
                    st.rerun()
                else:
                    st.error(message)

        with btnc2:
            if st.button('Sign In Instead', type="secondary", use_container_width=True):
                st.session_state.teacher_login_type = 'login'
                st.rerun()

    footer_dashboard()
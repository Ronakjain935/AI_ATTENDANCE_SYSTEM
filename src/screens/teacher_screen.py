import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import time

from src.ui.base_layout import style_page_background, style_base_layout
from src.components.header import header_dashboard
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
from src.components.dialog_attendance_results import attendance_result_dialog
from src.components.dialog_voice_attendance import voice_attendance_dialog
from src.database.config import supabase

def teacher_screen():
    style_page_background()
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
    today_str = datetime.now().strftime("%A, %b %d, %Y")

    # Header Control Bar
    top_c1, top_c2 = st.columns([3, 1], vertical_alignment='center')
    with top_c1:
        header_dashboard(page_title="Classroom Control", user_name=teacher_name, role="Faculty")
    with top_c2:
        if st.button("Log Out", type='secondary', key='teacher_logout_btn', use_container_width=True):
            st.session_state['is_logged_in'] = False
            if 'teacher_data' in st.session_state:
                del st.session_state.teacher_data
            st.rerun()

    # Pre-fetch stats
    subjects = get_teacher_subjects(teacher_id) or []
    records = get_attendance_for_teacher(teacher_id) or []
    total_students_enrolled = sum(s.get('total_students', 0) for s in subjects)
    
    sessions_keys = set((r.get('timestamp'), r.get('subject_id')) for r in records if r.get('timestamp'))
    total_sessions_count = len(sessions_keys)

    total_presents = sum(1 for r in records if r.get('is_present'))
    total_logs = len(records)
    total_absents = total_logs - total_presents
    avg_rate = int(total_presents / total_logs * 100) if total_logs > 0 else 100
    rate_color = "#218739" if avg_rate >= 75 else ("#B7791F" if avg_rate >= 60 else "#C53030")

    # CLASSROOM CONTROL PANEL (Classic Academic Style)
    ctrl_panel_html = f"""<div style="background: #FFFFFF; border: 1px solid #D9DEE7; border-radius: 12px; padding: 1.5rem; margin-top: 1.25rem; margin-bottom: 1.5rem; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);">
<div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; border-bottom: 1px solid #D9DEE7; padding-bottom: 12px; margin-bottom: 14px;">
<div>
<div style="font-size: 0.72rem; font-weight: 700; color: #2F6FED; text-transform: uppercase; letter-spacing: 0.06em;">
CLASSROOM CONTROL &bull; INSTRUCTOR CONSOLE
</div>
<h2 style="font-size: 1.45rem; font-weight: 800; color: #172B4D; margin: 2px 0 2px 0;">Prof. {teacher_name}</h2>
<span style="font-size: 0.80rem; font-weight: 600; color: #667085;">{today_str} &bull; {len(subjects)} Active Subjects</span>
</div>

<div style="text-align: right;">
<div style="font-size: 2.3rem; font-weight: 800; color: {rate_color}; font-family: 'Plus Jakarta Sans', sans-serif; line-height: 1;">
{avg_rate}%
</div>
<span style="font-size: 0.74rem; font-weight: 700; color: #667085; text-transform: uppercase; letter-spacing: 0.04em;">
TODAY'S ATTENDANCE
</span>
</div>
</div>

<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; text-align: center;">
<div>
<span style="font-size: 0.72rem; font-weight: 600; color: #667085; display: block; text-transform: uppercase;">Students Present</span>
<strong style="font-size: 1.25rem; color: #218739; font-family: 'Plus Jakarta Sans', sans-serif;">{total_presents}</strong>
</div>
<div>
<span style="font-size: 0.72rem; font-weight: 600; color: #667085; display: block; text-transform: uppercase;">Students Absent</span>
<strong style="font-size: 1.25rem; color: #C53030; font-family: 'Plus Jakarta Sans', sans-serif;">{total_absents}</strong>
</div>
<div>
<span style="font-size: 0.72rem; font-weight: 600; color: #667085; display: block; text-transform: uppercase;">Total Students</span>
<strong style="font-size: 1.25rem; color: #172B4D; font-family: 'Plus Jakarta Sans', sans-serif;">{total_students_enrolled}</strong>
</div>
<div>
<span style="font-size: 0.72rem; font-weight: 600; color: #667085; display: block; text-transform: uppercase;">Total Subjects</span>
<strong style="font-size: 1.25rem; color: #2F6FED; font-family: 'Plus Jakarta Sans', sans-serif;">{len(subjects)}</strong>
</div>
</div>
</div>"""
    st.markdown(ctrl_panel_html, unsafe_allow_html=True)

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    # Fixed Navigation Tabs
    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "secondary"
        if st.button('📷 Take Attendance', type=type1, use_container_width=True):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "secondary"
        if st.button('📚 Manage Subjects', type=type2, use_container_width=True):
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


def teacher_tab_take_attendance(subjects):
    st.markdown("""<div style="margin-bottom: 12px;">
<div style="font-size: 0.72rem; font-weight: 700; color: #2F6FED; text-transform: uppercase; letter-spacing: 0.06em;">
AI RECOGNITION CONSOLE
</div>
<h3 style="font-size: 1.35rem; font-weight: 800; color: #172B4D; margin: 2px 0 0 0;">Classroom Roll-Call Console</h3>
<p style="color: #667085; font-size: 0.88rem; margin: 0;">Scan classroom photos or record acoustic voice roll-call.</p>
</div>""", unsafe_allow_html=True)

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    if not subjects:
        st.info('No registered courses found. Create your first subject in "Manage Subjects" tab.')
        return
    
    subject_options = {f"{s['name']} ({s['subject_code']}) &bull; {s.get('total_students', 0)} Enrolled": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3, 1.2], vertical_alignment='bottom')

    with col1:
        selected_subject_label = st.selectbox('Select Active Classroom', options=list(subject_options.keys()))

    with col2:
        if st.button('➕ Add Classroom Photo', type='primary', use_container_width=True):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.write("")

    # AI RECOGNITION CONSOLE: Left Camera area, Right Status panel
    c_left, c_right = st.columns([1.5, 1], gap="medium")

    with c_left:
        st.markdown(f"""<div style="font-size: 0.82rem; font-weight: 700; color: #172B4D; margin-bottom: 6px;">
CLASSROOM CAMERA AREA [{len(st.session_state.attendance_images)} PHOTOS LOADED]
</div>""", unsafe_allow_html=True)

        if st.session_state.attendance_images:
            gallery_cols = st.columns(min(len(st.session_state.attendance_images), 3))
            for idx, img in enumerate(st.session_state.attendance_images[:3]):
                with gallery_cols[idx]:
                    st.image(img, use_container_width=True, caption=f"Photo #{idx+1}")
            if len(st.session_state.attendance_images) > 3:
                st.caption(f"+ {len(st.session_state.attendance_images) - 3} additional photos queued")
        else:
            empty_viewfinder = """<div style="background: #FFFFFF; border: 1.5px dashed #D9DEE7; border-radius: 8px; padding: 2.5rem 1rem; text-align: center;">
<div style="font-size: 0.82rem; font-weight: 700; color: #40566F; margin-bottom: 4px;">CAMERA AREA STANDBY</div>
<p style="font-size: 0.86rem; color: #667085; margin: 0;">Click 'Add Classroom Photo' above to load student group snapshots.</p>
</div>"""
            st.markdown(empty_viewfinder, unsafe_allow_html=True)

    with c_right:
        has_photos = bool(st.session_state.attendance_images)
        scan_state = "READY TO SCAN" if has_photos else "READY"
        state_color = "#218739" if has_photos else "#40566F"

        ai_console_html = f"""<div style="background: #FFFFFF; border: 1px solid #D9DEE7; border-radius: 8px; padding: 1.1rem; font-size: 0.82rem; box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);">
<div style="color: #2F6FED; font-weight: 700; border-bottom: 1px solid #D9DEE7; padding-bottom: 6px; margin-bottom: 8px; text-transform: uppercase;">
AI RECOGNITION CONSOLE
</div>
<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
<span style="color: #667085;">STATUS:</span>
<strong style="color: {state_color};">● {scan_state}</strong>
</div>
<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
<span style="color: #667085;">QUEUE:</span>
<strong style="color: #172B4D;">{len(st.session_state.attendance_images)} PHOTOS</strong>
</div>
<div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
<span style="color: #667085;">ENGINE:</span>
<strong style="color: #172B4D;">Face Vectors 512-D</strong>
</div>
<div style="display: flex; justify-content: space-between; border-top: 1px solid #F0EFEA; padding-top: 6px;">
<span style="color: #667085;">VOICE CORE:</span>
<strong style="color: #218739;">READY</strong>
</div>
</div>"""
        st.markdown(ai_console_html, unsafe_allow_html=True)

    st.write("")

    # Action buttons
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button('Clear Photos', use_container_width=True, type='secondary', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()

    with b2:
        if st.button('🔍 Run Face Biometrics', use_container_width=True, type='primary', disabled=not has_photos):
            with st.spinner('Scanning classroom photos...'):
                from src.pipelines.face_pipeline import predict_attendance
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

    with b3:
        if st.button('🎙️ Voice Attendance', type='secondary', use_container_width=True):
            voice_attendance_dialog(selected_subject_id)


def teacher_tab_manage_subjects(subjects):
    teacher_id = st.session_state.teacher_data['teacher_id']
    col1, col2 = st.columns([3, 1.2], vertical_alignment='center')
    with col1:
        st.markdown("""<div>
<h3 style="font-size: 1.35rem; font-weight: 800; color: #172B4D; margin: 0 0 2px 0;">Active Subject Tiles</h3>
<p style="color: #667085; font-size: 0.88rem; margin: 0;">Create and organize your active classes and student rosters.</p>
</div>""", unsafe_allow_html=True)

    with col2:
        if st.button('➕ Create Subject', use_container_width=True, type='primary'):
            create_subject_dialog(teacher_id)

    st.write("")
    if subjects:
        for idx, sub in enumerate(subjects):
            stats = [
                ("Students", f"{sub['total_students']} enrolled"),
                ("Sessions", f"{sub['total_classes']} logged"),
            ]
            def action_buttons():
                bcol1, bcol2 = st.columns(2)
                with bcol1:
                    if st.button(f"🔗 Share Code: {sub['subject_code']}", key=f"share_{sub['subject_code']}", type='secondary', use_container_width=True):
                        share_subject_dialog(sub['name'], sub['subject_code'])
                with bcol2:
                    if st.button("🗑️ Delete Subject", key=f"del_{sub['subject_id']}", type='tertiary', use_container_width=True):
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
                footer_callback=action_buttons,
                tile_index=idx + 1
            )

            with st.expander(f"View Enrolled Students ({sub['total_students']})", expanded=False):
                enrolled = get_enrolled_students_for_subject(sub['subject_id'])
                if enrolled:
                    std_list = []
                    for s_idx, e in enumerate(enrolled, 1):
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
                            "#": s_idx,
                            "Student Name": std_name,
                            "Student ID": std_id,
                            "Enrolled On": enrolled_at or "N/A"
                        })
                    st.dataframe(pd.DataFrame(std_list), use_container_width=True, hide_index=True)
                else:
                    st.info(f"No students enrolled in {sub['name']} yet. Click 'Share Code' above to invite students.")
            st.write("")
    else:
        st.info("No courses registered under your account. Click 'Create Subject' above to get started.")

    # Other existing subjects in system available to claim
    all_subs = get_all_existing_subjects()
    other_subs = [s for s in all_subs if s.get('teacher_id') != teacher_id]
    if other_subs:
        st.write("")
        with st.expander(f"System Courses Available to Claim ({len(other_subs)})", expanded=False):
            st.markdown("<p style='color: #667085; font-size: 0.88rem;'>Courses from previous setups. You can link them to your account with one click:</p>", unsafe_allow_html=True)
            for oth in other_subs:
                c_info, c_btn = st.columns([3, 1.2], vertical_alignment='center')
                with c_info:
                    owner = oth.get('teachers', {}).get('name', 'Another account') if oth.get('teachers') else 'Another account'
                    st.markdown(f"**{oth['name']}** (`{oth['subject_code']}`) &bull; Section: {oth.get('section', 'N/A')} &bull; Owner: *{owner}* &bull; Enrolled: **{oth.get('total_students', 0)}**")
                with c_btn:
                    if st.button("Claim Subject", key=f"claim_other_{oth['subject_id']}", type="primary", use_container_width=True):
                        claim_subject(oth['subject_code'], teacher_id)
                        st.toast(f"Transferred '{oth['name']}' to your account!")
                        time.sleep(0.5)
                        st.rerun()
                st.divider()


def teacher_tab_attendance_records(records):
    st.markdown("""<div>
<h3 style="font-size: 1.35rem; font-weight: 800; color: #172B4D; margin: 0 0 2px 0;">Attendance Timeline</h3>
<p style="color: #667085; font-size: 0.88rem; margin: 0;">Chronological log of past class sessions and student presence.</p>
</div>""", unsafe_allow_html=True)

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
        st.markdown(f"<p style='color: #40566F; font-weight: 600; margin: 0;'>Total Logged Sessions: <strong style='color: #172B4D;'>{len(sessions_map)}</strong></p>", unsafe_allow_html=True)
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

    # TIMELINE DISPLAY
    for (ts, sid), sess in sorted(sessions_map.items(), key=lambda x: str(x[0][0]), reverse=True):
        logs = sess['logs']
        present_count = sum(1 for l in logs if l['Status'] == "Present")
        total_count = len(logs)
        turnout_pct = int(present_count / total_count * 100) if total_count > 0 else 0
        pct_color = "#218739" if turnout_pct >= 75 else "#B7791F"
        
        timeline_node_html = f"""<div style="background: #FFFFFF; border: 1px solid #D9DEE7; border-left: 4px solid #172B4D; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">
<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
<div>
<span style="font-size: 0.76rem; font-weight: 600; color: #667085;">{sess['formatted_time']}</span>
<h4 style="margin: 2px 0; font-size: 1.1rem; font-weight: 700; color: #172B4D;">
{sess['subject_name']} <span style="font-size: 0.82rem; font-weight: 600; color: #667085;">[{sess['subject_code']}]</span>
</h4>
</div>
<div style="text-align: right;">
<span style="font-size: 1.15rem; font-weight: 800; color: {pct_color}; font-family: 'Plus Jakarta Sans', sans-serif;">{present_count} / {total_count} Present</span>
<span style="display: block; font-size: 0.74rem; font-weight: 600; color: #667085;">TURNOUT: {turnout_pct}%</span>
</div>
</div>
</div>"""
        st.markdown(timeline_node_html, unsafe_allow_html=True)

        with st.expander("Session Roster Details", expanded=False):
            c_info, c_del = st.columns([3, 1.2], vertical_alignment='center')
            with c_info:
                st.caption(f"Recorded timestamp: {ts}")
            with c_del:
                clean_ts_id = str(ts).replace("-", "_").replace(":", "_").replace(".", "_")
                delete_key = f"del_sess_{clean_ts_id}_{sid}"
                if st.button("Delete Session", key=delete_key, type="tertiary", use_container_width=True):
                    delete_attendance_session(ts, sid)
                    st.toast("Deleted attendance session.")
                    time.sleep(0.5)
                    st.rerun()

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
    c1, c2 = st.columns([3, 1], vertical_alignment='center')
    with c1:
        header_dashboard(page_title="Instructor Authentication")
    with c2:
        if st.button("← Home", type='secondary', key='loginbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.write("")
    with st.container(border=True):
        login_header_html = """<div style="margin-bottom: 14px;">
<div style="display: inline-block; background: #EEF4FF; color: #2F6FED; border: 1px solid #CFE0FC; padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; margin-bottom: 6px;">
Faculty Access
</div>
<h2 style="font-size: 1.4rem; font-weight: 800; color: #172B4D; margin: 0 0 4px 0;">Teacher Sign In</h2>
<p style="color: #667085; font-size: 0.88rem; margin: 0;">Access your courses, rosters, and take automated attendance.</p>
</div>"""
        st.markdown(login_header_html, unsafe_allow_html=True)

        teacher_username = st.text_input("Username", placeholder='e.g. ronakjain')
        teacher_pass = st.text_input("Password", type='password', placeholder="Enter password")

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
    c1, c2 = st.columns([3, 1], vertical_alignment='center')
    with c1:
        header_dashboard(page_title="Instructor Registration")
    with c2:
        if st.button("← Home", type='secondary', key='regbackbtn', use_container_width=True):
            st.session_state['login_type'] = None
            st.rerun()

    st.write("")
    with st.container(border=True):
        reg_html = """<div style="margin-bottom: 14px;">
<div style="display: inline-block; background: #EAF6ED; color: #218739; border: 1px solid #BFE3C7; padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; margin-bottom: 6px;">
Account Setup
</div>
<h2 style="font-size: 1.4rem; font-weight: 800; color: #172B4D; margin: 0 0 4px 0;">Instructor Registration</h2>
<p style="color: #667085; font-size: 0.88rem; margin: 0;">Create educator credentials to manage digital classroom attendance.</p>
</div>"""
        st.markdown(reg_html, unsafe_allow_html=True)

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
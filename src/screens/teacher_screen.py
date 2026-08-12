import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
import time

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import (
    check_teacher_exists, create_teacher, teacher_login, 
    get_teacher_subjects, get_attendance_for_teacher,
    delete_attendance_session, delete_all_attendance_for_teacher
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
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"Welcome, {teacher_data['name']}")
        if st.button("Logout 🚪", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            if 'teacher_data' in st.session_state:
                del st.session_state.teacher_data
            st.rerun()

    st.write("")

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'
    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button('📷 Take Attendance', type=type1, use_container_width=True):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
        if st.button('📚 Manage Subjects', type=type2, use_container_width=True):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
        if st.button('📋 Attendance Records', type=type3, use_container_width=True):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    elif st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    elif st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()

    footer_dashboard()


def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data['teacher_id']
    st.header('Take AI Attendance')

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You haven\'t created any subjects yet! Please create one under "Manage Subjects" to begin!')
        return
    
    subject_options = {f"{s['name']} - {s['subject_code']}": s['subject_id'] for s in subjects}

    col1, col2 = st.columns([3, 1], vertical_alignment='bottom')

    with col1:
        selected_subject_label = st.selectbox('Select Subject', options=list(subject_options.keys()))

    with col2:
        if st.button('🖼️ Add Photos', type='primary', use_container_width=True):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()

    if st.session_state.attendance_images:
        st.header('Added Photos')
        gallery_cols = st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, use_container_width=True, caption=f'Photo {idx+1}')

    has_photos = bool(st.session_state.attendance_images)
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button('🗑️ Clear all photos', use_container_width=True, type='tertiary', disabled=not has_photos):
            st.session_state.attendance_images = []
            st.rerun()

    with c2:
        if st.button('🔍 Run Face Analysis', use_container_width=True, type='secondary', disabled=not has_photos):
            with st.spinner('Deep scanning classroom photos...'):
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
                    st.warning('No students enrolled in this course yet. Share your subject code with students so they can enroll!')
                elif total_faces_scanned == 0:
                    st.warning('No human faces were detected in the uploaded photos. Please upload clearer classroom photos.')
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
                            "Status": "✅ Present" if is_present else "❌ Absent"
                        })

                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestamp,
                            'is_present': bool(is_present)
                        })

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        if st.button('🎙️ Voice Attendance', type='primary', use_container_width=True):
            voice_attendance_dialog(selected_subject_id)


def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data['teacher_id']
    col1, col2 = st.columns(2)
    with col1:
        st.header('Manage Subjects')

    with col2:
        if st.button('➕ Create New Subject', use_container_width=True, type='primary'):
            create_subject_dialog(teacher_id)

    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("🫂", "Students", sub['total_students']),
                ("🕰️", "Classes", sub['total_classes']),
            ]
            def share_btn():
                if st.button(f"🔗 Share Code: {sub['name']}", key=f"share_{sub['subject_code']}", type='tertiary', use_container_width=True):
                    share_subject_dialog(sub['name'], sub['subject_code'])
                st.write("")

            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=stats,
                footer_callback=share_btn
            )
    else:
        st.info("NO SUBJECTS FOUND. CREATE ONE ABOVE")


def teacher_tab_attendance_records():
    st.header('Attendance Records')

    teacher_id = st.session_state.teacher_data['teacher_id']
    records = get_attendance_for_teacher(teacher_id)

    if not records:
        st.info("No attendance records found yet.")
        return
    
    # Process and group attendance records by timestamp and subject
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
                    formatted_time = datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p")
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
        
        # Get student details
        student_res = supabase.table('students').select('name').eq('student_id', r['student_id']).execute()
        student_name = student_res.data[0]['name'] if (student_res and student_res.data) else f"Student #{r['student_id']}"
        
        sessions_map[session_key]['logs'].append({
            'Name': student_name,
            'ID': r['student_id'],
            'Status': "✅ Present" if r.get('is_present') else "❌ Absent"
        })

    # Header Bar: Stats & Clear All Button
    col1, col2 = st.columns([2.5, 1.5], vertical_alignment='center')
    with col1:
        st.markdown(f"<p style='color: #475569; font-weight: 600; margin: 0;'>Total Logged Sessions: <span style='color: #5865F2; font-weight: 800;'>{len(sessions_map)}</span></p>", unsafe_allow_html=True)
    with col2:
        if st.button("🗑️ Clear All History", type="tertiary", use_container_width=True):
            if st.session_state.get('confirm_clear_all'):
                delete_all_attendance_for_teacher(teacher_id)
                st.session_state.confirm_clear_all = False
                st.toast("All attendance records deleted successfully! 🗑️")
                st.rerun()
            else:
                st.session_state.confirm_clear_all = True
                st.warning("Click again to confirm deleting ALL attendance history.")

    st.write("")

    # Display sessions sorted by newest first
    for (ts, sid), sess in sorted(sessions_map.items(), key=lambda x: str(x[0][0]), reverse=True):
        logs = sess['logs']
        present_count = sum(1 for l in logs if "Present" in l['Status'])
        total_count = len(logs)
        
        with st.expander(f"📅 {sess['formatted_time']} | 📚 {sess['subject_code']} - {sess['subject_name']} ({present_count}/{total_count} Present)"):
            c_info, c_del = st.columns([2.5, 1.5], vertical_alignment='center')
            
            with c_info:
                st.markdown(f"**Course:** {sess['subject_name']} (`{sess['subject_code']}`)")
                st.markdown(f"**Attendance:** ✅ `{present_count}` Present | ❌ `{total_count - present_count}` Absent")
            
            with c_del:
                clean_ts_id = str(ts).replace("-", "_").replace(":", "_").replace(".", "_")
                delete_key = f"del_sess_{clean_ts_id}_{sid}"
                if st.button("🗑️ Delete Session", key=delete_key, type="tertiary", use_container_width=True):
                    delete_attendance_session(ts, sid)
                    st.toast(f"Deleted attendance session for {sess['formatted_time']}! 🗑️")
                    time.sleep(0.5)
                    st.rerun()
            
            st.markdown("<h5 style='margin-top: 10px; color: #0f172a;'>Student Roster Status:</h5>", unsafe_allow_html=True)
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
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("⬅️ Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header('Login using password', anchor=False)
    st.write("")

    teacher_username = st.text_input("Enter username", placeholder='ronakjain')
    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button('🔑 Login', shortcut='control+enter', use_container_width=True, type='primary'):
            if login_teacher(teacher_username, teacher_pass):
                st.toast("Welcome back!", icon="👋")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username and password combo")

    with btnc2:
        if st.button('📝 Register Instead', type="secondary", use_container_width=True):
            st.session_state.teacher_login_type = 'register'
            st.rerun()

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All Fields are required!"
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"
    if teacher_pass != teacher_pass_confirm:
        return False, "Password doesn't match"
    
    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Sucessfully Created! Login Now"
    except Exception as e:
        return False, "Unexpected Error!"


def teacher_screen_register():
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("⬅️ Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header('Register your teacher profile')
    st.write("")

    teacher_username = st.text_input("Enter username", placeholder='ronakjain')
    teacher_name = st.text_input("Enter name", placeholder='Ronak Jain')
    teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")
    teacher_pass_confirm = st.text_input("Confirm your password", type='password', placeholder="Enter password")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button('📝 Register now', shortcut='control+enter', use_container_width=True, type='primary'):
            success, message = register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm)
            if success:
                st.success(message)
                time.sleep(1.5)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)

    with btnc2:
        if st.button('🔑 Login Instead', type="secondary", use_container_width=True):
            st.session_state.teacher_login_type = 'login'
            st.rerun()

    footer_dashboard()
import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', subject_code).execute()
    if not res.data:
        st.error('Subject Code not found!')
        if st.button('Close', use_container_width=True):
            st.query_params.clear()
            st.rerun()
        return
    subject = res.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
    if check.data:
        st.info(f"You are already enrolled in **{subject['name']}**!")
        if st.button('Got it!', type='primary', use_container_width=True):
            st.query_params.clear()
            st.rerun()
        return

    st.markdown(f"""
        <div style="text-align: center; padding: 0.5rem 0 1rem 0;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎯</div>
            <h3 style="color: #0f172a !important; margin: 0 0 0.5rem 0; font-weight: 800;">Class Invitation</h3>
            <p style="color: #475569 !important; font-size: 1.05rem;">Would you like to enroll in <strong>{subject['name']}</strong> (<code>{subject['subject_code']}</code>)?</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        if st.button('No thanks', type='tertiary', use_container_width=True):
            st.query_params.clear()
            st.rerun()
    with col2:
        if st.button('Yes, enroll now!', type='primary', use_container_width=True):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success('Joined successfully! Welcome to class! 🎉')
            st.query_params.clear()
            time.sleep(1.5)
            st.rerun()

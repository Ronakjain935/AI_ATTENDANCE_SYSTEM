import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Course Invitation")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data['student_id']

    res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', subject_code).execute()
    if not res.data:
        st.error('Course code not found or expired.')
        if st.button('Close', use_container_width=True):
            st.query_params.clear()
            st.rerun()
        return
    subject = res.data[0]

    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
    if check.data:
        st.info(f"You are already enrolled in **{subject['name']}**.")
        if st.button('Continue to Dashboard', type='primary', use_container_width=True):
            st.query_params.clear()
            st.rerun()
        return

    invitation_html = f"""<div style="text-align: center; padding: 0.5rem 0 1rem 0;">
<div style="display: inline-block; background: #EEF4FF; color: #2F6FED; border: 1px solid #CFE0FC; padding: 3px 10px; border-radius: 4px; font-size: 0.74rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px;">
Course Invitation
</div>
<h3 style="color: #172B4D; margin: 0 0 0.4rem 0; font-weight: 700; font-size: 1.3rem;">
{subject['name']}
</h3>
<p style="color: #667085; font-size: 0.88rem; margin: 0;">Code: <strong style="color: #172B4D; font-family: monospace;">{subject['subject_code']}</strong></p>
<p style="color: #1F2937; font-size: 0.90rem; margin-top: 10px;">Would you like to enroll in this course roster?</p>
</div>"""
    st.markdown(invitation_html, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        if st.button('Cancel', type='secondary', use_container_width=True):
            st.query_params.clear()
            st.rerun()
    with col2:
        if st.button('Enroll Now', type='primary', use_container_width=True):
            enroll_student_to_subject(student_id, subject['subject_id'])
            st.success('Enrolled successfully!')
            st.query_params.clear()
            time.sleep(0.8)
            st.rerun()

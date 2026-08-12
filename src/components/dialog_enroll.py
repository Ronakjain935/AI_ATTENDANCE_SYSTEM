import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.markdown("<p style='color: #475569 !important; font-size: 0.95rem; margin-bottom: 1rem;'>Enter the subject code provided by your teacher to enroll in the course.</p>", unsafe_allow_html=True)
    
    join_code = st.text_input('Subject Code', placeholder='e.g. CS101')

    st.markdown("<div style='margin-top: 1.2rem;'></div>", unsafe_allow_html=True)
    if st.button('Enroll Now', type='primary', use_container_width=True):
        if join_code:
            res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', join_code.strip()).execute()
            if res.data:
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                if check.data:
                    st.warning('You are already enrolled in this course!')
                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success(f'Successfully enrolled in {subject["name"]}!')
                    time.sleep(1)
                    st.rerun()
            else:
                st.error('Invalid Subject Code. Please verify with your teacher.')
        else:
            st.warning('Please enter a subject code.')
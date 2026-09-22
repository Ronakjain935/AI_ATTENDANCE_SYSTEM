import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time

@st.dialog("Enroll in Course")
def enroll_dialog():
    st.markdown("<p style='color: #667085; font-size: 0.88rem; margin-bottom: 1rem;'>Enter the unique course code provided by your instructor.</p>", unsafe_allow_html=True)
    
    join_code = st.text_input('Course Code', placeholder='e.g. CS101, MATH204')

    st.write("")
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("Cancel", type="secondary", use_container_width=True):
            st.rerun()

    with btn_col2:
        if st.button('Enroll Now', type='primary', use_container_width=True):
            if join_code:
                code = join_code.strip().upper()
                res = supabase.table('subjects').select('subject_id, name, subject_code').eq('subject_code', code).execute()
                if res.data:
                    subject = res.data[0]
                    student_id = st.session_state.student_data['student_id']

                    check = supabase.table('subject_students').select('*').eq('subject_id', subject['subject_id']).eq('student_id', student_id).execute()
                    if check.data:
                        st.warning('You are already enrolled in this course.')
                    else:
                        enroll_student_to_subject(student_id, subject['subject_id'])
                        st.success(f'Successfully joined {subject["name"]}!')
                        time.sleep(0.8)
                        st.rerun()
                else:
                    st.error('Invalid course code. Please verify with your instructor.')
            else:
                st.warning('Please enter a course code.')
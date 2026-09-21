import streamlit as st
from src.database.db import create_attendance
import time

def show_attendance_result(df, logs):
    st.markdown("<p style='color: #475569; font-size: 0.9rem; font-weight: 500; margin-bottom: 12px;'>Review the attendance verification results before confirming.</p>", unsafe_allow_html=True)
    
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', use_container_width=True, type='tertiary'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Confirm & Save', use_container_width=True, type='primary'):
            try:
                create_attendance(logs)
                st.toast("Attendance recorded successfully!", icon="✅")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                time.sleep(0.5)
                st.rerun()
            except Exception as e:
                st.error(f'Failed to record attendance: {str(e)}')

@st.dialog("Attendance Verification")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)

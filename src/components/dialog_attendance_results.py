import streamlit as st
import pandas as pd
from src.database.db import create_attendance
import time

def show_attendance_result(df, logs):
    total_count = len(df)
    present_count = len(df[df['Status'] == 'Present']) if 'Status' in df.columns else 0
    absent_count = total_count - present_count
    attendance_rate = int(present_count / total_count * 100) if total_count > 0 else 0
    rate_color = "#218739" if attendance_rate >= 75 else ("#B7791F" if attendance_rate >= 60 else "#C53030")

    # Attendance Verification KPI Bar
    stats_html = f"""<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 14px;">
<div style="background: #F7F6F2; border: 1px solid #D9DEE7; border-radius: 8px; padding: 8px 10px; text-align: center;">
<span style="display: block; font-size: 0.68rem; font-weight: 700; color: #667085; text-transform: uppercase;">Total</span>
<strong style="font-size: 1.2rem; color: #172B4D; font-weight: 800;">{total_count}</strong>
</div>
<div style="background: #F7F6F2; border: 1px solid #D9DEE7; border-radius: 8px; padding: 8px 10px; text-align: center;">
<span style="display: block; font-size: 0.68rem; font-weight: 700; color: #218739; text-transform: uppercase;">Present</span>
<strong style="font-size: 1.2rem; color: #218739; font-weight: 800;">{present_count}</strong>
</div>
<div style="background: #F7F6F2; border: 1px solid #D9DEE7; border-radius: 8px; padding: 8px 10px; text-align: center;">
<span style="display: block; font-size: 0.68rem; font-weight: 700; color: #C53030; text-transform: uppercase;">Absent</span>
<strong style="font-size: 1.2rem; color: #C53030; font-weight: 800;">{absent_count}</strong>
</div>
<div style="background: #F7F6F2; border: 1px solid #D9DEE7; border-radius: 8px; padding: 8px 10px; text-align: center;">
<span style="display: block; font-size: 0.68rem; font-weight: 700; color: #667085; text-transform: uppercase;">Turnout</span>
<strong style="font-size: 1.2rem; color: {rate_color}; font-weight: 800;">{attendance_rate}%</strong>
</div>
</div>"""
    st.markdown(stats_html, unsafe_allow_html=True)

    # Search & Filter row
    f_col1, f_col2 = st.columns([2, 1.2], vertical_alignment='center')
    with f_col1:
        search_query = st.text_input("Filter student name / ID", placeholder="Search roster...", label_visibility="collapsed")
    with f_col2:
        status_filter = st.selectbox("Status", options=["All Students", "Present Only", "Absent Only"], label_visibility="collapsed")

    filtered_df = df.copy()
    if search_query:
        query = search_query.strip().lower()
        filtered_df = filtered_df[
            filtered_df['Name'].astype(str).str.lower().str.contains(query) | 
            filtered_df['ID'].astype(str).str.lower().str.contains(query)
        ]
    if status_filter == "Present Only":
        filtered_df = filtered_df[filtered_df['Status'] == 'Present']
    elif status_filter == "Absent Only":
        filtered_df = filtered_df[filtered_df['Status'] == 'Absent']

    st.dataframe(filtered_df, hide_index=True, use_container_width=True)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', use_container_width=True, type='secondary'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Confirm & Save Attendance', use_container_width=True, type='primary'):
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

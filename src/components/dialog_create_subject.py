import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown("<p style='color: #475569 !important; font-size: 0.95rem; margin-bottom: 1rem;'>Enter the details of the new subject below:</p>", unsafe_allow_html=True)
    
    sub_id = st.text_input("Subject Code", placeholder="e.g. CS101")
    sub_name = st.text_input("Subject Name", placeholder="e.g. Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="e.g. Section A")

    st.markdown("<div style='margin-top: 1.2rem;'></div>", unsafe_allow_html=True)
    if st.button("Create Subject Now", type='primary', use_container_width=True):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id.strip(), sub_name.strip(), sub_section.strip(), teacher_id)
                st.toast("Subject Created Successfully! 🎉")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please fill in all required fields.")

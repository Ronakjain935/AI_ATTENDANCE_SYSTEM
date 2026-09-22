import streamlit as st
import time
from src.database.db import create_subject
from src.database.config import supabase

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown("<p style='color: #667085; font-size: 0.88rem; margin-bottom: 1rem;'>Enter course information to register a new classroom roster.</p>", unsafe_allow_html=True)
    
    sub_id = st.text_input("Subject / Course Code", placeholder="e.g. CS101, MATH204")
    sub_name = st.text_input("Course Title", placeholder="e.g. Introduction to Computer Science")
    sub_section = st.text_input("Section / Cohort", placeholder="e.g. Section A, Lab 2")

    st.write("")
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("Cancel", type="secondary", use_container_width=True):
            st.rerun()

    with btn_col2:
        if st.button("Create Subject", type='primary', use_container_width=True):
            if sub_id and sub_name and sub_section:
                code = sub_id.strip().upper()
                name = sub_name.strip()
                section = sub_section.strip()

                # Pre-check if subject code already exists in database
                existing = None
                try:
                    existing = supabase.table('subjects').select('*').eq('subject_code', code).execute()
                except Exception:
                    pass

                if existing and existing.data:
                    try:
                        supabase.table('subjects').update({
                            'name': name,
                            'section': section,
                            'teacher_id': teacher_id
                        }).eq('subject_code', code).execute()
                        st.success(f"Existing course '{code}' updated and linked to your account.")
                        time.sleep(0.8)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error linking course: {str(e)}")
                else:
                    try:
                        create_subject(code, name, section, teacher_id)
                        st.toast("Course created successfully!", icon="✅")
                        time.sleep(0.8)
                        st.rerun()
                    except Exception as e:
                        err_str = str(e)
                        if "23505" in err_str or "unique constraint" in err_str:
                            try:
                                supabase.table('subjects').update({
                                    'name': name,
                                    'section': section,
                                    'teacher_id': teacher_id
                                }).eq('subject_code', code).execute()
                                st.success(f"Course '{code}' linked to your account.")
                                time.sleep(0.8)
                                st.rerun()
                            except Exception:
                                st.error(f"Course code '{code}' already exists.")
                        else:
                            st.error(f"Error: {err_str}")
            else:
                st.warning("Please fill in all course fields.")

import streamlit as st
import time
from src.database.db import create_subject
from src.database.config import supabase

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown("<p style='color: #475569 !important; font-size: 0.95rem; margin-bottom: 1rem;'>Enter the details of the subject below:</p>", unsafe_allow_html=True)
    
    sub_id = st.text_input("Subject Code", placeholder="e.g. CS101")
    sub_name = st.text_input("Subject Name", placeholder="e.g. Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="e.g. Section A")

    st.markdown("<div style='margin-top: 1.2rem;'></div>", unsafe_allow_html=True)
    if st.button("Save & Add Subject", type='primary', use_container_width=True):
        if sub_id and sub_name and sub_section:
            code = sub_id.strip()
            name = sub_name.strip()
            section = sub_section.strip()

            # Pre-check if subject code already exists in database
            existing = None
            try:
                existing = supabase.table('subjects').select('*').eq('subject_code', code).execute()
            except Exception:
                pass

            if existing and existing.data:
                # Subject already exists in database: auto-link and update it to current teacher!
                try:
                    supabase.table('subjects').update({
                        'name': name,
                        'section': section,
                        'teacher_id': teacher_id
                    }).eq('subject_code', code).execute()
                    st.success(f"Existing subject '{code}' has been updated and linked to your account! 🎉")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(f"Error linking subject: {str(e)}")
            else:
                try:
                    create_subject(code, name, section, teacher_id)
                    st.toast("Subject Created Successfully! 🎉")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    err_str = str(e)
                    if "23505" in err_str or "unique constraint" in err_str:
                        # Fallback recovery: update and link
                        try:
                            supabase.table('subjects').update({
                                'name': name,
                                'section': section,
                                'teacher_id': teacher_id
                            }).eq('subject_code', code).execute()
                            st.success(f"Subject '{code}' has been linked to your account! 🎉")
                            time.sleep(1)
                            st.rerun()
                        except Exception:
                            st.error(f"Subject code '{code}' already exists in database.")
                    else:
                        st.error(f"Error: {err_str}")
        else:
            st.warning("Please fill in all required fields.")

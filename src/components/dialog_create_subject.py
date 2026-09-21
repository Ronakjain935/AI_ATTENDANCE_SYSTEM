import streamlit as st
import time
from src.database.db import create_subject, claim_subject
from src.database.config import supabase

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    st.markdown("<p style='color: #475569 !important; font-size: 0.95rem; margin-bottom: 1rem;'>Enter the details of the new subject below:</p>", unsafe_allow_html=True)
    
    sub_id = st.text_input("Subject Code", placeholder="e.g. CS101")
    sub_name = st.text_input("Subject Name", placeholder="e.g. Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="e.g. Section A")

    st.markdown("<div style='margin-top: 1.2rem;'></div>", unsafe_allow_html=True)
    if st.button("Create Subject Now", type='primary', use_container_width=True):
        if sub_id and sub_name and sub_section:
            code = sub_id.strip()
            # Pre-check if subject code already exists in database
            existing = None
            try:
                existing = supabase.table('subjects').select('*, teachers(name, username)').eq('subject_code', code).execute()
            except Exception:
                pass

            if existing and existing.data:
                sub = existing.data[0]
                owner_name = sub.get('teachers', {}).get('name', 'Another account') if sub.get('teachers') else 'Another account'
                st.error(f"⚠️ Subject code **'{code}'** already exists in the database (Registered under: **{owner_name}**).")
                st.info(f"If you created **'{code}'** under a previous login, click below to link it to your current account:")
                if st.button(f"🔄 Link '{code}' to My Account", type="primary", use_container_width=True, key=f"claim_{code}"):
                    claim_subject(code, teacher_id)
                    st.success(f"Transferred '{code}' to your account! 🎉")
                    time.sleep(1)
                    st.rerun()
            else:
                try:
                    create_subject(code, sub_name.strip(), sub_section.strip(), teacher_id)
                    st.toast("Subject Created Successfully! 🎉")
                    time.sleep(1)
                    st.rerun()
                except Exception as e:
                    err_str = str(e)
                    if "23505" in err_str or "unique constraint" in err_str:
                        st.error(f"⚠️ Subject code **'{code}'** already exists in the database.")
                        if st.button(f"🔄 Link '{code}' to My Account", type="primary", use_container_width=True, key=f"claim_err_{code}"):
                            claim_subject(code, teacher_id)
                            st.success(f"Transferred '{code}' to your account! 🎉")
                            time.sleep(1)
                            st.rerun()
                    else:
                        st.error(f"Error: {err_str}")
        else:
            st.warning("Please fill in all required fields.")

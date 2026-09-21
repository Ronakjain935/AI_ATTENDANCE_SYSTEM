import streamlit as st
import textwrap
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.utils.assets import get_asset_base64

def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    student_b64 = get_asset_base64("student_mascot.png")
    student_img_src = student_b64 if student_b64 else "https://i.ibb.co/844D9Lrt/mascot-student.png"

    teacher_b64 = get_asset_base64("teacher_mascot.png")
    teacher_img_src = teacher_b64 if teacher_b64 else "https://i.ibb.co/CsmQQV6X/mascot-prof.png"

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            card_student_html = textwrap.dedent(f"""\
<div style="text-align: center; padding-bottom: 8px;">
<div style="display: inline-block; background: #EEF2FF; color: #4338CA; border: 1px solid #E0E7FF; padding: 3px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 10px;">
Student Access
</div>
<h2 style="font-size: 1.45rem; font-weight: 700; color: #0F172A; margin: 0 0 6px 0;">Student Portal</h2>
<p style="color: #64748B; font-size: 0.88rem; line-height: 1.45; margin: 0 0 14px 0;">
Check into courses with facial verification and track your attendance records in real time.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 14px;">
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 130px; height: 130px;">
<img src="{student_img_src}" style="max-height: 110px; max-width: 100%; object-fit: contain;" alt="Student Mascot" />
</div>
</div>
<div style="text-align: left; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 14px; margin-bottom: 16px; font-size: 0.84rem; color: #334155;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="color: #4F46E5; font-weight: 700;">✓</span> Instant FaceID & Photo Check-in
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="color: #4F46E5; font-weight: 700;">✓</span> Join Classes via QR Code or PIN
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #4F46E5; font-weight: 700;">✓</span> Real-Time Attendance History
</div>
</div>
</div>\
""")
            st.markdown(card_student_html, unsafe_allow_html=True)
            if st.button("Enter Student Portal →", type="primary", use_container_width=True, key="student_btn"):
                st.session_state["login_type"] = "student"
                st.rerun()

    with col2:
        with st.container(border=True):
            card_teacher_html = textwrap.dedent(f"""\
<div style="text-align: center; padding-bottom: 8px;">
<div style="display: inline-block; background: #ECFDF5; color: #047857; border: 1px solid #A7F3D0; padding: 3px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.04em; text-transform: uppercase; margin-bottom: 10px;">
Instructor Control
</div>
<h2 style="font-size: 1.45rem; font-weight: 700; color: #0F172A; margin: 0 0 6px 0;">Teacher Portal</h2>
<p style="color: #64748B; font-size: 0.88rem; line-height: 1.45; margin: 0 0 14px 0;">
Take automated attendance with classroom photos, track course rosters, and review logs.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 14px;">
<div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 130px; height: 130px;">
<img src="{teacher_img_src}" style="max-height: 110px; max-width: 100%; object-fit: contain;" alt="Teacher Mascot" />
</div>
</div>
<div style="text-align: left; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 14px; margin-bottom: 16px; font-size: 0.84rem; color: #334155;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="color: #059669; font-weight: 700;">✓</span> Multi-Face Classroom Photo Scan
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="color: #059669; font-weight: 700;">✓</span> Voice Speaker Attendance Analysis
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #059669; font-weight: 700;">✓</span> Instant QR Code Sharing & Export
</div>
</div>
</div>\
""")
            st.markdown(card_teacher_html, unsafe_allow_html=True)
            if st.button("Enter Teacher Portal →", type="secondary", use_container_width=True, key="teacher_btn"):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    footer_home()
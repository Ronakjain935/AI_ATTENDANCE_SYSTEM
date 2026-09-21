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
<div style="text-align: center; padding-bottom: 4px;">
<div style="height: 3px; width: 44px; background: #1E3A8A; border-radius: 2px; margin: 0 auto 14px auto;"></div>
<div style="display: inline-flex; align-items: center; gap: 6px; background: #F8FAFC; color: #1E3A8A; border: 1px solid #CBD5E1; padding: 3px 12px; border-radius: 4px; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #1E3A8A;"></span>
Student Portal
</div>
<h2 style="font-size: 1.6rem; font-weight: 700; font-family: 'Lora', Georgia, serif; color: #0F172A; margin: 0 0 6px 0; letter-spacing: -0.015em;">Student Access</h2>
<p style="color: #475569; font-size: 0.88rem; line-height: 1.55; margin: 0 0 16px 0;">
Instant biometric attendance check-in, course roster status, and personal semester logs.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 16px;">
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 140px; height: 130px; box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);">
<img src="{student_img_src}" style="max-height: 110px; max-width: 100%; object-fit: contain;" alt="Student Portal Emblem" />
</div>
</div>
<div style="text-align: left; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 16px; margin-bottom: 18px; font-size: 0.84rem; color: #334155;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #1E3A8A; font-weight: 800; font-size: 0.92rem;">✓</span>
<span>Instant FaceID Biometric Check-In</span>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #1E3A8A; font-weight: 800; font-size: 0.92rem;">✓</span>
<span>1-Click Course Enrollment via QR / PIN</span>
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #1E3A8A; font-weight: 800; font-size: 0.92rem;">✓</span>
<span>Personal Attendance History & Analytics</span>
</div>
</div>
</div>\
""")
            st.markdown(card_student_html, unsafe_allow_html=True)
            if st.button("Access Student Portal  ➔", type="primary", use_container_width=True, key="student_btn"):
                st.session_state["login_type"] = "student"
                st.rerun()

    with col2:
        with st.container(border=True):
            card_teacher_html = textwrap.dedent(f"""\
<div style="text-align: center; padding-bottom: 4px;">
<div style="height: 3px; width: 44px; background: #047857; border-radius: 2px; margin: 0 auto 14px auto;"></div>
<div style="display: inline-flex; align-items: center; gap: 6px; background: #F8FAFC; color: #065F46; border: 1px solid #CBD5E1; padding: 3px 12px; border-radius: 4px; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #047857;"></span>
Faculty Portal
</div>
<h2 style="font-size: 1.6rem; font-weight: 700; font-family: 'Lora', Georgia, serif; color: #0F172A; margin: 0 0 6px 0; letter-spacing: -0.015em;">Instructor Console</h2>
<p style="color: #475569; font-size: 0.88rem; line-height: 1.55; margin: 0 0 16px 0;">
Take automated attendance with classroom photos, track course rosters, and export official logs.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 16px;">
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 140px; height: 130px; box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);">
<img src="{teacher_img_src}" style="max-height: 110px; max-width: 100%; object-fit: contain;" alt="Instructor Portal Emblem" />
</div>
</div>
<div style="text-align: left; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 16px; margin-bottom: 18px; font-size: 0.84rem; color: #334155;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #047857; font-weight: 800; font-size: 0.92rem;">✓</span>
<span>Multi-Face High Density Photo Scan</span>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #047857; font-weight: 800; font-size: 0.92rem;">✓</span>
<span>Voice Acoustic Speaker Roll-Call AI</span>
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #047857; font-weight: 800; font-size: 0.92rem;">✓</span>
<span>QR Code Sharing & Excel Roster Export</span>
</div>
</div>
</div>\
""")
            st.markdown(card_teacher_html, unsafe_allow_html=True)
            if st.button("Access Instructor Console  ➔", type="secondary", use_container_width=True, key="teacher_btn"):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    footer_home()
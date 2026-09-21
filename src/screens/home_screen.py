import streamlit as st
import textwrap
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home, render_theme_toggle, get_current_theme
from src.utils.assets import get_asset_base64

def home_screen():
    style_background_home()
    style_base_layout()

    # Top Bar with Theme Toggle
    top_c1, top_c2 = st.columns([4.2, 1.2], vertical_alignment="center")
    with top_c2:
        render_theme_toggle("home_theme_toggle")

    header_home()

    theme = get_current_theme()
    is_dark = (theme == "dark")

    card_bg = "#1E293B" if is_dark else "#FFFFFF"
    card_border = "#334155" if is_dark else "#CBD5E1"
    box_bg = "#0B0F19" if is_dark else "#F1F5F9"
    title_color = "#F8FAFC" if is_dark else "#0F172A"
    sub_color = "#94A3B8" if is_dark else "#475569"
    text_color = "#E2E8F0" if is_dark else "#1E293B"

    student_b64 = get_asset_base64("student_mascot.png")
    student_img_src = student_b64 if student_b64 else "https://i.ibb.co/844D9Lrt/mascot-student.png"

    teacher_b64 = get_asset_base64("teacher_mascot.png")
    teacher_img_src = teacher_b64 if teacher_b64 else "https://i.ibb.co/CsmQQV6X/mascot-prof.png"

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            card_student_html = textwrap.dedent(f"""\
<div style="text-align: center; padding-bottom: 4px;">
<div style="height: 3px; width: 44px; background: #2563EB; border-radius: 2px; margin: 0 auto 12px auto;"></div>
<div style="display: inline-flex; align-items: center; gap: 6px; background: {box_bg}; color: {'#38BDF8' if is_dark else '#1E3A8A'}; border: 1px solid {card_border}; padding: 3px 12px; border-radius: 4px; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #2563EB;"></span>
Student Portal
</div>
<h2 style="font-size: 1.65rem; font-weight: 800; color: {title_color}; margin: 0 0 6px 0;">Student Access</h2>
<p style="color: {sub_color}; font-size: 0.90rem; line-height: 1.5; margin: 0 0 16px 0;">
Instant biometric attendance check-in, course roster status, and personal semester logs.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 16px;">
<div style="background: {box_bg}; border: 1px solid {card_border}; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 140px; height: 130px;">
<img src="{student_img_src}" style="max-height: 110px; max-width: 100%; object-fit: contain;" alt="Student Portal Emblem" />
</div>
</div>
<div style="text-align: left; background: {box_bg}; border: 1px solid {card_border}; border-radius: 8px; padding: 12px 16px; margin-bottom: 18px; font-size: 0.88rem; color: {text_color}; font-weight: 500;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #2563EB; font-weight: 900; font-size: 1rem;">✓</span>
<span>Instant FaceID Biometric Check-In</span>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #2563EB; font-weight: 900; font-size: 1rem;">✓</span>
<span>1-Click Course Enrollment via QR / PIN</span>
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #2563EB; font-weight: 900; font-size: 1rem;">✓</span>
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
<div style="height: 3px; width: 44px; background: #16A34A; border-radius: 2px; margin: 0 auto 12px auto;"></div>
<div style="display: inline-flex; align-items: center; gap: 6px; background: {box_bg}; color: {'#4ADE80' if is_dark else '#047857'}; border: 1px solid {card_border}; padding: 3px 12px; border-radius: 4px; font-size: 0.75rem; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 10px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #16A34A;"></span>
Faculty Portal
</div>
<h2 style="font-size: 1.65rem; font-weight: 800; color: {title_color}; margin: 0 0 6px 0;">Instructor Console</h2>
<p style="color: {sub_color}; font-size: 0.90rem; line-height: 1.5; margin: 0 0 16px 0;">
Take automated attendance with classroom photos, track course rosters, and export official logs.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 16px;">
<div style="background: {box_bg}; border: 1px solid {card_border}; border-radius: 12px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 140px; height: 130px;">
<img src="{teacher_img_src}" style="max-height: 110px; max-width: 100%; object-fit: contain;" alt="Instructor Portal Emblem" />
</div>
</div>
<div style="text-align: left; background: {box_bg}; border: 1px solid {card_border}; border-radius: 8px; padding: 12px 16px; margin-bottom: 18px; font-size: 0.88rem; color: {text_color}; font-weight: 500;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #16A34A; font-weight: 900; font-size: 1rem;">✓</span>
<span>Multi-Face High Density Photo Scan</span>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #16A34A; font-weight: 900; font-size: 1rem;">✓</span>
<span>Voice Acoustic Speaker Roll-Call AI</span>
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #16A34A; font-weight: 900; font-size: 1rem;">✓</span>
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
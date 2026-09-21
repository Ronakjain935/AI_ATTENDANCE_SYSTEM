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
<div style="text-align: center; padding-bottom: 6px;">
<div style="height: 4px; width: 48px; background: linear-gradient(90deg, #4F46E5, #38BDF8); border-radius: 999px; margin: 0 auto 14px auto;"></div>
<div style="display: inline-flex; align-items: center; gap: 6px; background: #EEF2FF; color: #4338CA; border: 1px solid #E0E7FF; padding: 3px 12px; border-radius: 999px; font-size: 0.74rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 10px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #4F46E5;"></span>
Student Access
</div>
<h2 style="font-size: 1.55rem; font-weight: 800; color: #0F172A; margin: 0 0 6px 0; letter-spacing: -0.02em;">Student Portal</h2>
<p style="color: #64748B; font-size: 0.88rem; line-height: 1.5; margin: 0 0 16px 0;">
Verify attendance instantly with FaceID and track your course status across the semester.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 16px;">
<div style="background: linear-gradient(180deg, #F8FAFC 0%, #EDF2F7 100%); border: 1px solid #E2E8F0; border-radius: 16px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 140px; height: 135px; box-shadow: inset 0 1px 0 rgba(255,255,255,0.8), 0 4px 8px -2px rgba(0,0,0,0.04);">
<img src="{student_img_src}" style="max-height: 115px; max-width: 100%; object-fit: contain;" alt="Student Mascot" />
</div>
</div>
<div style="text-align: left; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 12px 16px; margin-bottom: 18px; font-size: 0.84rem; color: #334155;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #4F46E5; font-weight: 800; font-size: 0.9rem;">✓</span>
<span>Instant FaceID Biometric Check-In</span>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #4F46E5; font-weight: 800; font-size: 0.9rem;">✓</span>
<span>1-Click Course Enrollment via QR / PIN</span>
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #4F46E5; font-weight: 800; font-size: 0.9rem;">✓</span>
<span>Personal Attendance History & Analytics</span>
</div>
</div>
</div>\
""")
            st.markdown(card_student_html, unsafe_allow_html=True)
            if st.button("Enter Student Portal  ➔", type="primary", use_container_width=True, key="student_btn"):
                st.session_state["login_type"] = "student"
                st.rerun()

    with col2:
        with st.container(border=True):
            card_teacher_html = textwrap.dedent(f"""\
<div style="text-align: center; padding-bottom: 6px;">
<div style="height: 4px; width: 48px; background: linear-gradient(90deg, #059669, #10B981); border-radius: 999px; margin: 0 auto 14px auto;"></div>
<div style="display: inline-flex; align-items: center; gap: 6px; background: #ECFDF5; color: #047857; border: 1px solid #A7F3D0; padding: 3px 12px; border-radius: 999px; font-size: 0.74rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 10px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #059669;"></span>
Instructor Console
</div>
<h2 style="font-size: 1.55rem; font-weight: 800; color: #0F172A; margin: 0 0 6px 0; letter-spacing: -0.02em;">Teacher Portal</h2>
<p style="color: #64748B; font-size: 0.88rem; line-height: 1.5; margin: 0 0 16px 0;">
Take automated attendance with classroom photos, track course rosters, and export logs.
</p>
<div style="display: flex; justify-content: center; margin-bottom: 16px;">
<div style="background: linear-gradient(180deg, #F8FAFC 0%, #EDF2F7 100%); border: 1px solid #E2E8F0; border-radius: 16px; padding: 10px; display: inline-flex; align-items: center; justify-content: center; width: 140px; height: 135px; box-shadow: inset 0 1px 0 rgba(255,255,255,0.8), 0 4px 8px -2px rgba(0,0,0,0.04);">
<img src="{teacher_img_src}" style="max-height: 115px; max-width: 100%; object-fit: contain;" alt="Teacher Mascot" />
</div>
</div>
<div style="text-align: left; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 12px 16px; margin-bottom: 18px; font-size: 0.84rem; color: #334155;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #059669; font-weight: 800; font-size: 0.9rem;">✓</span>
<span>Multi-Face High Density Photo Scan</span>
</div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 7px;">
<span style="color: #059669; font-weight: 800; font-size: 0.9rem;">✓</span>
<span>Voice Acoustic Speaker Roll-Call AI</span>
</div>
<div style="display: flex; align-items: center; gap: 8px;">
<span style="color: #059669; font-weight: 800; font-size: 0.9rem;">✓</span>
<span>QR Code Sharing & Excel Roster Export</span>
</div>
</div>
</div>\
""")
            st.markdown(card_teacher_html, unsafe_allow_html=True)
            if st.button("Enter Instructor Portal  ➔", type="secondary", use_container_width=True, key="teacher_btn"):
                st.session_state["login_type"] = "teacher"
                st.rerun()

    footer_home()
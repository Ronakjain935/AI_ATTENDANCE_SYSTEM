import streamlit as st
import os
from src.utils.assets import get_asset_path, get_asset_base64

def header_home():
    """
    Renders the classic academic header for the home screen centered:
    SNAPCLASS branding, subtitle, AI ONLINE indicator, and hero section.
    """
    logo_b64 = get_asset_base64("logo.png")
    logo_src = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"

    header_html = f"""<div style="text-align: center; margin-bottom: 2rem;">
<div style="display: inline-flex; align-items: center; justify-content: center; gap: 14px; margin-bottom: 1.5rem; flex-wrap: wrap;">
    <img src="{logo_src}" width="42" height="42" style="border-radius: 8px; vertical-align: middle; object-fit: contain;" />
    <div style="text-align: left; line-height: 1.15;">
        <span style="font-size: 1.45rem; font-weight: 800; color: #172B4D; letter-spacing: -0.02em;">SNAPCLASS</span>
        <span style="display: block; font-size: 0.68rem; font-weight: 700; color: #40566F; letter-spacing: 0.08em; text-transform: uppercase;">SMART CLASSROOM. SMART ATTENDANCE.</span>
    </div>
    <div style="display: inline-flex; align-items: center; background: #E8F5E9; border: 1px solid #C8E6C9; padding: 4px 12px; border-radius: 9999px; margin-left: 8px; font-size: 0.74rem; font-weight: 700; color: #218739; letter-spacing: 0.04em;">
        <span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #218739; margin-right: 6px;"></span>
        AI ONLINE
    </div>
</div>

<!-- Centered Welcome Section -->
<div style="border-bottom: 1px solid #D9DEE7; padding-bottom: 1.75rem;">
    <div style="display: inline-block; font-size: 0.76rem; font-weight: 700; color: #2F6FED; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5rem; background: #EFF6FF; border: 1px solid #DBEAFE; padding: 4px 14px; border-radius: 9999px;">
        INSTITUTIONAL ATTENDANCE PLATFORM
    </div>
    <h1 style="font-size: 2.75rem; font-weight: 800; color: #172B4D; line-height: 1.15; margin: 0.35rem 0 0.65rem 0; text-align: center;">
        Smart Classroom
    </h1>
    <p style="color: #667085; font-size: 1.06rem; margin: 0 auto 1.35rem auto; max-width: 620px; line-height: 1.55; font-weight: 400; text-align: center;">
        AI-powered attendance management for modern classrooms. Rapid biometric verification via high-accuracy facial vectors and acoustic voice models.
    </p>
    <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center; align-items: center;">
        <span style="background: #FFFFFF; border: 1px solid #D9DEE7; color: #172B4D; font-size: 0.82rem; font-weight: 600; padding: 5px 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">● Instant Roll-Call</span>
        <span style="background: #FFFFFF; border: 1px solid #D9DEE7; color: #172B4D; font-size: 0.82rem; font-weight: 600; padding: 5px 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">● Multi-Face Biometrics</span>
        <span style="background: #FFFFFF; border: 1px solid #D9DEE7; color: #172B4D; font-size: 0.82rem; font-weight: 600; padding: 5px 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">● Voice Recognition</span>
        <span style="background: #FFFFFF; border: 1px solid #D9DEE7; color: #172B4D; font-size: 0.82rem; font-weight: 600; padding: 5px 14px; border-radius: 6px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">● QR & PIN Join</span>
    </div>
</div>
</div>"""
    st.markdown(header_html, unsafe_allow_html=True)


def header_dashboard(page_title="Dashboard", user_name=None, role=None):
    """
    Renders the fixed classic academic header for dashboard screens:
    Left: SNAPCLASS logo
    Center/Left: Current page title
    Right: User profile + AI ONLINE status indicator
    """
    logo_path = get_asset_path("logo.png")
    
    col_brand, col_title, col_user = st.columns([1, 1.2, 1.3], vertical_alignment="center")
    
    with col_brand:
        b_icon, b_text = st.columns([0.3, 2], vertical_alignment="center")
        with b_icon:
            if os.path.exists(logo_path):
                st.image(logo_path, width=32)
            else:
                st.image("https://i.ibb.co/YTYGn5qV/logo.png", width=32)
        with b_text:
            brand_html = """<div style="line-height: 1.1;">
<span style="font-size: 1.15rem; font-weight: 800; color: #172B4D;">SNAPCLASS</span>
</div>"""
            st.markdown(brand_html, unsafe_allow_html=True)

    with col_title:
        title_html = f"""<div style="font-size: 0.95rem; font-weight: 700; color: #40566F; border-left: 1.5px solid #D9DEE7; padding-left: 12px;">
{page_title}
</div>"""
        st.markdown(title_html, unsafe_allow_html=True)

    with col_user:
        user_disp = user_name if user_name else "Account"
        role_tag = role.upper() if role else "USER"
        user_html = f"""<div style="display: flex; align-items: center; justify-content: flex-end; gap: 10px;">
<div style="text-align: right; line-height: 1.2;">
<span style="font-size: 0.86rem; font-weight: 700; color: #172B4D;">{user_disp}</span>
<span style="display: block; font-size: 0.68rem; font-weight: 700; color: #667085;">{role_tag} &bull; <span style="color: #218739;">● AI ONLINE</span></span>
</div>
</div>"""
        st.markdown(user_html, unsafe_allow_html=True)

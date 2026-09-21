import streamlit as st
import textwrap
from src.utils.assets import get_asset_base64

def header_home():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    html = textwrap.dedent(f"""\
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 1rem; margin-bottom: 2rem; text-align: center;">
<div style="background: #FFFFFF; padding: 12px 18px; border-radius: 16px; border: 1px solid #E2E8F0; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
<img src="{logo_url}" style="height: 64px; width: auto;" alt="SnapClass Logo" />
</div>
<h1 style="color: #0F172A; font-size: 2.5rem; font-weight: 800; letter-spacing: -0.03em; margin: 0 0 0.5rem 0; line-height: 1.15;">
Snap<span style="color: #4F46E5;">Class</span>
</h1>
<p style="color: #475569; font-size: 1.05rem; font-weight: 500; margin: 0 0 1rem 0; max-width: 520px; line-height: 1.5;">
Automated smart attendance verification for modern classrooms and lecture halls.
</p>
<div style="display: flex; gap: 8px; flex-wrap: wrap; justify-content: center;">
<span style="background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">
Face Recognition
</span>
<span style="background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">
Voice Attendance
</span>
<span style="background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600;">
Instant QR Join
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


def header_dashboard():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    html = textwrap.dedent(f"""\
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.5rem;">
<div style="background: #FFFFFF; padding: 6px 10px; border-radius: 10px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.03); display: flex; align-items: center;">
<img src="{logo_url}" style="height: 38px; width: auto;" alt="SnapClass Logo" />
</div>
<div>
<h2 style="font-size: 1.45rem; font-weight: 800; line-height: 1.1; margin: 0; letter-spacing: -0.02em;">
<span style="color: #0F172A;">Snap</span><span style="color: #4F46E5;">Class</span>
</h2>
<span style="font-size: 0.76rem; font-weight: 600; color: #64748B; letter-spacing: 0.04em; text-transform: uppercase;">
Attendance Platform
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)

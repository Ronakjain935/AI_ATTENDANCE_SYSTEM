import streamlit as st
import textwrap
from src.utils.config import APP_LIVE_URL

def footer_home():
    html = textwrap.dedent(f"""\
<div style="margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid #CBD5E1; text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 8px;">
<span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #047857;"></span>
<span style="color: #475569; font-size: 0.82rem; font-weight: 600;">Official Deployment:</span>
<a href="{APP_LIVE_URL}" target="_blank" style="color: #1E3A8A; font-weight: 600; text-decoration: none; font-size: 0.82rem; border-bottom: 1px dashed #1E3A8A;">
{APP_LIVE_URL}
</a>
</div>
<p style="color: #64748B; font-size: 0.80rem; margin: 0;">
SnapClass Institutional Attendance Platform &bull; Encrypted & Verified Records
</p>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


def footer_dashboard():
    html = textwrap.dedent(f"""\
<div style="margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid #CBD5E1; text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #047857;"></span>
<span style="color: #64748B; font-size: 0.80rem; font-weight: 600;">Active Server:</span>
<a href="{APP_LIVE_URL}" target="_blank" style="color: #1E3A8A; font-weight: 600; text-decoration: none; font-size: 0.80rem;">
{APP_LIVE_URL}
</a>
</div>
<p style="color: #94A3B8; font-size: 0.76rem; margin: 0;">
SnapClass Platform &bull; Academic Year 2024–2025
</p>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)

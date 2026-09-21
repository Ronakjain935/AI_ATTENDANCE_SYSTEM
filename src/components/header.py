import streamlit as st
import textwrap
from src.utils.assets import get_asset_base64

def header_home():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    html = textwrap.dedent(f"""\
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 1rem; margin-bottom: 2.2rem; text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 8px; background: #FFFFFF; border: 1px solid #E2E8F0; padding: 5px 16px; border-radius: 999px; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04); margin-bottom: 1.25rem;">
<span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #10B981; box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);"></span>
<span style="font-size: 0.78rem; font-weight: 700; color: #4F46E5; text-transform: uppercase; letter-spacing: 0.06em;">SnapClass 2.5</span>
<span style="color: #CBD5E1; font-weight: 300;">|</span>
<span style="font-size: 0.82rem; font-weight: 500; color: #475569;">Next-Gen Biometric Attendance</span>
</div>

<div style="background: #FFFFFF; padding: 10px 18px; border-radius: 18px; border: 1px solid #E2E8F0; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1.25rem;">
<img src="{logo_url}" style="height: 60px; width: auto;" alt="SnapClass Logo" />
</div>

<h1 style="font-size: 2.85rem; font-weight: 800; color: #0F172A; line-height: 1.15; letter-spacing: -0.035em; margin: 0 0 0.85rem 0;">
Smart Attendance.<br>
<span style="background: linear-gradient(135deg, #4F46E5 0%, #6366F1 50%, #06B6D4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Zero Roll-Call Friction.</span>
</h1>

<p style="color: #64748B; font-size: 1.05rem; font-weight: 500; margin: 0 0 1.5rem 0; max-width: 580px; line-height: 1.55;">
Snap a single classroom photo or capture roll-call audio. Deep facial embeddings and acoustic voice models instantly mark attendance in seconds.
</p>

<div style="display: flex; gap: 8px; flex-wrap: wrap; justify-content: center;">
<span style="background: #FFFFFF; color: #334155; border: 1px solid #E2E8F0; padding: 5px 14px; border-radius: 999px; font-size: 0.8rem; font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">
⚡ &lt; 1s Scan Speed
</span>
<span style="background: #FFFFFF; color: #334155; border: 1px solid #E2E8F0; padding: 5px 14px; border-radius: 999px; font-size: 0.8rem; font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">
🎯 99.4% Face Accuracy
</span>
<span style="background: #FFFFFF; color: #334155; border: 1px solid #E2E8F0; padding: 5px 14px; border-radius: 999px; font-size: 0.8rem; font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">
🎙️ Voice Speaker AI
</span>
<span style="background: #FFFFFF; color: #334155; border: 1px solid #E2E8F0; padding: 5px 14px; border-radius: 999px; font-size: 0.8rem; font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">
📱 Instant QR Check-In
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


def header_dashboard():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    html = textwrap.dedent(f"""\
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.25rem;">
<div style="background: #FFFFFF; padding: 6px 10px; border-radius: 12px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px rgba(0,0,0,0.04); display: flex; align-items: center;">
<img src="{logo_url}" style="height: 38px; width: auto;" alt="SnapClass Logo" />
</div>
<div>
<div style="display: flex; align-items: center; gap: 6px;">
<h2 style="font-size: 1.45rem; font-weight: 800; line-height: 1.1; margin: 0; letter-spacing: -0.025em; color: #0F172A;">
Snap<span style="color: #4F46E5;">Class</span>
</h2>
<span style="font-size: 0.65rem; background: #EEF2FF; color: #4338CA; border: 1px solid #E0E7FF; padding: 1px 6px; border-radius: 4px; font-weight: 800; letter-spacing: 0.05em;">PRO</span>
</div>
<span style="font-size: 0.76rem; font-weight: 600; color: #64748B; letter-spacing: 0.04em; text-transform: uppercase;">
Institutional Attendance Platform
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)

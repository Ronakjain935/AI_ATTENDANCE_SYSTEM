import streamlit as st
import textwrap
from src.utils.assets import get_asset_base64

def header_home():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    html = textwrap.dedent(f"""\
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 0.8rem; margin-bottom: 2.2rem; text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 8px; background: #FFFFFF; border: 1px solid #CBD5E1; padding: 5px 16px; border-radius: 999px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04); margin-bottom: 1.25rem;">
<span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #047857; box-shadow: 0 0 0 2px rgba(4, 120, 87, 0.2);"></span>
<span style="font-size: 0.76rem; font-weight: 700; color: #1E3A8A; text-transform: uppercase; letter-spacing: 0.08em;">SnapClass Institutional</span>
<span style="color: #CBD5E1; font-weight: 300;">|</span>
<span style="font-size: 0.80rem; font-weight: 500; color: #475569;">Biometric & Acoustic Roll-Call</span>
</div>

<div style="background: #FFFFFF; padding: 12px 20px; border-radius: 14px; border: 1px solid #CBD5E1; box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04); display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1.25rem;">
<img src="{logo_url}" style="height: 56px; width: auto;" alt="SnapClass Logo" />
</div>

<h1 style="font-size: 2.85rem; font-weight: 700; color: #0F172A; line-height: 1.18; letter-spacing: -0.02em; margin: 0 0 0.85rem 0; font-family: 'Lora', Georgia, serif;">
Smart Attendance.<br>
<span style="color: #1E3A8A;">Zero Roll-Call Friction.</span>
</h1>

<p style="color: #475569; font-size: 1.05rem; font-weight: 400; margin: 0 0 1.6rem 0; max-width: 600px; line-height: 1.6;">
Elevate your academic workflow. Snap a high-density classroom photo or record roll-call audio to instantly identify and log student presence with institutional precision.
</p>

<div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
<span style="background: #FFFFFF; color: #1E293B; border: 1px solid #CBD5E1; padding: 5px 14px; border-radius: 6px; font-size: 0.80rem; font-weight: 600; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);">
⚡ Instant Sub-Second Scan
</span>
<span style="background: #FFFFFF; color: #1E293B; border: 1px solid #CBD5E1; padding: 5px 14px; border-radius: 6px; font-size: 0.80rem; font-weight: 600; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);">
🎯 99.4% Multi-Face Biometrics
</span>
<span style="background: #FFFFFF; color: #1E293B; border: 1px solid #CBD5E1; padding: 5px 14px; border-radius: 6px; font-size: 0.80rem; font-weight: 600; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);">
🎙️ Acoustic Voice Speaker AI
</span>
<span style="background: #FFFFFF; color: #1E293B; border: 1px solid #CBD5E1; padding: 5px 14px; border-radius: 6px; font-size: 0.80rem; font-weight: 600; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);">
📱 Official QR / PIN Check-In
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


def header_dashboard():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    html = textwrap.dedent(f"""\
<div style="display: flex; align-items: center; gap: 14px; margin-bottom: 0.4rem;">
<div style="background: #FFFFFF; padding: 6px 10px; border-radius: 10px; border: 1px solid #CBD5E1; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04); display: flex; align-items: center;">
<img src="{logo_url}" style="height: 38px; width: auto;" alt="SnapClass Logo" />
</div>
<div>
<div style="display: flex; align-items: center; gap: 8px;">
<h2 style="font-size: 1.48rem; font-weight: 700; line-height: 1.1; margin: 0; font-family: 'Lora', Georgia, serif; color: #0F172A; letter-spacing: -0.01em;">
Snap<span style="color: #1E3A8A;">Class</span>
</h2>
<span style="font-size: 0.65rem; background: #0F172A; color: #F8FAFC; border: 1px solid #1E293B; padding: 2px 7px; border-radius: 4px; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase;">
EDITION
</span>
</div>
<span style="font-size: 0.74rem; font-weight: 600; color: #64748B; letter-spacing: 0.05em; text-transform: uppercase;">
Institutional Attendance System
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


import streamlit as st
import textwrap
from src.utils.assets import get_asset_base64
from src.ui.base_layout import get_current_theme

def header_home():
    theme = get_current_theme()
    is_dark = (theme == "dark")

    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"

    badge_bg = "#1E293B" if is_dark else "#FFFFFF"
    badge_border = "#334155" if is_dark else "#CBD5E1"
    badge_text = "#38BDF8" if is_dark else "#1E3A8A"
    sub_text = "#94A3B8" if is_dark else "#475569"
    pill_bg = "#1E293B" if is_dark else "#FFFFFF"
    pill_border = "#334155" if is_dark else "#CBD5E1"
    pill_text = "#F8FAFC" if is_dark else "#0F172A"
    title_color = "#FFFFFF" if is_dark else "#0F172A"
    accent_color = "#38BDF8" if is_dark else "#2563EB"

    html = textwrap.dedent(f"""\
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 0.5rem; margin-bottom: 2rem; text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 8px; background: {badge_bg}; border: 1.5px solid {badge_border}; padding: 6px 18px; border-radius: 999px; margin-bottom: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,0.08);">
<span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #10B981;"></span>
<span style="font-size: 0.78rem; font-weight: 800; color: {badge_text}; text-transform: uppercase; letter-spacing: 0.08em;">SnapClass Platform</span>
<span style="color: {badge_border}; font-weight: 300;">|</span>
<span style="font-size: 0.82rem; font-weight: 600; color: {sub_text};">Biometric & Acoustic Roll-Call</span>
</div>

<div style="background: {badge_bg}; padding: 12px 20px; border-radius: 14px; border: 1.5px solid {badge_border}; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1.25rem; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
<img src="{logo_url}" style="height: 56px; width: auto;" alt="SnapClass Logo" />
</div>

<h1 style="font-size: 2.75rem; font-weight: 800; color: {title_color}; line-height: 1.15; letter-spacing: -0.02em; margin: 0 0 0.85rem 0;">
Smart Attendance.<br>
<span style="color: {accent_color};">Zero Roll-Call Friction.</span>
</h1>

<p style="color: {sub_text}; font-size: 1.05rem; font-weight: 500; margin: 0 0 1.5rem 0; max-width: 600px; line-height: 1.55;">
Automate classroom attendance with deep facial embeddings and acoustic voice models in seconds.
</p>

<div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: center;">
<span style="background: {pill_bg}; color: {pill_text}; border: 1.5px solid {pill_border}; padding: 6px 14px; border-radius: 8px; font-size: 0.84rem; font-weight: 700;">
⚡ Instant Sub-Second Scan
</span>
<span style="background: {pill_bg}; color: {pill_text}; border: 1.5px solid {pill_border}; padding: 6px 14px; border-radius: 8px; font-size: 0.84rem; font-weight: 700;">
🎯 99.4% Multi-Face Biometrics
</span>
<span style="background: {pill_bg}; color: {pill_text}; border: 1.5px solid {pill_border}; padding: 6px 14px; border-radius: 8px; font-size: 0.84rem; font-weight: 700;">
🎙️ Acoustic Voice Speaker AI
</span>
<span style="background: {pill_bg}; color: {pill_text}; border: 1.5px solid {pill_border}; padding: 6px 14px; border-radius: 8px; font-size: 0.84rem; font-weight: 700;">
📱 Official QR / PIN Check-In
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


def header_dashboard():
    theme = get_current_theme()
    is_dark = (theme == "dark")

    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"

    card_bg = "#1E293B" if is_dark else "#FFFFFF"
    card_border = "#334155" if is_dark else "#CBD5E1"
    title_color = "#FFFFFF" if is_dark else "#0F172A"
    accent_color = "#38BDF8" if is_dark else "#2563EB"
    sub_color = "#94A3B8" if is_dark else "#475569"

    html = textwrap.dedent(f"""\
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.3rem;">
<div style="background: {card_bg}; padding: 6px 10px; border-radius: 10px; border: 1.5px solid {card_border}; display: flex; align-items: center;">
<img src="{logo_url}" style="height: 38px; width: auto;" alt="SnapClass Logo" />
</div>
<div>
<div style="display: flex; align-items: center; gap: 8px;">
<h2 style="font-size: 1.48rem; font-weight: 800; line-height: 1.1; margin: 0; color: {title_color}; letter-spacing: -0.01em;">
Snap<span style="color: {accent_color};">Class</span>
</h2>
<span style="font-size: 0.68rem; background: {'#2563EB' if is_dark else '#0F172A'}; color: #FFFFFF; padding: 2px 7px; border-radius: 4px; font-weight: 800; letter-spacing: 0.05em; text-transform: uppercase;">
EDITION
</span>
</div>
<span style="font-size: 0.74rem; font-weight: 700; color: {sub_color}; letter-spacing: 0.04em; text-transform: uppercase;">
Institutional Attendance System
</span>
</div>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)

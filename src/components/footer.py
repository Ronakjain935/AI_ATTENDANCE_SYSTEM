import streamlit as st
import textwrap
from src.utils.config import APP_LIVE_URL
from src.ui.base_layout import get_current_theme

def footer_home():
    theme = get_current_theme()
    is_dark = (theme == "dark")
    border_col = "#334155" if is_dark else "#CBD5E1"
    sub_text = "#94A3B8" if is_dark else "#475569"
    link_color = "#38BDF8" if is_dark else "#2563EB"

    html = textwrap.dedent(f"""\
<div style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1.5px solid {border_col}; text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 6px;">
<span style="display: inline-block; width: 7px; height: 7px; border-radius: 50%; background: #10B981;"></span>
<span style="color: {sub_text}; font-size: 0.82rem; font-weight: 700;">Live Deployment:</span>
<a href="{APP_LIVE_URL}" target="_blank" style="color: {link_color}; font-weight: 700; text-decoration: underline; font-size: 0.82rem;">
{APP_LIVE_URL}
</a>
</div>
<p style="color: {sub_text}; font-size: 0.80rem; margin: 0; font-weight: 500;">
SnapClass Platform &bull; Encrypted Institutional Attendance
</p>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


def footer_dashboard():
    theme = get_current_theme()
    is_dark = (theme == "dark")
    border_col = "#334155" if is_dark else "#CBD5E1"
    sub_text = "#94A3B8" if is_dark else "#475569"
    link_color = "#38BDF8" if is_dark else "#2563EB"

    html = textwrap.dedent(f"""\
<div style="margin-top: 2.5rem; padding-top: 1.2rem; border-top: 1.5px solid {border_col}; text-align: center;">
<div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 4px;">
<span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: #10B981;"></span>
<span style="color: {sub_text}; font-size: 0.80rem; font-weight: 700;">Live Host:</span>
<a href="{APP_LIVE_URL}" target="_blank" style="color: {link_color}; font-weight: 700; text-decoration: underline; font-size: 0.80rem;">
{APP_LIVE_URL}
</a>
</div>
<p style="color: {sub_text}; font-size: 0.76rem; margin: 0;">
SnapClass Institutional System
</p>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)

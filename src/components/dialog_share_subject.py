import streamlit as st
import segno
import io
import urllib.parse
import textwrap
from src.utils.config import APP_LIVE_URL
from src.ui.base_layout import get_current_theme

@st.dialog("Share Course")
def share_subject_dialog(subject_name, subject_code):
    theme = get_current_theme()
    is_dark = (theme == "dark")

    banner_bg = "#1E293B" if is_dark else "#F1F5F9"
    banner_border = "#475569" if is_dark else "#CBD5E1"
    banner_text = "#F8FAFC" if is_dark else "#0F172A"
    code_bg = "#0B0F19" if is_dark else "#0F172A"
    code_text = "#38BDF8" if is_dark else "#FFFFFF"
    card_bg = "#0F172A" if is_dark else "#F8FAFC"
    card_border = "#334155" if is_dark else "#CBD5E1"
    sub_text = "#94A3B8" if is_dark else "#475569"

    join_url = f"{APP_LIVE_URL}/?join-code={subject_code}"

    # Generate high quality QR code PNG with clean border
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=12, border=2, light='#FFFFFF', dark='#000000')
    qr_bytes = out.getvalue()

    # Share message formatting
    wa_msg = f"Join {subject_name} on SnapClass!\n\nCourse Code: {subject_code}\nClick to join directly: {join_url}"
    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_msg)}"

    email_sub = f"Course Enrollment: {subject_name} ({subject_code}) on SnapClass"
    email_body = f"Hello,\n\nYou are invited to join {subject_name} on SnapClass.\n\nCourse Code: {subject_code}\nDirect Enrollment Link:\n{join_url}\n\nBest regards,\nSnapClass Platform"
    email_url = f"mailto:?subject={urllib.parse.quote(email_sub)}&body={urllib.parse.quote(email_body)}"

    # Subject Details Banner (High Contrast)
    banner_html = textwrap.dedent(f"""\
<div style="background-color: {banner_bg}; padding: 14px 18px; border-radius: 10px; border: 1.5px solid {banner_border}; margin-bottom: 1rem;">
<div style="display: inline-block; background-color: {code_bg}; color: {code_text} !important; padding: 3px 10px; border-radius: 4px; font-weight: 800; font-size: 0.82rem; font-family: monospace; letter-spacing: 0.05em;">
CODE: {subject_code}
</div>
<h3 style="color: {banner_text}; margin: 8px 0 0 0; font-size: 1.25rem; font-weight: 800;">
{subject_name}
</h3>
</div>\
""")
    st.markdown(banner_html, unsafe_allow_html=True)

    col1, col2 = st.columns([1.15, 0.85], gap="medium")

    with col1:
        st.markdown(f"<p style='color: {banner_text}; margin-bottom: 6px; font-size: 0.86rem; font-weight: 700; text-transform: uppercase;'>Official Enrollment Link</p>", unsafe_allow_html=True)
        
        # High contrast full-width link box
        link_box_html = textwrap.dedent(f"""\
<div style="background: {card_bg}; border: 1.5px solid {card_border}; border-radius: 8px; padding: 10px 12px; margin-bottom: 14px; word-break: break-all; font-family: monospace; font-size: 0.85rem; font-weight: 600; color: {'#38BDF8' if is_dark else '#1E3A8A'}; user-select: all;">
{join_url}
</div>\
""")
        st.markdown(link_box_html, unsafe_allow_html=True)

        st.markdown(f"<p style='color: {banner_text}; margin-bottom: 8px; font-size: 0.86rem; font-weight: 700; text-transform: uppercase;'>Instant Dispatch</p>", unsafe_allow_html=True)
        
        # Guaranteed bright white text for WhatsApp and Email buttons
        share_links_html = textwrap.dedent(f"""\
<div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 12px;">
<a href="{wa_url}" target="_blank" style="background-color: #16A34A !important; padding: 11px 16px; border-radius: 8px; text-align: center; display: block; text-decoration: none !important; box-shadow: 0 1px 3px rgba(0,0,0,0.2);">
<span style="color: #FFFFFF !important; font-weight: 800; font-size: 0.92rem; text-decoration: none !important;">💬 Share via WhatsApp</span>
</a>
<a href="{email_url}" target="_blank" style="background-color: #2563EB !important; padding: 11px 16px; border-radius: 8px; text-align: center; display: block; text-decoration: none !important; box-shadow: 0 1px 3px rgba(0,0,0,0.2);">
<span style="color: #FFFFFF !important; font-weight: 800; font-size: 0.92rem; text-decoration: none !important;">✉️ Share via Official Email</span>
</a>
</div>\
""")
        st.markdown(share_links_html, unsafe_allow_html=True)

    with col2:
        st.markdown(f"<p style='color: {banner_text}; margin-bottom: 6px; font-size: 0.86rem; font-weight: 700; text-align: center; text-transform: uppercase;'>Classroom QR</p>", unsafe_allow_html=True)
        st.image(qr_bytes, use_container_width=True)
        
        st.download_button(
            label="Download QR",
            data=qr_bytes,
            file_name=f"SnapClass_QR_{subject_code}.png",
            mime="image/png",
            use_container_width=True,
            type="secondary"
        )

    info_html = textwrap.dedent(f"""\
<div style="background-color: {card_bg}; border: 1px solid {card_border}; border-left: 4px solid #2563EB; padding: 10px 14px; border-radius: 8px; margin-top: 10px; font-size: 0.84rem; color: {sub_text};">
Students scanning this QR code or opening the link will be automatically directed to <strong>{subject_name}</strong>.
</div>\
""")
    st.markdown(info_html, unsafe_allow_html=True)

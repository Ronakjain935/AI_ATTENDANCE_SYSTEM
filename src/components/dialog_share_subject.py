import streamlit as st
import segno
import io
import urllib.parse
import textwrap
from src.utils.config import APP_LIVE_URL

@st.dialog("Share Course")
def share_subject_dialog(subject_name, subject_code):
    join_url = f"{APP_LIVE_URL}/?join-code={subject_code}"

    # Generate high quality QR code PNG with clean border
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=12, border=2, light='#FFFFFF', dark='#0F172A')
    qr_bytes = out.getvalue()

    # Share message formatting
    wa_msg = f"Join {subject_name} on SnapClass!\n\nSubject Code: {subject_code}\nClick to join directly: {join_url}"
    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_msg)}"

    email_sub = f"Enrollment Invitation: {subject_name} ({subject_code}) on SnapClass"
    email_body = f"Hello,\n\nYou are invited to join {subject_name} on SnapClass.\n\nSubject Code: {subject_code}\nDirect Enrollment Link:\n{join_url}\n\nBest regards,\nSnapClass Institutional Platform"
    email_url = f"mailto:?subject={urllib.parse.quote(email_sub)}&body={urllib.parse.quote(email_body)}"

    # Classic Subject Details Banner
    banner_html = textwrap.dedent(f"""\
<div style="background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%); padding: 16px 18px; border-radius: 12px; border: 1px solid #CBD5E1; border-left: 4px solid #1E3A8A; margin-bottom: 1.15rem; box-shadow: 0 1px 3px rgba(0,0,0,0.03);">
<div style="display: inline-block; background-color: #0F172A; color: #F8FAFC; border: 1px solid #1E293B; padding: 2px 10px; border-radius: 4px; font-weight: 700; font-size: 0.76rem; letter-spacing: 0.05em; font-family: monospace;">
CODE: {subject_code}
</div>
<h3 style="color: #0F172A; margin: 8px 0 0 0; font-size: 1.22rem; font-weight: 700; font-family: 'Lora', Georgia, serif; letter-spacing: -0.01em;">
{subject_name}
</h3>
</div>\
""")
    st.markdown(banner_html, unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 0.9], gap="medium")

    with col1:
        st.markdown("<p style='color: #475569; margin-bottom: 4px; font-size: 0.84rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em;'>Official Enrollment URL</p>", unsafe_allow_html=True)
        st.code(join_url, language=None)
        
        st.markdown("<p style='color: #475569; margin-top: 12px; margin-bottom: 8px; font-size: 0.84rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em;'>Instant Dispatch</p>", unsafe_allow_html=True)
        
        share_links_html = textwrap.dedent(f"""\
<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 10px;">
<a href="{wa_url}" target="_blank" style="background: linear-gradient(180deg, #15803D 0%, #166534 100%); color: #FFFFFF !important; text-decoration: none; padding: 9px 14px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; text-align: center; display: block; border: 1px solid #14532D; box-shadow: 0 1px 2px rgba(0,0,0,0.08);">
💬 Share via WhatsApp
</a>
<a href="{email_url}" target="_blank" style="background: linear-gradient(180deg, #1E3A8A 0%, #1E293B 100%); color: #FFFFFF !important; text-decoration: none; padding: 9px 14px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; text-align: center; display: block; border: 1px solid #0F172A; box-shadow: 0 1px 2px rgba(0,0,0,0.08);">
✉️ Share via Official Email
</a>
</div>\
""")
        st.markdown(share_links_html, unsafe_allow_html=True)

    with col2:
        st.markdown("<p style='color: #475569; margin-bottom: 4px; font-size: 0.84rem; font-weight: 600; text-align: center; text-transform: uppercase; letter-spacing: 0.04em;'>Classroom QR Code</p>", unsafe_allow_html=True)
        st.image(qr_bytes, use_container_width=True)
        
        st.download_button(
            label="Download QR Badge",
            data=qr_bytes,
            file_name=f"SnapClass_QR_{subject_code}.png",
            mime="image/png",
            use_container_width=True,
            type="secondary"
        )

    info_html = textwrap.dedent(f"""\
<div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; border-left: 3px solid #1E3A8A; padding: 10px 14px; border-radius: 8px; margin-top: 14px; font-size: 0.82rem; color: #475569;">
Students scanning this QR code or opening the link will be automatically directed to <strong>{subject_name}</strong> on <code>{APP_LIVE_URL}</code>.
</div>\
""")
    st.markdown(info_html, unsafe_allow_html=True)


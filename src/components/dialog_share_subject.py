import streamlit as st
import segno
import io
import urllib.parse
from src.utils.config import APP_LIVE_URL

@st.dialog("Share Course")
def share_subject_dialog(subject_name, subject_code):
    join_url = f"{APP_LIVE_URL}/?join-code={subject_code}"

    # Generate crisp QR code
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=2, light='#FFFFFF', dark='#000000')
    qr_bytes = out.getvalue()

    wa_msg = f"Join {subject_name} on SnapClass!\n\nCourse Code: {subject_code}\nClick to join directly: {join_url}"
    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_msg)}"

    email_sub = f"Course Enrollment: {subject_name} ({subject_code}) on SnapClass"
    email_body = f"Hello,\n\nYou are invited to join {subject_name} on SnapClass.\n\nCourse Code: {subject_code}\nDirect Enrollment Link:\n{join_url}\n\nBest regards,\nSnapClass Platform"
    email_url = f"mailto:?subject={urllib.parse.quote(email_sub)}&body={urllib.parse.quote(email_body)}"

    # Subject details banner
    banner_html = f"""<div style="background-color: #F7F6F2; padding: 12px 16px; border-radius: 8px; border: 1px solid #D9DEE7; margin-bottom: 1rem;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
<span style="background-color: #172B4D; color: #FFFFFF; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.78rem; font-family: monospace;">
CODE: {subject_code}
</span>
</div>
<h3 style="color: #172B4D; margin: 0; font-size: 1.2rem; font-weight: 700;">{subject_name}</h3>
</div>"""
    st.markdown(banner_html, unsafe_allow_html=True)

    col1, col2 = st.columns([1.15, 0.85], gap="medium")

    with col1:
        st.markdown("<p style='color: #172B4D; margin-bottom: 4px; font-size: 0.82rem; font-weight: 700; text-transform: uppercase;'>Enrollment Link</p>", unsafe_allow_html=True)
        
        link_box_html = f"""<div style="background: #FFFFFF; border: 1px solid #D9DEE7; border-radius: 8px; padding: 8px 10px; margin-bottom: 12px; word-break: break-all; font-family: monospace; font-size: 0.82rem; font-weight: 600; color: #2F6FED; user-select: all;">
{join_url}
</div>"""
        st.markdown(link_box_html, unsafe_allow_html=True)

        st.markdown("<p style='color: #172B4D; margin-bottom: 6px; font-size: 0.82rem; font-weight: 700; text-transform: uppercase;'>Instant Dispatch</p>", unsafe_allow_html=True)
        
        share_links_html = f"""<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 12px;">
<a href="{wa_url}" target="_blank" style="background-color: #218739 !important; padding: 10px 14px; border-radius: 8px; text-align: center; display: block; text-decoration: none !important; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
<span style="color: #FFFFFF !important; font-weight: 600; font-size: 0.88rem;">💬 Share via WhatsApp</span>
</a>
<a href="{email_url}" target="_blank" style="background-color: #2F6FED !important; padding: 10px 14px; border-radius: 8px; text-align: center; display: block; text-decoration: none !important; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
<span style="color: #FFFFFF !important; font-weight: 600; font-size: 0.88rem;">✉️ Share via Email</span>
</a>
</div>"""
        st.markdown(share_links_html, unsafe_allow_html=True)

    with col2:
        st.markdown("<p style='color: #172B4D; margin-bottom: 4px; font-size: 0.82rem; font-weight: 700; text-align: center; text-transform: uppercase;'>QR Code</p>", unsafe_allow_html=True)
        st.image(qr_bytes, use_container_width=True)
        
        st.download_button(
            label="Download QR",
            data=qr_bytes,
            file_name=f"SnapClass_QR_{subject_code}.png",
            mime="image/png",
            use_container_width=True,
            type="secondary"
        )

    info_html = f"""<div style="background-color: #F7F6F2; border: 1px solid #D9DEE7; border-left: 3px solid #172B4D; padding: 8px 12px; border-radius: 6px; margin-top: 8px; font-size: 0.80rem; color: #667085;">
Students scanning this QR code will be redirected directly to enroll in <strong>{subject_name}</strong>.
</div>"""
    st.markdown(info_html, unsafe_allow_html=True)

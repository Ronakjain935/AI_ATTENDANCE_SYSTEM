import streamlit as st
import segno
import io
import urllib.parse
import textwrap

@st.dialog("Share Course")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "aiattendancesystemgit-h.streamlit.app"
    join_url = f"https://{app_domain}/?join-code={subject_code}"

    # Generate high quality QR code PNG
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=12, border=2, light='#FFFFFF', dark='#000000')
    qr_bytes = out.getvalue()

    # Share message formatting
    wa_msg = f"Join {subject_name} on SnapClass!\n\nSubject Code: {subject_code}\nClick to join directly: {join_url}"
    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_msg)}"

    email_sub = f"Join {subject_name} ({subject_code}) on SnapClass"
    email_body = f"Hello,\n\nYou are invited to join {subject_name} on SnapClass.\n\nSubject Code: {subject_code}\nClick the link below to enroll:\n{join_url}\n\nBest regards,"
    email_url = f"mailto:?subject={urllib.parse.quote(email_sub)}&body={urllib.parse.quote(email_body)}"

    # Subject Details Banner
    banner_html = textwrap.dedent(f"""\
<div style="background-color: #F8FAFC; padding: 14px 16px; border-radius: 10px; border: 1px solid #E2E8F0; margin-bottom: 1rem;">
<div style="display: inline-block; background-color: #EEF2FF; color: #4338CA; border: 1px solid #E0E7FF; padding: 2px 8px; border-radius: 6px; font-weight: 700; font-size: 0.78rem;">
Code: {subject_code}
</div>
<h3 style="color: #0F172A; margin: 6px 0 0 0; font-size: 1.15rem; font-weight: 700;">
{subject_name}
</h3>
</div>\
""")
    st.markdown(banner_html, unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 0.9], gap="medium")

    with col1:
        st.markdown("<p style='color: #334155; margin-bottom: 4px; font-size: 0.88rem; font-weight: 600;'>Direct Course Link</p>", unsafe_allow_html=True)
        st.code(join_url, language=None)
        
        st.markdown("<p style='color: #334155; margin-top: 10px; margin-bottom: 8px; font-size: 0.88rem; font-weight: 600;'>Quick Share</p>", unsafe_allow_html=True)
        
        share_links_html = textwrap.dedent(f"""\
<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 10px;">
<a href="{wa_url}" target="_blank" style="background-color: #25D366; color: #FFFFFF !important; text-decoration: none; padding: 9px 14px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; text-align: center; display: block; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
Share via WhatsApp
</a>
<a href="{email_url}" target="_blank" style="background-color: #4F46E5; color: #FFFFFF !important; text-decoration: none; padding: 9px 14px; border-radius: 8px; font-weight: 600; font-size: 0.88rem; text-align: center; display: block; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
Share via Email
</a>
</div>\
""")
        st.markdown(share_links_html, unsafe_allow_html=True)

    with col2:
        st.markdown("<p style='color: #334155; margin-bottom: 4px; font-size: 0.88rem; font-weight: 600; text-align: center;'>QR Code</p>", unsafe_allow_html=True)
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
<div style="background-color: #F8FAFC; border: 1px solid #E2E8F0; border-left: 3px solid #4F46E5; padding: 10px 14px; border-radius: 8px; margin-top: 12px; font-size: 0.84rem; color: #334155;">
Students scanning this QR code or following the link will be automatically prompted to enroll in <strong>{subject_name}</strong>.
</div>\
""")
    st.markdown(info_html, unsafe_allow_html=True)

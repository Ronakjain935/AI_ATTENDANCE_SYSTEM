import streamlit as st
import segno
import io
import urllib.parse

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "snapclass-main.streamlit.app"
    join_url = f"https://{app_domain}/?join-code={subject_code}"

    # Generate high quality QR code PNG
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=12, border=2, light='#FFFFFF', dark='#000000')
    qr_bytes = out.getvalue()

    # Share message formatting
    wa_msg = f"📚 *Join {subject_name} on SnapClass!*\n\nSubject Code: *{subject_code}*\nClick this link to join instantly:\n👉 {join_url}"
    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_msg)}"

    email_sub = f"Join {subject_name} ({subject_code}) on SnapClass"
    email_body = f"Hello,\n\nYou are invited to join {subject_name} on SnapClass.\n\nSubject Code: {subject_code}\nClick the link below to enroll:\n{join_url}\n\nBest regards,"
    email_url = f"mailto:?subject={urllib.parse.quote(email_sub)}&body={urllib.parse.quote(email_body)}"

    # Subject Details Banner
    st.markdown(f"""
        <div style="background-color: #f8fafc; padding: 14px 18px; border-radius: 16px; border: 1px solid #e2e8f0; margin-bottom: 1.2rem;">
            <span style="background-color: #5865F2; color: #ffffff; padding: 4px 10px; border-radius: 8px; font-weight: 700; font-size: 0.85rem;">
                Code: {subject_code}
            </span>
            <h3 style="color: #0f172a !important; margin: 8px 0 0 0; font-size: 1.3rem; font-weight: 800;">
                {subject_name}
            </h3>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 0.9], gap="medium")

    with col1:
        st.markdown("<h4 style='color: #0f172a !important; margin-bottom: 6px; font-size: 1rem; font-weight: 700;'>🔗 Direct Class Link</h4>", unsafe_allow_html=True)
        st.code(join_url, language=None)
        
        st.markdown("<h4 style='color: #0f172a !important; margin-top: 14px; margin-bottom: 8px; font-size: 1rem; font-weight: 700;'>⚡ Quick Share</h4>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 10px;">
                <a href="{wa_url}" target="_blank" style="background-color: #25D366; color: #ffffff !important; text-decoration: none; padding: 11px 16px; border-radius: 12px; font-weight: 700; font-size: 0.95rem; text-align: center; display: block; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.25);">
                    📱 Share on WhatsApp
                </a>
                <a href="{email_url}" target="_blank" style="background-color: #5865F2; color: #ffffff !important; text-decoration: none; padding: 11px 16px; border-radius: 12px; font-weight: 700; font-size: 0.95rem; text-align: center; display: block; box-shadow: 0 4px 12px rgba(88, 101, 242, 0.25);">
                    ✉️ Share via Email
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<h4 style='color: #0f172a !important; margin-bottom: 6px; font-size: 1rem; font-weight: 700; text-align: center;'>📷 Scan QR Code</h4>", unsafe_allow_html=True)
        
        st.image(qr_bytes, use_container_width=True, caption="Scan using phone camera to join")
        
        st.download_button(
            label="📥 Download QR Code",
            data=qr_bytes,
            file_name=f"SnapClass_QR_{subject_code}.png",
            mime="image/png",
            use_container_width=True,
            type="secondary"
        )

    st.markdown(f"""
        <div style="background-color: #E0E3FF; border-left: 4px solid #5865F2; padding: 10px 14px; border-radius: 8px; margin-top: 14px; font-size: 0.88rem; color: #0f172a;">
            💡 <strong>How it works:</strong> Students scanning this QR code or clicking the link will be automatically prompted to enroll in <strong>{subject_name}</strong>!
        </div>
    """, unsafe_allow_html=True)

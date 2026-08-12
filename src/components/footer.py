import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top: 3.5rem; display: flex; flex-direction: column; align-items: center; gap: 8px;">
            <div style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.16); padding: 8px 24px; border-radius: 9999px; backdrop-filter: blur(12px); box-shadow: 0 6px 20px rgba(0,0,0,0.2); display: flex; align-items: center; gap: 12px;">
                <span style="font-weight: 800; color: #818CF8; font-size: 0.85rem; letter-spacing: 0.06em; text-transform: uppercase;">⚡ SnapClass AI v2.0</span>
                <span style="color: rgba(255,255,255,0.3);">•</span>
                <span style="font-weight: 600; color: #E2E8F0; font-size: 0.88rem;">Automated Smart Attendance Platform</span>
            </div>
            <p style="color: #94A3B8; font-size: 0.8rem; font-weight: 500; margin: 4px 0 0 0;">
                🔒 Powered by Deep Facial & Speaker Recognition AI
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top: 3.5rem; display: flex; flex-direction: column; align-items: center; gap: 8px;">
            <div style="background: #FFFFFF; border: 1px solid rgba(99, 102, 241, 0.18); padding: 8px 24px; border-radius: 9999px; box-shadow: 0 6px 18px rgba(79, 70, 229, 0.08); display: flex; align-items: center; gap: 12px;">
                <span style="font-weight: 800; color: #4F46E5; font-size: 0.85rem; letter-spacing: 0.06em; text-transform: uppercase;">⚡ SnapClass AI</span>
                <span style="color: #CBD5E1;">•</span>
                <span style="font-weight: 600; color: #334155; font-size: 0.88rem;">Automated Smart Attendance Platform</span>
            </div>
            <p style="color: #64748B; font-size: 0.8rem; font-weight: 500; margin: 4px 0 0 0;">
                🔒 Encrypted & Verified Attendance Verification
            </p>
        </div>
    """, unsafe_allow_html=True)

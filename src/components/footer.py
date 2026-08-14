import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top: 4rem; display: flex; flex-direction: column; align-items: center; gap: 10px;">
            <div style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.18); padding: 10px 28px; border-radius: 9999px; backdrop-filter: blur(14px); box-shadow: 0 8px 24px rgba(0,0,0,0.25); display: flex; align-items: center; gap: 14px; flex-wrap: wrap; justify-content: center;">
                <span style="font-weight: 800; background: linear-gradient(135deg, #818CF8, #C084FC); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 0.88rem; letter-spacing: 0.08em; text-transform: uppercase;">⚡ SnapClass AI v2.5</span>
                <span style="color: rgba(255,255,255,0.3);">•</span>
                <span style="font-weight: 600; color: #F1F5F9; font-size: 0.9rem;">Automated Smart Attendance Platform</span>
            </div>
            <p style="color: #A5B4FC; font-size: 0.82rem; font-weight: 500; margin: 4px 0 0 0; text-align: center;">
                🔒 Powered by Deep Facial & Speaker Recognition AI • Built with ⚡ by Ronak Jain
            </p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top: 4rem; display: flex; flex-direction: column; align-items: center; gap: 10px;">
            <div style="background: #FFFFFF; border: 1px solid rgba(99, 102, 241, 0.2); padding: 10px 28px; border-radius: 9999px; box-shadow: 0 8px 20px rgba(79, 70, 229, 0.08); display: flex; align-items: center; gap: 14px; flex-wrap: wrap; justify-content: center;">
                <span style="font-weight: 800; color: #4F46E5; font-size: 0.88rem; letter-spacing: 0.08em; text-transform: uppercase;">⚡ SnapClass AI</span>
                <span style="color: #CBD5E1;">•</span>
                <span style="font-weight: 600; color: #334155; font-size: 0.9rem;">Automated Smart Attendance Platform</span>
            </div>
            <p style="color: #64748B; font-size: 0.82rem; font-weight: 500; margin: 4px 0 0 0; text-align: center;">
                🔒 Encrypted & Verified Attendance Verification • Built with ⚡ by Ronak Jain
            </p>
        </div>
    """, unsafe_allow_html=True)

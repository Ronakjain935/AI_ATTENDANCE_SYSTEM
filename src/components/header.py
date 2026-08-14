import streamlit as st
from src.utils.assets import get_asset_base64

def header_home():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom: 2.5rem; margin-top: 1rem;">
            <div style="background: rgba(255, 255, 255, 0.1); padding: 18px 24px; border-radius: 32px; backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.22); box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), 0 0 30px rgba(99, 102, 241, 0.2); display: flex; align-items: center; justify-content: center;">
                <img src='{logo_url}' style='height: 110px; width: auto; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.3));' alt='SnapClass Logo' />
            </div>
            <h1 style='text-align: center; color: #FFFFFF; font-size: 3.6rem; font-weight: 800; letter-spacing: -0.03em; margin-top: 18px; line-height: 1.05; text-shadow: 0 4px 20px rgba(0,0,0,0.3);'>
                SNAP<span style="background: linear-gradient(135deg, #818CF8 0%, #C084FC 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">CLASS</span>
            </h1>
            <div style="margin-top: 10px; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(165, 180, 252, 0.3); padding: 6px 18px; border-radius: 9999px; backdrop-filter: blur(8px);">
                <span style="color: #E0E7FF; font-size: 1.05rem; font-weight: 700; letter-spacing: 0.03em;">
                    ✨ AI-Powered Automated Classroom Attendance
                </span>
            </div>
        </div>   
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_b64 = get_asset_base64("logo.png")
    logo_url = logo_b64 if logo_b64 else "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; gap: 16px; margin-bottom: 0.5rem;">
            <div style="background: #FFFFFF; padding: 10px; border-radius: 22px; border: 1px solid rgba(99, 102, 241, 0.2); box-shadow: 0 6px 20px rgba(99, 102, 241, 0.15);">
                <img src='{logo_url}' style='height: 56px; width: auto;' alt='SnapClass Logo' />
            </div>
            <div>
                <h2 style='text-align:left; font-size: 2rem; font-weight: 800; line-height: 1.0; margin: 0; letter-spacing: -0.02em;'>
                    <span style="color: #4F46E5;">SNAP</span><span style="color: #10B981;">CLASS</span>
                </h2>
                <span style="font-size: 0.8rem; font-weight: 700; color: #64748B; letter-spacing: 0.08em; text-transform: uppercase;">Smart AI Attendance Platform</span>
            </div>
        </div>   
    """, unsafe_allow_html=True)

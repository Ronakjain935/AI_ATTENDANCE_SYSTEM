import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom: 2.2rem; margin-top: 1rem;">
            <div style="background: rgba(255, 255, 255, 0.12); padding: 16px; border-radius: 28px; backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25);">
                <img src='{logo_url}' style='height: 100px; width: auto;' />
            </div>
            <h1 style='text-align: center; color: #FFFFFF; font-size: 3.5rem; font-weight: 800; letter-spacing: -0.03em; margin-top: 14px; line-height: 1.05; text-shadow: 0 4px 15px rgba(0,0,0,0.2);'>
                SNAP<span style="color: #818CF8;">CLASS</span>
            </h1>
            <p style="color: #C7D2FE; font-size: 1.15rem; font-weight: 600; margin-top: 6px; letter-spacing: 0.02em;">
                ✨ AI-Powered Automated Classroom Attendance
            </p>
        </div>   
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; gap: 14px; margin-bottom: 0.5rem;">
            <div style="background: #FFFFFF; padding: 8px; border-radius: 18px; border: 1px solid rgba(99, 102, 241, 0.2); box-shadow: 0 4px 14px rgba(99, 102, 241, 0.12);">
                <img src='{logo_url}' style='height: 52px; width: auto;' />
            </div>
            <div>
                <h2 style='text-align:left; color:#4F46E5; font-size: 1.9rem; font-weight: 800; line-height: 1.0; margin: 0; letter-spacing: -0.02em;'>
                    SNAP<span style="color: #F43F5E;">CLASS</span>
                </h2>
                <span style="font-size: 0.8rem; font-weight: 700; color: #64748B; letter-spacing: 0.06em; text-transform: uppercase;">Smart Attendance AI</span>
            </div>
        </div>   
    """, unsafe_allow_html=True)

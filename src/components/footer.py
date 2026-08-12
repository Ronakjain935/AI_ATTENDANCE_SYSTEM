import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top: 3.5rem; display: flex; justify-content: center; align-items: center;">
            <div style="background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.18); padding: 8px 20px; border-radius: 9999px; backdrop-filter: blur(10px); box-shadow: 0 4px 15px rgba(0,0,0,0.15);">
                <p style="font-weight: 700; color: #FFFFFF; margin: 0; font-size: 0.92rem; letter-spacing: 0.02em;">
                    Crafted with ❤️ by <span style="color: #38BDF8; font-weight: 800;">Ronak Jain</span>
                </p>  
            </div>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top: 3.5rem; display: flex; justify-content: center; align-items: center;">
            <div style="background: #FFFFFF; border: 1px solid rgba(99, 102, 241, 0.15); padding: 8px 22px; border-radius: 9999px; box-shadow: 0 4px 14px rgba(79, 70, 229, 0.08);">
                <p style="font-weight: 700; color: #0F172A; margin: 0; font-size: 0.92rem; letter-spacing: 0.02em;">
                    Crafted with ❤️ by <span style="color: #4F46E5; font-weight: 800;">Ronak Jain</span>
                </p>  
            </div>
        </div>
    """, unsafe_allow_html=True)

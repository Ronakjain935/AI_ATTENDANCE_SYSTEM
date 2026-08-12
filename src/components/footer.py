import streamlit as st

def footer_home():
    st.markdown("""
        <div style="margin-top:3rem; display:flex; gap:8px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:white; margin: 0;"> Created with ❤️ by <span style="color:#38bdf8;">Ronak Jain</span></p>  
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="margin-top:3rem; display:flex; gap:8px; justify-content:center; align-items:center">
            <p style="font-weight:bold; color:#1e293b; margin: 0;"> Created with ❤️ by <span style="color:#0284c7;">Ronak Jain</span></p>  
        </div>
    """, unsafe_allow_html=True)


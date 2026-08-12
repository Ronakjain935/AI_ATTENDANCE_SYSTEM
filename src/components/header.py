import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:20px">
            <img src='{logo_url}' style='height:110px;' />
            <h1 style='text-align:center; color:#E0E3FF; font-size: 3.2rem; font-weight: 800; letter-spacing: -0.02em; margin-top: 10px; line-height: 1.1;'>
                SNAP<br/>CLASS
            </h1>
        </div>   
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; gap:14px">
            <img src='{logo_url}' style='height:75px;' />
            <h2 style='text-align:left; color:#5865F2; font-size: 2.2rem; font-weight: 800; line-height: 1.0; margin: 0;'>
                SNAP<br/>CLASS
            </h2>
        </div>   
    """, unsafe_allow_html=True)

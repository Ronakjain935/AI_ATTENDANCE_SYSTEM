import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    st.markdown("""
        <style>
            .portal-card {
                background-color: #E0E3FF;
                border-radius: 2.5rem;
                padding: 2.5rem 2rem;
                text-align: center;
                box-shadow: 0 12px 35px rgba(0, 0, 0, 0.2);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;
                min-height: 380px;
                border: 2px solid rgba(255, 255, 255, 0.4);
            }
            .portal-card h2 {
                color: #1e293b;
                font-size: 2.2rem;
                font-weight: 800;
                margin-top: 0;
                margin-bottom: 1.5rem;
            }
            .portal-img-container {
                height: 140px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 2rem;
            }
            .portal-img-container img {
                max-height: 130px;
                object-fit: contain;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div class="portal-card">
                <div>
                    <h2>I'm Student</h2>
                    <div class="portal-img-container">
                        <img src="https://i.ibb.co/844D9Lrt/mascot-student.png" />
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top: -55px; padding: 0 1.5rem;'>", unsafe_allow_html=True)
        if st.button('Student Portal ➔', type='primary', use_container_width=True, key='student_btn'):
            st.session_state['login_type'] = 'student'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="portal-card">
                <div>
                    <h2>I'm Teacher</h2>
                    <div class="portal-img-container">
                        <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" />
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top: -55px; padding: 0 1.5rem;'>", unsafe_allow_html=True)
        if st.button('Teacher Portal ➔', type='primary', use_container_width=True, key='teacher_btn'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    footer_home()
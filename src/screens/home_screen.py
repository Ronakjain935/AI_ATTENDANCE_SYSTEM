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
                background: rgba(255, 255, 255, 0.94);
                backdrop-filter: blur(20px);
                border-radius: 2rem;
                padding: 2.5rem 2rem 3.5rem 2rem;
                text-align: center;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.2);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;
                min-height: 390px;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .portal-card:hover {
                transform: translateY(-6px);
                box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.3);
            }
            .portal-card h2 {
                color: #0F172A !important;
                font-size: 2.1rem !important;
                font-weight: 800 !important;
                margin-top: 0;
                margin-bottom: 0.5rem;
                letter-spacing: -0.02em;
            }
            .portal-card p {
                color: #64748B !important;
                font-size: 0.95rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
            }
            .portal-img-container {
                height: 140px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 1rem;
            }
            .portal-img-container img {
                max-height: 135px;
                object-fit: contain;
                filter: drop-shadow(0 10px 20px rgba(0,0,0,0.12));
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div class="portal-card">
                <div>
                    <h2>Student Portal</h2>
                    <p>Mark attendance & view enrolled courses</p>
                    <div class="portal-img-container">
                        <img src="https://i.ibb.co/844D9Lrt/mascot-student.png" alt="Student Mascot" />
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top: -50px; padding: 0 1.5rem;'>", unsafe_allow_html=True)
        if st.button('Enter Student Portal ➔', type='primary', use_container_width=True, key='student_btn'):
            st.session_state['login_type'] = 'student'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="portal-card">
                <div>
                    <h2>Teacher Portal</h2>
                    <p>Scan attendance & manage subjects</p>
                    <div class="portal-img-container">
                        <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" alt="Teacher Mascot" />
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top: -50px; padding: 0 1.5rem;'>", unsafe_allow_html=True)
        if st.button('Enter Teacher Portal ➔', type='secondary', use_container_width=True, key='teacher_btn'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    footer_home()
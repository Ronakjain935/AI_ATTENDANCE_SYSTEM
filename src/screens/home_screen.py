import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.utils.assets import get_asset_base64

def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    student_b64 = get_asset_base64("student_mascot.png")
    student_img_src = student_b64 if student_b64 else "https://i.ibb.co/844D9Lrt/mascot-student.png"

    teacher_b64 = get_asset_base64("teacher_mascot.png")
    teacher_img_src = teacher_b64 if teacher_b64 else "https://i.ibb.co/CsmQQV6X/mascot-prof.png"

    st.markdown("""
        <style>
            .portal-card {
                position: relative;
                background: rgba(255, 255, 255, 0.94);
                backdrop-filter: blur(24px);
                border-radius: 2.2rem;
                padding: 2.2rem 2rem 3.5rem 2rem;
                text-align: center;
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.25);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: space-between;
                min-height: 420px;
                transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
                overflow: hidden;
            }
            .portal-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 6px;
            }
            .portal-card-student::before {
                background: linear-gradient(90deg, #4F46E5, #818CF8, #6366F1);
            }
            .portal-card-teacher::before {
                background: linear-gradient(90deg, #059669, #10B981, #34D399);
            }
            .portal-card:hover {
                transform: translateY(-8px) scale(1.01);
                box-shadow: 0 35px 75px rgba(0, 0, 0, 0.45), 0 0 30px rgba(99, 102, 241, 0.25);
            }
            .portal-badge {
                display: inline-block;
                padding: 4px 14px;
                border-radius: 9999px;
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin-bottom: 0.8rem;
            }
            .badge-student {
                background: rgba(79, 70, 229, 0.12);
                color: #4F46E5;
                border: 1px solid rgba(79, 70, 229, 0.2);
            }
            .badge-teacher {
                background: rgba(16, 185, 129, 0.12);
                color: #059669;
                border: 1px solid rgba(16, 185, 129, 0.2);
            }
            .portal-card h2 {
                color: #0F172A !important;
                font-size: 2.2rem !important;
                font-weight: 800 !important;
                margin-top: 0;
                margin-bottom: 0.4rem;
                letter-spacing: -0.02em;
            }
            .portal-card p {
                color: #64748B !important;
                font-size: 0.96rem;
                font-weight: 600;
                margin-bottom: 1.2rem;
            }
            .portal-img-container {
                height: 180px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 0.5rem;
            }
            .portal-img-container img {
                max-height: 175px;
                max-width: 100%;
                object-fit: contain;
                filter: drop-shadow(0 15px 25px rgba(0,0,0,0.18));
                transition: transform 0.3s ease;
            }
            .portal-card:hover .portal-img-container img {
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(f"""
            <div class="portal-card portal-card-student">
                <div>
                    <span class="portal-badge badge-student">Student Access</span>
                    <h2>Student Portal</h2>
                    <p>Mark attendance instantly & view enrolled courses</p>
                    <div class="portal-img-container">
                        <img src="{student_img_src}" alt="Student Mascot 3D" />
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top: -55px; padding: 0 1.5rem; position: relative; z-index: 10;'>", unsafe_allow_html=True)
        if st.button('Enter Student Portal ➔', type='primary', use_container_width=True, key='student_btn'):
            st.session_state['login_type'] = 'student'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="portal-card portal-card-teacher">
                <div>
                    <span class="portal-badge badge-teacher">Instructor Control</span>
                    <h2>Teacher Portal</h2>
                    <p>Scan classroom attendance & manage subjects</p>
                    <div class="portal-img-container">
                        <img src="{teacher_img_src}" alt="Teacher Mascot 3D" />
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div style='margin-top: -55px; padding: 0 1.5rem; position: relative; z-index: 10;'>", unsafe_allow_html=True)
        if st.button('Enter Teacher Portal ➔', type='secondary', use_container_width=True, key='teacher_btn'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    footer_home()
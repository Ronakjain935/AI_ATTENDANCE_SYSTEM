import streamlit as st
from PIL import Image

@st.dialog("Classroom Photos")
def add_photos_dialog():
    current_count = len(st.session_state.attendance_images) if 'attendance_images' in st.session_state else 0
    st.markdown(f"<p style='color: #667085; font-size: 0.88rem; margin-bottom: 0.75rem;'>Capture or upload classroom photos for facial attendance recognition. Current batch: <strong>{current_count} photos</strong>.</p>", unsafe_allow_html=True)

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'secondary'
        if st.button('📷 Camera Snapshot', type=type_camera, use_container_width=True):
            st.session_state.photo_tab = 'camera'
            st.rerun()

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'secondary'
        if st.button('📁 Upload Images', type=type_upload, use_container_width=True):
            st.session_state.photo_tab = 'upload'
            st.rerun()

    st.write("")

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Capture Classroom Photo', key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast('Photo captured successfully!')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader('Select classroom image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast(f'{len(uploaded_files)} photos added successfully!')
            st.rerun()

    st.divider()
    if st.button('Done & Return to Console', type='primary', use_container_width=True):
        st.rerun()

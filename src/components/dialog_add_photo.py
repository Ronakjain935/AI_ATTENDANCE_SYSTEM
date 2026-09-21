import streamlit as st
from PIL import Image

@st.dialog("Classroom Photos")
def add_photos_dialog():
    st.markdown("<p style='color: #475569; font-size: 0.9rem; margin-bottom: 1rem;'>Capture or upload classroom photos for facial attendance recognition.</p>", unsafe_allow_html=True)

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'secondary'
        if st.button('Take Snapshot', type=type_camera, use_container_width=True):
            st.session_state.photo_tab = 'camera'
            st.rerun()

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'secondary'
        if st.button('Upload Images', type=type_upload, use_container_width=True):
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
        uploaded_files = st.file_uploader('Select image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast('Photos added successfully!')
            st.rerun()

    st.divider()
    if st.button('Done', type='primary', use_container_width=True):
        st.rerun()

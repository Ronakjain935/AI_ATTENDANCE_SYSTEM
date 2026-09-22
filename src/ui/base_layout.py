import streamlit as st

def style_page_background():
    """Sets the fixed warm ivory page background across the application."""
    st.markdown("""<style>
.stApp {
    background-color: #F7F6F2 !important;
    background-image: none !important;
    color: #1F2937 !important;
}
</style>""", unsafe_allow_html=True)

def style_background_home():
    """Alias for backwards compatibility."""
    style_page_background()

def style_background_dashboard():
    """Alias for backwards compatibility."""
    style_page_background()

def style_base_layout():
    """
    Injects the single, fixed Classic Modern Academic UI styling system.
    Strictly NO light/dark mode switching. Maximum text readability.
    """
    css = """<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #F7F6F2 !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    color: #1F2937 !important;
    overflow-x: hidden !important;
    max-width: 100vw;
    -webkit-font-smoothing: antialiased;
}

/* Headings: Deep Navy, Bold, High Readability */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    color: #172B4D !important;
    letter-spacing: -0.02em !important;
}

p, span, label, div {
    color: #1F2937;
}

/* Hide Default Streamlit Chrome */
#MainMenu, footer, header, [data-testid="stHeader"] {
    visibility: hidden !important;
    height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
}

/* Container Spacing */
.block-container {
    padding-top: 1.25rem !important;
    padding-bottom: 3rem !important;
    padding-left: 1.5rem !important;
    padding-right: 1.5rem !important;
    max-width: 1140px !important;
    margin: 0 auto !important;
}

/* Cards: Pure White with Soft Gray Border */
[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border-radius: 12px !important;
    padding: 1.4rem !important;
    border: 1px solid #D9DEE7 !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04) !important;
}

/* Visible Form Labels with Dark Charcoal Text */
label, label p, [data-testid="stWidgetLabel"] p {
    color: #172B4D !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.01em !important;
    margin-bottom: 4px !important;
}

/* High-Contrast Form Inputs */
.stTextInput input, .stNumberInput input, .stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border-radius: 8px !important;
    border: 1px solid #D9DEE7 !important;
    padding: 10px 14px !important;
    font-size: 0.94rem !important;
    font-weight: 500 !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02) !important;
}
.stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {
    border-color: #2F6FED !important;
    box-shadow: 0 0 0 3px rgba(47, 111, 237, 0.15) !important;
    outline: none !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: #8C9BAE !important;
    font-weight: 400 !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border-radius: 8px !important;
    border: 1px solid #D9DEE7 !important;
    min-height: 42px !important;
}

/* BUTTON SYSTEM: Strong Contrast & Touch Targets */
.stButton > button {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    padding: 10px 18px !important;
    min-height: 42px !important;
    font-size: 0.90rem !important;
    letter-spacing: 0.01em !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    transition: all 0.12s ease !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08) !important;
}

/* Primary Button: Deep Navy */
.stButton > button[kind="primary"],
.stButton > button[data-testid="stBaseButton-primary"] {
    background-color: #172B4D !important;
    color: #FFFFFF !important;
    border: 1px solid #0F1C33 !important;
}
.stButton > button[kind="primary"]:hover {
    background-color: #0F1C33 !important;
}
.stButton > button[kind="primary"] * {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* Secondary Button: White Card with Deep Navy Text & Soft Border */
.stButton > button[kind="secondary"],
.stButton > button[data-testid="stBaseButton-secondary"] {
    background-color: #FFFFFF !important;
    color: #172B4D !important;
    border: 1px solid #D9DEE7 !important;
}
.stButton > button[kind="secondary"]:hover {
    background-color: #F7F6F2 !important;
    border-color: #172B4D !important;
}
.stButton > button[kind="secondary"] * {
    color: #172B4D !important;
    font-weight: 600 !important;
}

/* Tertiary Button */
.stButton > button[kind="tertiary"],
.stButton > button[data-testid="stBaseButton-tertiary"] {
    background-color: transparent !important;
    color: #40566F !important;
    border: 1px solid transparent !important;
}
.stButton > button[kind="tertiary"]:hover {
    background-color: #EAE8E0 !important;
    color: #172B4D !important;
}

/* Dialogs & Modals: Pure White with Dark Text */
div[data-baseweb="modal"] {
    background-color: rgba(23, 43, 77, 0.45) !important;
    backdrop-filter: blur(4px) !important;
}
div[data-baseweb="modal"] > div,
div[role="dialog"],
[data-testid="stModal"] > div {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border-radius: 12px !important;
    border: 1px solid #D9DEE7 !important;
    padding: 1.6rem !important;
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12) !important;
}
[data-testid="stDialogHeader"] h2,
div[role="dialog"] h2,
div[data-baseweb="modal"] h2 {
    color: #172B4D !important;
    font-size: 1.35rem !important;
    font-weight: 700 !important;
}

/* DataFrames & Tables */
[data-testid="stDataFrame"] {
    background-color: #FFFFFF !important;
    border: 1px solid #D9DEE7 !important;
    border-radius: 8px !important;
}

/* Expanders */
[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    border: 1px solid #D9DEE7 !important;
    border-radius: 8px !important;
}
[data-testid="stExpander"] summary {
    color: #172B4D !important;
    font-weight: 600 !important;
}

/* Camera Viewfinder */
[data-testid="stCameraInput"] {
    background-color: #FAF9F5 !important;
    border: 1.5px dashed #D9DEE7 !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* File Uploader */
[data-testid="stFileUploader"] section {
    background-color: #FAF9F5 !important;
    border: 1.5px dashed #D9DEE7 !important;
    border-radius: 8px !important;
}

/* Responsive Media Queries */
@media (max-width: 768px) {
    .block-container {
        padding-top: 0.85rem !important;
        padding-left: 0.85rem !important;
        padding-right: 0.85rem !important;
    }
    .stButton > button {
        min-height: 44px !important;
    }
}

@media (max-width: 480px) {
    .block-container {
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    .stButton > button {
        width: 100% !important;
    }
    [data-testid="column"] {
        min-width: 100% !important;
        margin-bottom: 0.5rem !important;
    }
}
</style>"""
    st.markdown(css, unsafe_allow_html=True)
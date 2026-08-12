import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background-color: #5865F2 !important;
                color: #ffffff !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background-color: #E0E3FF !important;
                color: #0f172a !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

            html, body, p, div, label {
                font-family: 'Outfit', 'Inter', sans-serif !important;
            }

            h1, h2, h3, h4, h5, h6 {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
                color: #0f172a !important;
            }

            /* Protect Streamlit Material Icons */
            [data-testid="stIconMaterial"], [data-testid="stIconMaterial"] * {
                font-family: 'Material Symbols Rounded', 'Material Symbols Outlined' !important;
                font-style: normal !important;
                font-weight: normal !important;
                display: inline-block !important;
            }

            /* Hide Default Streamlit Header */
            #MainMenu, footer, header, [data-testid="stHeader"] {
                visibility: hidden !important;
                height: 0 !important;
            }

            .block-container {
                padding-top: 1.5rem !important;
                padding-bottom: 2rem !important;
                max-width: 1100px !important;
            }

            /* High Contrast Labels for Selectboxes & Text Inputs */
            label, label p, label span, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
                color: #0f172a !important;
                font-weight: 700 !important;
                font-size: 1rem !important;
                margin-bottom: 4px !important;
            }

            /* Text Inputs & Area Styling */
            .stTextInput input, .stNumberInput input, .stTextArea textarea {
                background-color: #ffffff !important;
                color: #0f172a !important;
                border-radius: 12px !important;
                border: 2px solid rgba(88, 101, 242, 0.4) !important;
                padding: 10px 14px !important;
                font-size: 1rem !important;
            }
            .stTextInput input::placeholder, .stTextArea textarea::placeholder {
                color: #64748b !important;
            }

            /* Selectbox Styling */
            div[data-baseweb="select"] > div {
                background-color: #ffffff !important;
                color: #0f172a !important;
                border-radius: 12px !important;
                border: 2px solid rgba(88, 101, 242, 0.4) !important;
                min-height: 48px !important;
                padding-left: 6px !important;
            }
            div[data-baseweb="select"] span, div[data-baseweb="select"] div {
                color: #0f172a !important;
                font-size: 1rem !important;
                font-weight: 600 !important;
            }

            /* Dropdown Options Popover Menu Fix */
            div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
                background-color: #ffffff !important;
                border-radius: 12px !important;
                border: 1px solid rgba(88, 101, 242, 0.3) !important;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15) !important;
            }
            li[role="option"] {
                color: #0f172a !important;
                background-color: #ffffff !important;
                font-weight: 600 !important;
            }
            li[role="option"]:hover, li[aria-selected="true"] {
                background-color: #5865F220 !important;
                color: #5865F2 !important;
            }

            /* File Uploader Widget Fix */
            [data-testid="stFileUploader"] {
                background-color: #ffffff !important;
                border-radius: 16px !important;
                border: 2px dashed rgba(88, 101, 242, 0.4) !important;
                padding: 1rem !important;
            }
            [data-testid="stFileUploader"] * {
                color: #0f172a !important;
            }

            /* Buttons */
            .stButton > button {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                border-radius: 1.5rem !important;
                padding: 12px 24px !important;
                min-height: 52px !important;
                border: none !important;
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
                font-size: 1.05rem !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 8px !important;
            }
            .stButton > button:hover {
                transform: translateY(-2px) scale(1.02) !important;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2) !important;
            }

            /* Primary Button (#5865F2 - Purple Blue) */
            .stButton > button[kind="primary"],
            .stButton > button[data-testid="stBaseButton-primary"] {
                background-color: #5865F2 !important;
                color: #ffffff !important;
                border: none !important;
            }
            .stButton > button[kind="primary"] *,
            .stButton > button[data-testid="stBaseButton-primary"] * {
                color: #ffffff !important;
            }

            /* Secondary Button (#EB459E - Hot Pink) */
            .stButton > button[kind="secondary"],
            .stButton > button[data-testid="stBaseButton-secondary"] {
                background-color: #EB459E !important;
                color: #ffffff !important;
                border: none !important;
            }
            .stButton > button[kind="secondary"] *,
            .stButton > button[data-testid="stBaseButton-secondary"] * {
                color: #ffffff !important;
            }

            /* Tertiary Button (Clean Light Slate Gray Background with Dark Navy Text) */
            .stButton > button[kind="tertiary"],
            .stButton > button[data-testid="stBaseButton-tertiary"] {
                background-color: #f1f5f9 !important;
                color: #0f172a !important;
                border: 1.5px solid #cbd5e1 !important;
            }
            .stButton > button[kind="tertiary"] *,
            .stButton > button[data-testid="stBaseButton-tertiary"] * {
                color: #0f172a !important;
            }

            /* Disabled Buttons */
            .stButton > button:disabled {
                opacity: 0.55 !important;
                cursor: not-allowed !important;
                transform: none !important;
            }

            /* Cards & Border Wrappers */
            [data-testid="stVerticalBlockBorderWrapper"] {
                background-color: #ffffff !important;
                border-radius: 2rem !important;
                padding: 2.2rem !important;
                border: 2px solid rgba(88, 101, 242, 0.15) !important;
                box-shadow: 0 10px 30px rgba(88, 101, 242, 0.12) !important;
            }

            /* --- DIALOG & MODAL HIGH-CONTRAST VISIBILITY FIXES --- */
            div[data-baseweb="modal"] {
                background-color: rgba(15, 23, 42, 0.75) !important;
            }

            div[data-baseweb="modal"] > div,
            div[role="dialog"],
            [data-testid="stModal"] > div {
                background-color: #ffffff !important;
                color: #0f172a !important;
                border-radius: 24px !important;
                border: 2px solid rgba(88, 101, 242, 0.25) !important;
                box-shadow: 0 25px 60px rgba(0, 0, 0, 0.45) !important;
                padding: 1.8rem !important;
                overflow: visible !important;
            }

            /* Modal Header & Title Visibility Fix */
            [data-testid="stDialogHeader"],
            div[role="dialog"] header,
            div[data-baseweb="modal"] header {
                padding-top: 0.25rem !important;
                margin-bottom: 0.75rem !important;
            }

            [data-testid="stDialogHeader"] h2,
            div[role="dialog"] h2,
            div[data-baseweb="modal"] h2,
            [data-testid="stDialog"] h2 {
                color: #0f172a !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 1.45rem !important;
                font-weight: 800 !important;
                margin: 0 !important;
                line-height: 1.3 !important;
            }

            /* Force visible text and labels in dialogs EXCEPT inside buttons */
            div[role="dialog"] h1, div[role="dialog"] h3, div[role="dialog"] h4, div[role="dialog"] h5, div[role="dialog"] h6,
            div[data-baseweb="modal"] h1, div[data-baseweb="modal"] h3, div[data-baseweb="modal"] h4, div[data-baseweb="modal"] h5, div[data-baseweb="modal"] h6 {
                color: #0f172a !important;
            }

            div[role="dialog"] p:not(.stButton *), 
            div[role="dialog"] span:not(.stButton *), 
            div[role="dialog"] label, 
            div[data-baseweb="modal"] p:not(.stButton *), 
            div[data-baseweb="modal"] span:not(.stButton *), 
            div[data-baseweb="modal"] label,
            [data-testid="stDialog"] p:not(.stButton *),
            [data-testid="stDialog"] label {
                color: #1e293b !important;
            }

            /* Close Button inside Dialog */
            div[data-baseweb="modal"] button[aria-label="Close"],
            div[role="dialog"] button[aria-label="Close"],
            [data-testid="stDialog"] button[aria-label="Close"] {
                color: #0f172a !important;
                background-color: #f1f5f9 !important;
                border-radius: 50% !important;
            }
            div[data-baseweb="modal"] button[aria-label="Close"] svg,
            div[role="dialog"] button[aria-label="Close"] svg {
                fill: #0f172a !important;
                stroke: #0f172a !important;
            }

            /* Dataframe Table Visibility */
            [data-testid="stDataFrame"] {
                background-color: #ffffff !important;
                border-radius: 12px !important;
                border: 1px solid #cbd5e1 !important;
            }

            /* Code Blocks inside Dialog */
            div[role="dialog"] [data-testid="stCodeBlock"],
            div[data-baseweb="modal"] [data-testid="stCodeBlock"],
            [data-testid="stDialog"] [data-testid="stCodeBlock"] {
                background-color: #f8fafc !important;
                border: 1px solid #cbd5e1 !important;
                border-radius: 12px !important;
            }
            div[role="dialog"] [data-testid="stCodeBlock"] code,
            div[data-baseweb="modal"] [data-testid="stCodeBlock"] code,
            [data-testid="stDialog"] [data-testid="stCodeBlock"] code {
                color: #0f172a !important;
                font-family: monospace !important;
                font-weight: 600 !important;
            }
        </style>
    """, unsafe_allow_html=True)
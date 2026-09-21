import streamlit as st

def style_background_home():
    st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.06) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(16, 185, 129, 0.04) 0px, transparent 50%) !important;
        background-attachment: fixed !important;
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC !important;
        background-image: 
            radial-gradient(at 50% 0%, rgba(99, 102, 241, 0.04) 0px, transparent 40%) !important;
        background-attachment: fixed !important;
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

    html, body, p, div, label, span {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        color: #1E293B;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
        color: #0F172A !important;
    }

    /* Minimal Modern Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    ::-webkit-scrollbar-track {
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: #CBD5E1;
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #94A3B8;
    }

    /* Protect Streamlit Material Icons */
    [data-testid="stIconMaterial"], [data-testid="stIconMaterial"] * {
        font-family: 'Material Symbols Rounded', 'Material Symbols Outlined' !important;
        font-style: normal !important;
        font-weight: normal !important;
        display: inline-block !important;
    }

    /* Hide Default Streamlit Header & Clutter */
    #MainMenu, footer, header, [data-testid="stHeader"] {
        visibility: hidden !important;
        height: 0 !important;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        max-width: 1080px !important;
    }

    /* Crisp Form Labels */
    label, label p, label span, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        letter-spacing: 0.01em !important;
        margin-bottom: 4px !important;
    }

    /* Inputs, Numbers & TextAreas */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 8px !important;
        border: 1px solid #CBD5E1 !important;
        padding: 9px 13px !important;
        font-size: 0.92rem !important;
        font-weight: 500 !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03) !important;
        transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
    }
    .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {
        border-color: #4F46E5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.12) !important;
        outline: none !important;
    }
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: #94A3B8 !important;
        font-weight: 400 !important;
    }

    /* Selectbox Input */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 8px !important;
        border: 1px solid #CBD5E1 !important;
        min-height: 42px !important;
        padding-left: 6px !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03) !important;
        transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
    }
    div[data-baseweb="select"]:focus-within > div {
        border-color: #4F46E5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.12) !important;
    }
    div[data-baseweb="select"] span, div[data-baseweb="select"] div {
        color: #0F172A !important;
        font-size: 0.92rem !important;
        font-weight: 500 !important;
    }

    /* Dropdown Menus */
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04) !important;
        padding: 4px !important;
    }
    li[role="option"] {
        color: #334155 !important;
        background-color: #FFFFFF !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
        padding: 8px 12px !important;
        margin-bottom: 2px !important;
    }
    li[role="option"]:hover, li[aria-selected="true"] {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
    }

    /* File Uploader Container */
    [data-testid="stFileUploader"] {
        background: #FFFFFF !important;
        border-radius: 12px !important;
        border: 1.5px dashed #CBD5E1 !important;
        padding: 1.25rem !important;
        transition: border-color 0.15s ease !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #4F46E5 !important;
    }
    [data-testid="stFileUploader"] * {
        color: #334155 !important;
    }

    /* Professional Button System (Human-Crafted SaaS) */
    .stButton > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 9px 18px !important;
        min-height: 42px !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.01em !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
    }
    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* Primary Button (Refined Indigo) */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: #4F46E5 !important;
        color: #FFFFFF !important;
        border: 1px solid #4338CA !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
    }
    .stButton > button[kind="primary"]:hover,
    .stButton > button[data-testid="stBaseButton-primary"]:hover {
        background: #4338CA !important;
        box-shadow: 0 3px 8px rgba(79, 70, 229, 0.25) !important;
    }
    .stButton > button[kind="primary"] *,
    .stButton > button[data-testid="stBaseButton-primary"] * {
        color: #FFFFFF !important;
    }

    /* Secondary Button (Neutral Slate) */
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"] {
        background: #F8FAFC !important;
        color: #1E293B !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04) !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="stBaseButton-secondary"]:hover {
        background: #F1F5F9 !important;
        border-color: #94A3B8 !important;
        color: #0F172A !important;
    }
    .stButton > button[kind="secondary"] *,
    .stButton > button[data-testid="stBaseButton-secondary"] * {
        color: #1E293B !important;
    }

    /* Tertiary Button (Subtle Outline / Minimal) */
    .stButton > button[kind="tertiary"],
    .stButton > button[data-testid="stBaseButton-tertiary"] {
        background: #FFFFFF !important;
        color: #475569 !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02) !important;
    }
    .stButton > button[kind="tertiary"]:hover,
    .stButton > button[data-testid="stBaseButton-tertiary"]:hover {
        background: #F8FAFC !important;
        border-color: #CBD5E1 !important;
        color: #0F172A !important;
    }
    .stButton > button[kind="tertiary"] *,
    .stButton > button[data-testid="stBaseButton-tertiary"] * {
        color: #475569 !important;
    }

    .stButton > button:disabled {
        opacity: 0.55 !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
    }

    /* Containers & Card Wrappers */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 1.75rem !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02) !important;
    }

    /* Clean Dialog & Modal System */
    div[data-baseweb="modal"] {
        background-color: rgba(15, 23, 42, 0.45) !important;
        backdrop-filter: blur(4px) !important;
    }
    div[data-baseweb="modal"] > div,
    div[role="dialog"],
    [data-testid="stModal"] > div {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 14px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.06) !important;
        padding: 2rem !important;
    }

    [data-testid="stDialogHeader"],
    div[role="dialog"] header,
    div[data-baseweb="modal"] header {
        padding-top: 0.1rem !important;
        margin-bottom: 0.6rem !important;
    }
    [data-testid="stDialogHeader"] h2,
    div[role="dialog"] h2,
    div[data-baseweb="modal"] h2,
    [data-testid="stDialog"] h2 {
        color: #0F172A !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.015em !important;
        margin: 0 !important;
    }

    /* Modal Close Button */
    div[data-baseweb="modal"] button[aria-label="Close"],
    div[role="dialog"] button[aria-label="Close"],
    [data-testid="stDialog"] button[aria-label="Close"] {
        color: #64748B !important;
        background-color: #F1F5F9 !important;
        border-radius: 6px !important;
        transition: background-color 0.15s ease !important;
    }
    div[data-baseweb="modal"] button[aria-label="Close"]:hover {
        background-color: #E2E8F0 !important;
        color: #0F172A !important;
    }

    /* Dataframe / Table */
    [data-testid="stDataFrame"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02) !important;
    }

    /* Dividers */
    hr {
        border-color: #E2E8F0 !important;
        margin: 1.5rem 0 !important;
    }

    /* Expander */
    [data-testid="stExpander"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E2E8F0 !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02) !important;
    }
</style>
""", unsafe_allow_html=True)
import streamlit as st

def style_background_home():
    st.markdown("""
<style>
    .stApp {
        background-color: #F8F9FA !important;
        background-image: 
            radial-gradient(#E2E8F0 1px, transparent 1px),
            radial-gradient(at 0% 0%, rgba(30, 58, 138, 0.03) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(15, 23, 42, 0.02) 0px, transparent 50%) !important;
        background-size: 24px 24px, 100% 100%, 100% 100% !important;
        background-attachment: fixed !important;
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
<style>
    .stApp {
        background-color: #F8F9FA !important;
        background-image: 
            radial-gradient(#E2E8F0 1px, transparent 1px),
            radial-gradient(at 50% 0%, rgba(30, 58, 138, 0.02) 0px, transparent 40%) !important;
        background-size: 24px 24px, 100% 100% !important;
        background-attachment: fixed !important;
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    html, body, p, div, label, span {
        font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif !important;
        color: #1E293B;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Lora', Georgia, 'Times New Roman', serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.015em !important;
        color: #0F172A !important;
    }

    /* Classic Minimal Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
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

    /* Hide Default Streamlit Header & Chrome */
    #MainMenu, footer, header, [data-testid="stHeader"] {
        visibility: hidden !important;
        height: 0 !important;
    }

    .block-container {
        padding-top: 1.25rem !important;
        padding-bottom: 3rem !important;
        max-width: 1120px !important;
    }

    /* Form Labels - Classic Editorial Style */
    label, label p, label span, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.02em !important;
        margin-bottom: 5px !important;
        text-transform: uppercase;
    }

    /* Classic Inputs, Numbers & TextAreas */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 8px !important;
        border: 1px solid #CBD5E1 !important;
        padding: 10px 14px !important;
        font-size: 0.92rem !important;
        font-weight: 500 !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03) !important;
        transition: all 0.15s ease !important;
    }
    .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {
        border-color: #1E3A8A !important;
        box-shadow: 0 0 0 3px rgba(30, 58, 138, 0.12), 0 1px 2px rgba(15, 23, 42, 0.04) !important;
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
        padding-left: 8px !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.03) !important;
        transition: all 0.15s ease !important;
    }
    div[data-baseweb="select"]:focus-within > div {
        border-color: #1E3A8A !important;
        box-shadow: 0 0 0 3px rgba(30, 58, 138, 0.12) !important;
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
        border: 1px solid #CBD5E1 !important;
        box-shadow: 0 12px 28px -4px rgba(15, 23, 42, 0.12), 0 4px 8px -2px rgba(15, 23, 42, 0.06) !important;
        padding: 6px !important;
    }
    li[role="option"] {
        color: #334155 !important;
        background-color: #FFFFFF !important;
        font-weight: 500 !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
        padding: 9px 12px !important;
        margin-bottom: 2px !important;
        transition: background-color 0.12s ease !important;
    }
    li[role="option"]:hover, li[aria-selected="true"] {
        background-color: #F1F5F9 !important;
        color: #0F172A !important;
        font-weight: 600 !important;
    }

    /* File Uploader Container */
    [data-testid="stFileUploader"] {
        background: #FFFFFF !important;
        border-radius: 10px !important;
        border: 1.5px dashed #CBD5E1 !important;
        padding: 1.5rem !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02) !important;
        transition: border-color 0.15s ease, background 0.15s ease !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #1E3A8A !important;
        background: #FAFAFA !important;
    }
    [data-testid="stFileUploader"] * {
        color: #334155 !important;
    }

    /* Classic Executive Button System */
    .stButton > button {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 9px 18px !important;
        min-height: 42px !important;
        font-size: 0.90rem !important;
        letter-spacing: 0.015em !important;
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

    /* Primary Button: Classic Deep Oxford Navy */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #0A192F !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.15) !important;
    }
    .stButton > button[kind="primary"]:hover,
    .stButton > button[data-testid="stBaseButton-primary"]:hover {
        background: linear-gradient(180deg, #0F172A 0%, #020617 100%) !important;
        box-shadow: 0 4px 10px rgba(15, 23, 42, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.2) !important;
    }
    .stButton > button[kind="primary"] *,
    .stButton > button[data-testid="stBaseButton-primary"] * {
        color: #FFFFFF !important;
    }

    /* Secondary Button: Crisp Classic Slate & Porcelain */
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%) !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04), inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;
    }
    .stButton > button[kind="secondary"]:hover,
    .stButton > button[data-testid="stBaseButton-secondary"]:hover {
        background: #F1F5F9 !important;
        border-color: #94A3B8 !important;
        color: #0F172A !important;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.08) !important;
    }
    .stButton > button[kind="secondary"] *,
    .stButton > button[data-testid="stBaseButton-secondary"] * {
        color: #0F172A !important;
    }

    /* Tertiary Button: Minimal Classic Outline */
    .stButton > button[kind="tertiary"],
    .stButton > button[data-testid="stBaseButton-tertiary"] {
        background: #FFFFFF !important;
        color: #475569 !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02) !important;
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
        opacity: 0.5 !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
    }

    /* Containers & Card Wrappers - Classic Academic Elegance */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF !important;
        border-radius: 12px !important;
        padding: 1.6rem !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04), 0 4px 12px -2px rgba(15, 23, 42, 0.02) !important;
        transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
    }

    /* Classic Modal System */
    div[data-baseweb="modal"] {
        background-color: rgba(15, 23, 42, 0.6) !important;
        backdrop-filter: blur(5px) !important;
    }
    div[data-baseweb="modal"] > div,
    div[role="dialog"],
    [data-testid="stModal"] > div {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border-radius: 14px !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: 0 20px 45px -10px rgba(15, 23, 42, 0.22) !important;
        padding: 2rem !important;
    }

    [data-testid="stDialogHeader"],
    div[role="dialog"] header,
    div[data-baseweb="modal"] header {
        padding-top: 0.1rem !important;
        margin-bottom: 0.8rem !important;
    }
    [data-testid="stDialogHeader"] h2,
    div[role="dialog"] h2,
    div[data-baseweb="modal"] h2,
    [data-testid="stDialog"] h2 {
        color: #0F172A !important;
        font-family: 'Lora', Georgia, serif !important;
        font-size: 1.45rem !important;
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
        transition: all 0.15s ease !important;
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
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02) !important;
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
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.02) !important;
    }

    /* Streamlit Status / Alert Boxes */
    [data-testid="stAlert"] {
        border-radius: 8px !important;
        font-size: 0.9rem !important;
    }
</style>
""", unsafe_allow_html=True)
import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 45%, #312E81 100%) !important;
                background-attachment: fixed !important;
                color: #ffffff !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.08) 0%, transparent 40%),
                            radial-gradient(circle at 90% 80%, rgba(244, 63, 94, 0.06) 0%, transparent 40%),
                            #F8FAFC !important;
                background-attachment: fixed !important;
                color: #0F172A !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

            html, body, p, div, label, span {
                font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
            }

            h1, h2, h3, h4, h5, h6 {
                font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 800 !important;
                letter-spacing: -0.02em !important;
                color: #0F172A !important;
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
                padding-top: 1.8rem !important;
                padding-bottom: 2.5rem !important;
                max-width: 1120px !important;
            }

            /* Bespoke High-Contrast Labels */
            label, label p, label span, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {
                color: #0F172A !important;
                font-weight: 700 !important;
                font-size: 0.95rem !important;
                letter-spacing: 0.01em !important;
                margin-bottom: 6px !important;
            }

            /* Text Inputs & Area Styling */
            .stTextInput input, .stNumberInput input, .stTextArea textarea {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border-radius: 16px !important;
                border: 2px solid rgba(99, 102, 241, 0.25) !important;
                padding: 12px 16px !important;
                font-size: 1rem !important;
                font-weight: 500 !important;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02) !important;
                transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
            .stTextInput input:focus, .stTextArea textarea:focus {
                border-color: #6366F1 !important;
                box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15) !important;
            }
            .stTextInput input::placeholder, .stTextArea textarea::placeholder {
                color: #94A3B8 !important;
            }

            /* Selectbox Bespoke Container */
            div[data-baseweb="select"] > div {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border-radius: 16px !important;
                border: 2px solid rgba(99, 102, 241, 0.25) !important;
                min-height: 50px !important;
                padding-left: 8px !important;
                box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02) !important;
                transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
            }
            div[data-baseweb="select"] span, div[data-baseweb="select"] div {
                color: #0F172A !important;
                font-size: 0.98rem !important;
                font-weight: 600 !important;
            }

            /* Dropdown Popover Menu */
            div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
                background-color: #FFFFFF !important;
                border-radius: 16px !important;
                border: 1px solid rgba(99, 102, 241, 0.2) !important;
                box-shadow: 0 20px 40px -10px rgba(15, 23, 42, 0.18) !important;
                padding: 6px !important;
            }
            li[role="option"] {
                color: #0F172A !important;
                background-color: #FFFFFF !important;
                font-weight: 600 !important;
                border-radius: 10px !important;
                padding: 10px 14px !important;
                margin-bottom: 2px !important;
            }
            li[role="option"]:hover, li[aria-selected="true"] {
                background: linear-gradient(135deg, rgba(99, 102, 241, 0.12) 0%, rgba(79, 70, 229, 0.08) 100%) !important;
                color: #4F46E5 !important;
            }

            /* File Uploader Container */
            [data-testid="stFileUploader"] {
                background: rgba(255, 255, 255, 0.9) !important;
                border-radius: 20px !important;
                border: 2px dashed rgba(99, 102, 241, 0.35) !important;
                padding: 1.4rem !important;
                box-shadow: 0 4px 12px rgba(99, 102, 241, 0.05) !important;
            }
            [data-testid="stFileUploader"] * {
                color: #0F172A !important;
            }

            /* Bespoke Master Button Base */
            .stButton > button {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 700 !important;
                border-radius: 9999px !important;
                padding: 13px 28px !important;
                min-height: 52px !important;
                border: none !important;
                transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
                font-size: 1rem !important;
                letter-spacing: 0.01em !important;
                display: inline-flex !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 10px !important;
                cursor: pointer !important;
            }
            .stButton > button:hover {
                transform: translateY(-3px) scale(1.015) !important;
                box-shadow: 0 12px 25px -5px rgba(79, 70, 229, 0.3) !important;
            }
            .stButton > button:active {
                transform: translateY(-1px) scale(0.99) !important;
            }

            /* Primary Button (Royal Indigo Gradient) */
            .stButton > button[kind="primary"],
            .stButton > button[data-testid="stBaseButton-primary"] {
                background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%) !important;
                color: #FFFFFF !important;
                box-shadow: 0 8px 20px -4px rgba(79, 70, 229, 0.4) !important;
                border: none !important;
            }
            .stButton > button[kind="primary"] *,
            .stButton > button[data-testid="stBaseButton-primary"] * {
                color: #FFFFFF !important;
            }

            /* Secondary Button (Warm Rose Coral Gradient) */
            .stButton > button[kind="secondary"],
            .stButton > button[data-testid="stBaseButton-secondary"] {
                background: linear-gradient(135deg, #F43F5E 0%, #FB7185 100%) !important;
                color: #FFFFFF !important;
                box-shadow: 0 8px 20px -4px rgba(244, 63, 94, 0.35) !important;
                border: none !important;
            }
            .stButton > button[kind="secondary"] *,
            .stButton > button[data-testid="stBaseButton-secondary"] * {
                color: #FFFFFF !important;
            }

            /* Tertiary Button (Artisanal Frosted Card Button) */
            .stButton > button[kind="tertiary"],
            .stButton > button[data-testid="stBaseButton-tertiary"] {
                background: #FFFFFF !important;
                color: #0F172A !important;
                border: 1.5px solid #E2E8F0 !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
            }
            .stButton > button[kind="tertiary"]:hover {
                border-color: #6366F1 !important;
                background: #F8FAFC !important;
                box-shadow: 0 8px 20px rgba(99, 102, 241, 0.15) !important;
            }
            .stButton > button[kind="tertiary"] *,
            .stButton > button[data-testid="stBaseButton-tertiary"] * {
                color: #0F172A !important;
            }

            /* Disabled Button State */
            .stButton > button:disabled {
                opacity: 0.5 !important;
                cursor: not-allowed !important;
                transform: none !important;
                box-shadow: none !important;
            }

            /* Cards & Containers (Glassmorphism Elevated Card) */
            [data-testid="stVerticalBlockBorderWrapper"] {
                background: rgba(255, 255, 255, 0.95) !important;
                backdrop-filter: blur(16px) !important;
                border-radius: 28px !important;
                padding: 2.4rem !important;
                border: 1px solid rgba(99, 102, 241, 0.15) !important;
                box-shadow: 0 16px 40px -10px rgba(79, 70, 229, 0.1), 0 4px 16px rgba(0, 0, 0, 0.03) !important;
            }

            /* --- DIALOG & MODAL CRAFTED GLASS DESIGN --- */
            div[data-baseweb="modal"] {
                background-color: rgba(15, 23, 42, 0.75) !important;
                backdrop-filter: blur(8px) !important;
            }

            div[data-baseweb="modal"] > div,
            div[role="dialog"],
            [data-testid="stModal"] > div {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border-radius: 28px !important;
                border: 2px solid rgba(99, 102, 241, 0.2) !important;
                box-shadow: 0 30px 70px -10px rgba(15, 23, 42, 0.45) !important;
                padding: 2rem !important;
                overflow: visible !important;
            }

            /* Dialog Title Header Fix */
            [data-testid="stDialogHeader"],
            div[role="dialog"] header,
            div[data-baseweb="modal"] header {
                padding-top: 0.2rem !important;
                margin-bottom: 0.8rem !important;
            }

            [data-testid="stDialogHeader"] h2,
            div[role="dialog"] h2,
            div[data-baseweb="modal"] h2,
            [data-testid="stDialog"] h2 {
                color: #0F172A !important;
                font-family: 'Outfit', sans-serif !important;
                font-size: 1.55rem !important;
                font-weight: 800 !important;
                margin: 0 !important;
                line-height: 1.25 !important;
            }

            /* High Contrast Body Text in Modals (EXCEPT inside buttons) */
            div[role="dialog"] h1, div[role="dialog"] h3, div[role="dialog"] h4, div[role="dialog"] h5, div[role="dialog"] h6,
            div[data-baseweb="modal"] h1, div[data-baseweb="modal"] h3, div[data-baseweb="modal"] h4, div[data-baseweb="modal"] h5, div[data-baseweb="modal"] h6 {
                color: #0F172A !important;
            }

            div[role="dialog"] p:not(.stButton *), 
            div[role="dialog"] span:not(.stButton *), 
            div[role="dialog"] label, 
            div[data-baseweb="modal"] p:not(.stButton *), 
            div[data-baseweb="modal"] span:not(.stButton *), 
            div[data-baseweb="modal"] label,
            [data-testid="stDialog"] p:not(.stButton *),
            [data-testid="stDialog"] label {
                color: #1E293B !important;
            }

            /* Modal Close Button */
            div[data-baseweb="modal"] button[aria-label="Close"],
            div[role="dialog"] button[aria-label="Close"],
            [data-testid="stDialog"] button[aria-label="Close"] {
                color: #0F172A !important;
                background-color: #F1F5F9 !important;
                border-radius: 50% !important;
                transition: transform 0.15s ease !important;
            }
            div[data-baseweb="modal"] button[aria-label="Close"]:hover {
                transform: scale(1.1) rotate(90deg) !important;
                background-color: #E2E8F0 !important;
            }
            div[data-baseweb="modal"] button[aria-label="Close"] svg,
            div[role="dialog"] button[aria-label="Close"] svg {
                fill: #0F172A !important;
                stroke: #0F172A !important;
            }

            /* Dataframe Table Styling */
            [data-testid="stDataFrame"] {
                background-color: #FFFFFF !important;
                border-radius: 16px !important;
                border: 1px solid #E2E8F0 !important;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02) !important;
            }

            /* Code Blocks */
            div[role="dialog"] [data-testid="stCodeBlock"],
            div[data-baseweb="modal"] [data-testid="stCodeBlock"],
            [data-testid="stDialog"] [data-testid="stCodeBlock"] {
                background-color: #F8FAFC !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 14px !important;
            }
            div[role="dialog"] [data-testid="stCodeBlock"] code,
            div[data-baseweb="modal"] [data-testid="stCodeBlock"] code,
            [data-testid="stDialog"] [data-testid="stCodeBlock"] code {
                color: #0F172A !important;
                font-family: monospace !important;
                font-weight: 600 !important;
            }
        </style>
    """, unsafe_allow_html=True)
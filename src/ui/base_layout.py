import streamlit as st

def get_current_theme() -> str:
    """Returns 'light' or 'dark' (defaults to 'light')."""
    if "app_theme" not in st.session_state:
        st.session_state["app_theme"] = "light"
    return st.session_state["app_theme"]

def render_theme_toggle(key: str = "theme_toggle_btn"):
    """Renders a clean Light/Dark mode toggle button."""
    theme = get_current_theme()
    if theme == "light":
        btn_label = "🌙 Dark Mode"
    else:
        btn_label = "☀️ Light Mode"
    
    if st.button(btn_label, key=key, type="secondary", use_container_width=True):
        st.session_state["app_theme"] = "dark" if theme == "light" else "light"
        st.rerun()


def style_background_home():
    theme = get_current_theme()
    if theme == "dark":
        st.markdown("""
<style>
    .stApp {
        background-color: #0B0F19 !important;
        background-image: none !important;
        color: #F8FAFC !important;
    }
</style>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC !important;
        background-image: none !important;
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)


def style_background_dashboard():
    theme = get_current_theme()
    if theme == "dark":
        st.markdown("""
<style>
    .stApp {
        background-color: #0B0F19 !important;
        background-image: none !important;
        color: #F8FAFC !important;
    }
</style>
""", unsafe_allow_html=True)
    else:
        st.markdown("""
<style>
    .stApp {
        background-color: #F8FAFC !important;
        background-image: none !important;
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)


def style_base_layout():
    theme = get_current_theme()
    is_dark = (theme == "dark")

    if is_dark:
        # HIGH-CONTRAST MODERN DARK MODE
        bg_main = "#0B0F19"
        bg_card = "#1E293B"
        border_card = "#334155"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        text_muted = "#64748B"
        
        btn_pri_bg = "#2563EB"
        btn_pri_border = "#3B82F6"
        btn_pri_text = "#FFFFFF"
        
        btn_sec_bg = "#1E293B"
        btn_sec_border = "#475569"
        btn_sec_text = "#F8FAFC"
        
        btn_dis_bg = "#1E293B"
        btn_dis_border = "#334155"
        btn_dis_text = "#64748B"
        
        input_bg = "#0F172A"
        input_border = "#475569"
        input_focus = "#3B82F6"
        input_text = "#F8FAFC"
        
        modal_bg = "#111827"
        modal_border = "#374151"
    else:
        # HIGH-CONTRAST CRISP LIGHT MODE (NO washed-out text, NO dots)
        bg_main = "#F8FAFC"
        bg_card = "#FFFFFF"
        border_card = "#CBD5E1"
        text_primary = "#0F172A"
        text_secondary = "#334155"
        text_muted = "#475569"
        
        btn_pri_bg = "#0F172A"
        btn_pri_border = "#020617"
        btn_pri_text = "#FFFFFF"
        
        btn_sec_bg = "#FFFFFF"
        btn_sec_border = "#64748B"
        btn_sec_text = "#0F172A"
        
        btn_dis_bg = "#E2E8F0"
        btn_dis_border = "#CBD5E1"
        btn_dis_text = "#475569"
        
        input_bg = "#FFFFFF"
        input_border = "#64748B"
        input_focus = "#1E3A8A"
        input_text = "#0F172A"
        
        modal_bg = "#FFFFFF"
        modal_border = "#CBD5E1"

    st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [data-testid="stAppViewContainer"] {{
        background-color: {bg_main} !important;
        font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, sans-serif !important;
        color: {text_primary} !important;
    }}

    p, div, label, span {{
        color: {text_primary};
    }}

    h1, h2, h3, h4, h5, h6 {{
        font-family: 'Plus Jakarta Sans', 'Inter', sans-serif !important;
        font-weight: 700 !important;
        color: {text_primary} !important;
        letter-spacing: -0.015em !important;
    }}

    /* Minimal Clean Scrollbar */
    ::-webkit-scrollbar {{
        width: 6px;
        height: 6px;
    }}
    ::-webkit-scrollbar-track {{
        background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
        background: {border_card};
        border-radius: 4px;
    }}

    /* Protect Streamlit Material Icons */
    [data-testid="stIconMaterial"], [data-testid="stIconMaterial"] * {{
        font-family: 'Material Symbols Rounded', 'Material Symbols Outlined' !important;
        font-style: normal !important;
        font-weight: normal !important;
        display: inline-block !important;
    }}

    /* Hide Default Streamlit Header & Chrome */
    #MainMenu, footer, header, [data-testid="stHeader"] {{
        visibility: hidden !important;
        height: 0 !important;
    }}

    .block-container {{
        padding-top: 1.2rem !important;
        padding-bottom: 3rem !important;
        max-width: 1120px !important;
    }}

    /* Form Labels - High Contrast & Visible */
    label, label p, label span, [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p {{
        color: {text_primary} !important;
        font-weight: 700 !important;
        font-size: 0.88rem !important;
        letter-spacing: 0.01em !important;
        margin-bottom: 5px !important;
    }}

    /* High Visibility Form Inputs */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {{
        background-color: {input_bg} !important;
        color: {input_text} !important;
        border-radius: 8px !important;
        border: 1.5px solid {input_border} !important;
        padding: 10px 14px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        box-shadow: none !important;
        transition: border-color 0.15s ease !important;
    }}
    .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {{
        border-color: {input_focus} !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2) !important;
        outline: none !important;
    }}
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
        color: {text_muted} !important;
        font-weight: 400 !important;
    }}

    /* Selectbox Input */
    div[data-baseweb="select"] > div {{
        background-color: {input_bg} !important;
        color: {input_text} !important;
        border-radius: 8px !important;
        border: 1.5px solid {input_border} !important;
        min-height: 42px !important;
        padding-left: 8px !important;
        transition: border-color 0.15s ease !important;
    }}
    div[data-baseweb="select"]:focus-within > div {{
        border-color: {input_focus} !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2) !important;
    }}
    div[data-baseweb="select"] span, div[data-baseweb="select"] div {{
        color: {input_text} !important;
        font-size: 0.92rem !important;
        font-weight: 600 !important;
    }}

    /* Dropdown Menus */
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {{
        background-color: {modal_bg} !important;
        border-radius: 10px !important;
        border: 1.5px solid {modal_border} !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2) !important;
        padding: 6px !important;
    }}
    li[role="option"] {{
        color: {text_primary} !important;
        background-color: {modal_bg} !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
        padding: 9px 12px !important;
        margin-bottom: 2px !important;
    }}
    li[role="option"]:hover, li[aria-selected="true"] {{
        background-color: {input_focus} !important;
        color: #FFFFFF !important;
    }}

    /* HIGH-CONTRAST BUTTON SYSTEM */
    .stButton > button {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        padding: 9px 18px !important;
        min-height: 42px !important;
        font-size: 0.92rem !important;
        letter-spacing: 0.01em !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 8px !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-1px) !important;
    }}
    .stButton > button:active {{
        transform: translateY(0) !important;
    }}

    /* Primary Button: Solid & High Contrast */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {{
        background-color: {btn_pri_bg} !important;
        color: {btn_pri_text} !important;
        border: 1.5px solid {btn_pri_border} !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.15) !important;
    }}
    .stButton > button[kind="primary"] *,
    .stButton > button[data-testid="stBaseButton-primary"] * {{
        color: {btn_pri_text} !important;
        font-weight: 700 !important;
    }}

    /* Secondary Button: Sharp, Clear Borders */
    .stButton > button[kind="secondary"],
    .stButton > button[data-testid="stBaseButton-secondary"] {{
        background-color: {btn_sec_bg} !important;
        color: {btn_sec_text} !important;
        border: 1.5px solid {btn_sec_border} !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    }}
    .stButton > button[kind="secondary"] *,
    .stButton > button[data-testid="stBaseButton-secondary"] * {{
        color: {btn_sec_text} !important;
        font-weight: 600 !important;
    }}

    /* Tertiary Button */
    .stButton > button[kind="tertiary"],
    .stButton > button[data-testid="stBaseButton-tertiary"] {{
        background-color: {btn_sec_bg} !important;
        color: {btn_sec_text} !important;
        border: 1.5px solid {btn_sec_border} !important;
    }}
    .stButton > button[kind="tertiary"] *,
    .stButton > button[data-testid="stBaseButton-tertiary"] * {{
        color: {btn_sec_text} !important;
        font-weight: 600 !important;
    }}

    /* DISABLED BUTTONS: ALWAYS 100% VISIBLE (NOT FADED OUT) */
    .stButton > button:disabled,
    .stButton > button[disabled] {{
        background-color: {btn_dis_bg} !important;
        color: {btn_dis_text} !important;
        border: 1.5px solid {btn_dis_border} !important;
        opacity: 1 !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
    }}
    .stButton > button:disabled *,
    .stButton > button[disabled] * {{
        color: {btn_dis_text} !important;
        font-weight: 600 !important;
    }}

    /* Card Containers */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {bg_card} !important;
        border-radius: 10px !important;
        padding: 1.5rem !important;
        border: 1.5px solid {border_card} !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
    }}

    /* Dialogs & Modals */
    div[data-baseweb="modal"] {{
        background-color: rgba(0, 0, 0, 0.65) !important;
        backdrop-filter: blur(4px) !important;
    }}
    div[data-baseweb="modal"] > div,
    div[role="dialog"],
    [data-testid="stModal"] > div {{
        background-color: {modal_bg} !important;
        color: {text_primary} !important;
        border-radius: 12px !important;
        border: 1.5px solid {modal_border} !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3) !important;
        padding: 1.8rem !important;
    }}
    [data-testid="stDialogHeader"] h2,
    div[role="dialog"] h2,
    div[data-baseweb="modal"] h2,
    [data-testid="stDialog"] h2 {{
        color: {text_primary} !important;
        font-weight: 800 !important;
        font-size: 1.4rem !important;
    }}

    /* Streamlit Code Blocks: High Contrast */
    [data-testid="stCodeBlock"], pre, code {{
        background-color: {input_bg} !important;
        color: {text_primary} !important;
        border: 1px solid {border_card} !important;
        border-radius: 6px !important;
    }}

    /* Dividers */
    hr {{
        border-color: {border_card} !important;
        margin: 1.25rem 0 !important;
    }}

    /* Table & DataFrame */
    [data-testid="stDataFrame"] {{
        background-color: {bg_card} !important;
        border-radius: 8px !important;
        border: 1.5px solid {border_card} !important;
    }}

    /* Force all links inside share buttons to stay bright white */
    .snap-share-link, .snap-share-link * {{
        color: #FFFFFF !important;
        text-decoration: none !important;
    }}
</style>
""", unsafe_allow_html=True)
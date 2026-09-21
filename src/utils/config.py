import os
import streamlit as st

def get_app_live_url() -> str:
    """
    Returns the real live deployment URL of the application.
    Supports override via streamlit secrets or environment variable.
    """
    if "APP_LIVE_URL" in st.secrets:
        url = str(st.secrets["APP_LIVE_URL"]).strip()
    elif "APP_URL" in st.secrets:
        url = str(st.secrets["APP_URL"]).strip()
    elif os.environ.get("APP_LIVE_URL"):
        url = os.environ.get("APP_LIVE_URL").strip()
    else:
        url = "https://aiattendancesystemgit-h.streamlit.app"
    
    # Ensure scheme
    if not url.startswith("http://") and not url.startswith("https://"):
        url = f"https://{url}"
    return url.rstrip("/")

def get_app_domain() -> str:
    """
    Returns the clean domain name (without https:// and trailing slash).
    """
    url = get_app_live_url()
    return url.replace("https://", "").replace("http://", "").split("/")[0]

APP_LIVE_URL = get_app_live_url()
APP_DOMAIN = get_app_domain()

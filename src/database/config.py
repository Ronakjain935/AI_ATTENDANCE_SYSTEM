import streamlit as st
from supabase import create_client, Client

def _init_supabase() -> Client:
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        return create_client(url, key)
    except KeyError as e:
        st.error(
            f"❌ **Missing Secret in Streamlit Cloud: {e}**\n\n"
            "Your app requires Supabase credentials to run.\n\n"
            "**How to fix this in Streamlit Cloud:**\n"
            "1. Open your app on Streamlit Cloud.\n"
            "2. Click **Manage app** (bottom-right corner) ⚙️ -> **Settings** -> **Secrets**.\n"
            "3. Add your secrets in TOML format:\n"
            "```toml\n"
            'SUPABASE_URL = "https://your-project.supabase.co"\n'
            'SUPABASE_KEY = "your-anon-key"\n'
            "```\n"
            "4. Click **Save**."
        )
        st.stop()
    except Exception as e:
        st.error(f"❌ **Supabase Connection Error:** {e}")
        st.stop()

supabase: Client = _init_supabase()
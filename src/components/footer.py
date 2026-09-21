import streamlit as st
import textwrap

def footer_home():
    html = textwrap.dedent("""\
<div style="margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid #E2E8F0; text-align: center;">
<p style="color: #64748B; font-size: 0.85rem; font-weight: 500; margin: 0 0 4px 0;">
SnapClass — AI-Assisted Attendance Management
</p>
<p style="color: #94A3B8; font-size: 0.78rem; margin: 0;">
Built for modern educators and students
</p>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)


def footer_dashboard():
    html = textwrap.dedent("""\
<div style="margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid #E2E8F0; text-align: center;">
<p style="color: #64748B; font-size: 0.85rem; font-weight: 500; margin: 0 0 4px 0;">
SnapClass Platform
</p>
<p style="color: #94A3B8; font-size: 0.78rem; margin: 0;">
Encrypted & Verified Class Records
</p>
</div>\
""")
    st.markdown(html, unsafe_allow_html=True)

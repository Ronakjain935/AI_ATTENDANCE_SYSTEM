import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid #cbd5e1; margin-bottom:20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h3 style="margin:0; color: #1e293b; font-size: 1.5rem; font-weight: 700;">{name}</h3>
            <p style="color:#64748b; margin:10px 0;">Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 8px; border-radius:6px; font-weight:600;">{code}</span> | Section : <strong style="color:#1e293b;">{section}</strong></p>
    """
    
    if stats:
        html += """
            <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top: 12px;">
        """
        for icon, label, value in stats:
            html += f'''
                <div style="background: #EB459E12; padding:6px 14px; border-radius:12px; font-size:0.9rem; color:#1e293b;">
                    {icon} <b>{value}</b> {label}
                </div>
            '''
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

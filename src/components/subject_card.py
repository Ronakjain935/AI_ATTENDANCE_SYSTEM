import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: #FFFFFF; border-left: 6px solid #4F46E5; padding: 24px; border-radius: 24px; border: 1px solid rgba(99, 102, 241, 0.18); margin-bottom: 18px; box-shadow: 0 12px 30px -8px rgba(79, 70, 229, 0.1), 0 4px 12px rgba(0,0,0,0.02); transition: all 0.25s ease;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; flex-wrap: wrap;">
                <div>
                    <h3 style="margin: 0; color: #0F172A; font-size: 1.45rem; font-weight: 800; letter-spacing: -0.02em;">{name}</h3>
                    <div style="display: flex; align-items: center; gap: 10px; margin-top: 8px; flex-wrap: wrap;">
                        <span style="background: rgba(79, 70, 229, 0.1); color: #4F46E5; padding: 4px 12px; border-radius: 10px; font-weight: 700; font-size: 0.88rem; border: 1px solid rgba(79, 70, 229, 0.15);">
                            Code: {code}
                        </span>
                        <span style="background: #F1F5F9; color: #475569; padding: 4px 12px; border-radius: 10px; font-weight: 600; font-size: 0.88rem;">
                            Section {section}
                        </span>
                    </div>
                </div>
            </div>
    """
    
    if stats:
        html += """
            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; padding-top: 14px; border-top: 1px dashed #E2E8F0;">
        """
        for icon, label, value in stats:
            html += f'''
                <div style="background: rgba(244, 63, 94, 0.08); border: 1px solid rgba(244, 63, 94, 0.12); padding: 6px 14px; border-radius: 12px; font-size: 0.88rem; color: #0F172A; font-weight: 600;">
                    {icon} <b style="color: #F43F5E;">{value}</b> {label}
                </div>
            '''
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

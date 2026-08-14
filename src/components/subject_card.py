import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: #FFFFFF; border-left: 6px solid #4F46E5; padding: 24px; border-radius: 24px; border: 1px solid rgba(99, 102, 241, 0.18); margin-bottom: 18px; box-shadow: 0 12px 30px -8px rgba(79, 70, 229, 0.12), 0 4px 12px rgba(0,0,0,0.02); transition: all 0.25s ease;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; flex-wrap: wrap;">
                <div>
                    <h3 style="margin: 0; color: #0F172A; font-size: 1.45rem; font-weight: 800; letter-spacing: -0.02em;">{name}</h3>
                    <div style="display: flex; align-items: center; gap: 10px; margin-top: 10px; flex-wrap: wrap;">
                        <span style="background: rgba(79, 70, 229, 0.1); color: #4F46E5; padding: 5px 14px; border-radius: 12px; font-weight: 700; font-size: 0.88rem; border: 1px solid rgba(79, 70, 229, 0.18);">
                            Code: {code}
                        </span>
                        <span style="background: #F1F5F9; color: #475569; padding: 5px 14px; border-radius: 12px; font-weight: 600; font-size: 0.88rem; border: 1px solid #E2E8F0;">
                            Section {section}
                        </span>
                    </div>
                </div>
            </div>
    """
    
    if stats:
        html += """
            <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 18px; padding-top: 14px; border-top: 1px dashed #E2E8F0;">
        """
        for icon, label, value in stats:
            html += f'''
                <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.18); padding: 6px 14px; border-radius: 14px; font-size: 0.88rem; color: #0F172A; font-weight: 600; display: inline-flex; align-items: center; gap: 6px;">
                    <span>{icon}</span> <b style="color: #059669; font-size: 0.95rem;">{value}</b> <span style="color: #475569;">{label}</span>
                </div>
            '''
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

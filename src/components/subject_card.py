import streamlit as st
import textwrap

def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        stat_items = []
        for icon, label, value in stats:
            stat_items.append(
                f'<div style="display: inline-flex; align-items: center; gap: 6px; background: #F8FAFC; border: 1px solid #E2E8F0; padding: 5px 12px; border-radius: 8px; font-size: 0.82rem;">'
                f'<span style="font-size: 0.95rem;">{icon}</span>'
                f'<span style="color: #64748B; font-weight: 500;">{label}</span>'
                f'<strong style="color: #0F172A; font-weight: 700; font-size: 0.9rem;">{value}</strong>'
                f'</div>'
            )
        stats_chips = "".join(stat_items)
        stats_html = (
            f'<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; padding-top: 12px; border-top: 1px solid #F1F5F9;">'
            f'{stats_chips}'
            f'</div>'
        )

    card_html = textwrap.dedent(f"""\
<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-left: 4px solid #4F46E5; border-radius: 12px; padding: 18px 20px; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04), 0 1px 2px rgba(0, 0, 0, 0.02); transition: border-color 0.15s ease, box-shadow 0.15s ease;">
<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; flex-wrap: wrap;">
<div>
<h3 style="margin: 0 0 6px 0; color: #0F172A; font-size: 1.18rem; font-weight: 700; letter-spacing: -0.015em; line-height: 1.3;">{name}</h3>
<div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
<span style="background: #EEF2FF; color: #4338CA; border: 1px solid #E0E7FF; padding: 2px 10px; border-radius: 6px; font-weight: 600; font-size: 0.8rem; letter-spacing: 0.02em;">
Code: {code}
</span>
<span style="background: #F1F5F9; color: #475569; border: 1px solid #E2E8F0; padding: 2px 10px; border-radius: 6px; font-weight: 500; font-size: 0.8rem;">
Section {section}
</span>
</div>
</div>
</div>
{stats_html}
</div>\
""")

    st.markdown(card_html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

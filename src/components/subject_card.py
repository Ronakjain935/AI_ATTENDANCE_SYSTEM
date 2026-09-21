import streamlit as st
import textwrap

def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        stat_items = []
        for icon, label, value in stats:
            stat_items.append(
                f'<div style="display: inline-flex; align-items: center; gap: 7px; background: #F8FAFC; border: 1px solid #E2E8F0; padding: 6px 14px; border-radius: 8px; box-shadow: 0 1px 2px rgba(0,0,0,0.02);">'
                f'<span style="font-size: 1rem;">{icon}</span>'
                f'<span style="color: #64748B; font-size: 0.82rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em;">{label}:</span>'
                f'<strong style="color: #0F172A; font-weight: 800; font-size: 0.95rem;">{value}</strong>'
                f'</div>'
            )
        stats_chips = "".join(stat_items)
        stats_html = (
            f'<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 14px; padding-top: 12px; border-top: 1px solid #F1F5F9;">'
            f'{stats_chips}'
            f'</div>'
        )

    card_html = textwrap.dedent(f"""\
<div style="background: #FFFFFF; border: 1px solid rgba(226, 232, 240, 0.9); border-left: 5px solid #4F46E5; border-radius: 14px; padding: 20px 22px; margin-bottom: 16px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -2px rgba(0, 0, 0, 0.02);">
<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; flex-wrap: wrap;">
<div style="flex: 1;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px; flex-wrap: wrap;">
<span style="font-family: monospace; background: #EEF2FF; color: #4338CA; border: 1px solid #E0E7FF; padding: 2px 8px; border-radius: 6px; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.03em;">
{code}
</span>
<span style="background: #F8FAFC; color: #64748B; border: 1px solid #E2E8F0; padding: 2px 8px; border-radius: 6px; font-weight: 600; font-size: 0.78rem;">
Section {section}
</span>
</div>
<h3 style="margin: 0; color: #0F172A; font-size: 1.28rem; font-weight: 700; letter-spacing: -0.02em; line-height: 1.3;">
{name}
</h3>
</div>
</div>
{stats_html}
</div>\
""")

    st.markdown(card_html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

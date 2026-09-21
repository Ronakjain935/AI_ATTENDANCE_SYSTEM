import streamlit as st
import textwrap

def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        stat_items = []
        for icon, label, value in stats:
            stat_items.append(
                f'<div style="display: inline-flex; align-items: center; gap: 7px; background: #F8FAFC; border: 1px solid #CBD5E1; padding: 6px 12px; border-radius: 6px; box-shadow: 0 1px 2px rgba(15, 23, 42, 0.02);">'
                f'<span style="font-size: 0.95rem;">{icon}</span>'
                f'<span style="color: #475569; font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em;">{label}:</span>'
                f'<strong style="color: #0F172A; font-weight: 700; font-size: 0.92rem;">{value}</strong>'
                f'</div>'
            )
        stats_chips = "".join(stat_items)
        stats_html = (
            f'<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; padding-top: 12px; border-top: 1px solid #E2E8F0;">'
            f'{stats_chips}'
            f'</div>'
        )

    card_html = textwrap.dedent(f"""\
<div style="background: #FFFFFF; border: 1px solid #CBD5E1; border-left: 4px solid #1E3A8A; border-radius: 10px; padding: 18px 20px; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04), 0 4px 8px -2px rgba(15, 23, 42, 0.02);">
<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; flex-wrap: wrap;">
<div style="flex: 1;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px; flex-wrap: wrap;">
<span style="font-family: monospace; background: #0F172A; color: #F8FAFC; border: 1px solid #1E293B; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.78rem; letter-spacing: 0.04em;">
{code}
</span>
<span style="background: #F8FAFC; color: #475569; border: 1px solid #CBD5E1; padding: 2px 8px; border-radius: 4px; font-weight: 600; font-size: 0.76rem; text-transform: uppercase; letter-spacing: 0.03em;">
Section {section}
</span>
</div>
<h3 style="margin: 0; color: #0F172A; font-family: 'Lora', Georgia, serif; font-size: 1.25rem; font-weight: 700; letter-spacing: -0.01em; line-height: 1.35;">
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

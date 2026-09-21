import streamlit as st
import textwrap
from src.ui.base_layout import get_current_theme

def subject_card(name, code, section, stats=None, footer_callback=None):
    theme = get_current_theme()
    is_dark = (theme == "dark")

    card_bg = "#1E293B" if is_dark else "#FFFFFF"
    card_border = "#334155" if is_dark else "#CBD5E1"
    chip_bg = "#0B0F19" if is_dark else "#F1F5F9"
    chip_border = "#334155" if is_dark else "#CBD5E1"
    title_color = "#FFFFFF" if is_dark else "#0F172A"
    sub_color = "#94A3B8" if is_dark else "#475569"
    value_color = "#38BDF8" if is_dark else "#0F172A"
    badge_bg = "#2563EB" if is_dark else "#0F172A"
    badge_text = "#FFFFFF"

    stats_html = ""
    if stats:
        stat_items = []
        for icon, label, value in stats:
            stat_items.append(
                f'<div style="display: inline-flex; align-items: center; gap: 7px; background: {chip_bg}; border: 1.5px solid {chip_border}; padding: 6px 12px; border-radius: 6px;">'
                f'<span style="font-size: 0.95rem;">{icon}</span>'
                f'<span style="color: {sub_color}; font-size: 0.80rem; font-weight: 700; text-transform: uppercase;">{label}:</span>'
                f'<strong style="color: {value_color}; font-weight: 800; font-size: 0.92rem;">{value}</strong>'
                f'</div>'
            )
        stats_chips = "".join(stat_items)
        stats_html = (
            f'<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; padding-top: 12px; border-top: 1.5px solid {chip_border};">'
            f'{stats_chips}'
            f'</div>'
        )

    card_html = textwrap.dedent(f"""\
<div style="background: {card_bg}; border: 1.5px solid {card_border}; border-left: 5px solid #2563EB; border-radius: 10px; padding: 18px 20px; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0,0,0,0.06);">
<div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; flex-wrap: wrap;">
<div style="flex: 1;">
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px; flex-wrap: wrap;">
<span style="font-family: monospace; background: {badge_bg}; color: {badge_text}; padding: 3px 9px; border-radius: 4px; font-weight: 800; font-size: 0.80rem; letter-spacing: 0.04em;">
{code}
</span>
<span style="background: {chip_bg}; color: {sub_color}; border: 1.5px solid {chip_border}; padding: 3px 9px; border-radius: 4px; font-weight: 700; font-size: 0.78rem; text-transform: uppercase;">
Section {section}
</span>
</div>
<h3 style="margin: 0; color: {title_color}; font-size: 1.3rem; font-weight: 800; line-height: 1.3;">
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

import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None, progress_pct=None, tile_index=1):
    """
    Renders an elegant Subject Tile with index number (01, 02..),
    progress bar, session ratio, and action buttons.
    """
    idx_str = f"{tile_index:02d}" if isinstance(tile_index, int) else str(tile_index)
    clean_sec = section if str(section).lower().startswith('section') else f'Section {section}'

    # Statistics string
    stats_text = ""
    if stats:
        parts = []
        for item in stats:
            if isinstance(item, (list, tuple)):
                if len(item) == 3:
                    _, label, val = item
                elif len(item) == 2:
                    label, val = item
                elif len(item) == 1:
                    label, val = "Stat", item[0]
                else:
                    label, val = "Stat", str(item)
                parts.append(f"<strong>{label}:</strong> {val}")
            elif isinstance(item, dict):
                label = item.get('label', 'Stat')
                val = item.get('value', item.get('val', ''))
                parts.append(f"<strong>{label}:</strong> {val}")
        stats_text = " &bull; ".join(parts)

    # Progress bar
    progress_html = ""
    if progress_pct is not None:
        pct_color = "#218739" if progress_pct >= 75 else ("#B7791F" if progress_pct >= 60 else "#C53030")
        progress_html = f"""<div style="margin: 10px 0 8px 0;">
<div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px;">
<span style="font-size: 1.5rem; font-weight: 800; color: {pct_color}; font-family: 'Plus Jakarta Sans', sans-serif;">{progress_pct}%</span>
<span style="font-size: 0.72rem; font-weight: 700; color: #667085; text-transform: uppercase;">ATTENDANCE STANDING</span>
</div>
<div style="height: 6px; width: 100%; background: #F0EFEA; border-radius: 999px; overflow: hidden;">
<div style="height: 100%; width: {min(max(progress_pct, 0), 100)}%; background: {pct_color}; border-radius: 999px;"></div>
</div>
</div>"""

    tile_html = f"""<div style="background: #FFFFFF; border: 1px solid #D9DEE7; border-radius: 12px; padding: 16px 18px; margin-bottom: 14px; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
<div style="display: flex; align-items: center; gap: 8px;">
<span style="font-family: monospace; background: #172B4D; color: #FFFFFF; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 0.76rem;">
{code}
</span>
<span style="background: #F7F6F2; color: #40566F; border: 1px solid #D9DEE7; padding: 2px 8px; border-radius: 4px; font-weight: 600; font-size: 0.74rem;">
{clean_sec}
</span>
</div>
<span style="font-family: monospace; font-size: 0.85rem; font-weight: 800; color: #667085; background: #F7F6F2; border: 1px solid #D9DEE7; padding: 2px 8px; border-radius: 4px;">
{idx_str}
</span>
</div>

<h3 style="font-size: 1.18rem; font-weight: 700; color: #172B4D; margin: 0 0 6px 0; line-height: 1.3;">
{name}
</h3>

{progress_html}

<div style="font-size: 0.78rem; color: #667085; margin-top: 8px; padding-top: 8px; border-top: 1px solid #F0EFEA;">
{stats_text}
</div>
</div>"""
    st.markdown(tile_html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

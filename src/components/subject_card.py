import streamlit as st 

def subject_card(name, code, section, stats=None, footer_callback=None): 
    html = f"""
<div style="background:white;border-left:8px solid #eb459e;padding:25px;border-radius:20px;border:1px solid black;margin-bottom:20px;">
<h3 class="subject-title" style="margin:0;color:#1e293b;font-size:1.5rem;">{name}</h3>
<p style="color:#64748b;margin:10px 0;">Code: <span style="background:#e0e3ff;color:#5865f2;padding:2px 8px;border-radius:5px;">{code}</span> | Section: {section}</p>"""

    if stats:
        stat_items = ""
        for icon, label, value in stats:
            stat_items += f'<div style="background:rgba(235,69,158,0.06);padding:5px 12px;border-radius:12px;font-size:0.9rem;">{icon} <b>{value}</b> {label}</div>'
        html += f'<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px;">{stat_items}</div>'

    html += "</div>"

    st.html(html)

    if footer_callback: 
        footer_callback()
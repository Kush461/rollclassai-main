import streamlit as st 
def style_background_home(): 
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&display=swap');
            .stApp {
                background: #5865f2 !important; 
            }
            .stApp div[data-testid="stColumn"] {
                background-color: #e0e3ff !important;
                padding: 1.5rem !important;
                border-radius: 4rem !important;
                max-width: 280px !important;
                margin: 0 auto !important;
            }
            .stApp div[data-testid="stColumn"] h2 {
                font-size: 1.6rem !important;
                white-space: nowrap !important;
                text-align: center !important;
                color: #000000 !important;
                font-family: 'Outfit', sans-serif !important;
            }
            .stApp div[data-testid="stColumn"] div[data-testid="stImage"] {
                display: flex !important;
                justify-content: center !important;
            }
            .stApp div[data-testid="stColumn"] button {
                width: fit-content !important;
            }
        </style>
    """, unsafe_allow_html=True) 
    
def style_background_dashboard(): 
    st.markdown("""
        <style>
            .stApp {
                background: #e0e3ff !important; 
            }
            .stApp h2 {
                color: #000000 !important;
                text-align: center !important;
            }
            .stApp div[data-testid="stAlert"] {
    text-align: center !important;
}
        </style>
    """, unsafe_allow_html=True) 
    
def style_base_layout(): 
    st.markdown("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@2024&display=swap" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap" rel="stylesheet">
        <style>
            .block-container {
                padding-top: 1.5rem !important;
            }
            h1, h2, h3, h4 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-variation-settings: 'YEAR' 2024 !important;
                line-height: 0.8 !important;
                margin-bottom: 0rem !important;
            }
            h1 {
                font-size: 3.5rem !important;
                white-space: nowrap !important;
            }
            h2 {
                font-size: 1.4rem !important;
                white-space: normal !important;
                word-break: break-word !important;
            }
            p {
                font-family: 'Outfit', sans-serif !important;
            }
            .subject-title {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 700 !important;
            }
            button {
                background: #5865f2 !important;
                border-radius: 1.5rem !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button[kind="secondary"] {
                background: #eb459e !important;
            }
            button[kind="tertiary"] {
                background-color: black !important;
            }
            button:hover {
                transform: scale(1.05);
            }
            button p {
                white-space: nowrap !important;
            }
            .stApp div[data-testid="stTextInput"] input {
                background-color: #ffffff !important;
                color: #000000 !important;
                border-radius: 0.75rem !important;
                border: 2px solid #5865f2 !important;
                caret-color: #000000 !important;
            }
            .stApp div[data-testid="stTextInput"] div {
                background-color: #ffffff !important;
                border-radius: 0.75rem !important;
            }
            .stApp div[data-testid="stTextInput"] label {
                color: #000000 !important;
            }
            .stApp div[data-testid="stTextInput"] button {
                background-color: #5865f2 !important;
                border-radius: 0.5rem !important;
                padding: 4px 8px !important;
                width: auto !important;
                min-width: unset !important;
            }
            div[data-testid="stVerticalBlockBorderWrapper"] button {
                width: 100% !important;
            }
            #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
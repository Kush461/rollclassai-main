import streamlit as st 

def footer_home(): 
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f""" 
            <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;
                margin-bottom:30px;margin-top:15px;">
                <p>Created by Kushagra with ❤️</p>
                </div>
                """,unsafe_allow_html=True) 
    
def footer_dashboard(): 
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f""" 
            <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;
                margin-bottom:30px;margin-top:15px;color:black;">
                <p>Created by Kushagra with ❤️</p>
                </div>
                """,unsafe_allow_html=True)
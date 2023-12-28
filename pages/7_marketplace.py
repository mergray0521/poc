import requests
import streamlit as st
import snowflake.connector

st.header("Token Marketplace")
css_code = """
    <style>
        .custom-container {
            border: 2px solid #1f618d;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 280px;
        }

        .custom-image {
            width: 80%;
            border-radius: 5px;
            height: 150px;
        }

        .custom-button {
            margin-top: 10px;
            border: 2px solid #429DF5;
        }
    </style>
"""

# Create 3 columns and two rows
c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3) 

with st.container(): 
    # c1, c2, c3 = st.columns(3)
    for col in [c1, c2, c3]: 
        if col == c1:
            with col:
                c1.markdown(css_code, unsafe_allow_html=True)
                html_code_token1 = """
                    <div class="custom-container">
                        <img src="https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true" alt="My Say Token" class="custom-image">
                        <p>1,000 points</p>
                        <button class="custom-button">Purchase My Say</button>
                    </div>
                """
                c1.markdown(html_code_token1, unsafe_allow_html=True)
        if col == c2:
            with col:        
                c2.markdown(css_code, unsafe_allow_html=True)
                html_code_token2 = """
                    <div class="custom-container">
                        <img src="https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(17).png?raw=true" alt="My Way Token" class="custom-image">
                        <p>2,000 points</p>
                        <button class="custom-button">Purchase My Way</button>
                    </div>
                """
                c2.markdown(html_code_token2, unsafe_allow_html=True)
        if col == c3:
            with col:  
                c3.markdown(css_code, unsafe_allow_html=True)
                html_code_token3 = """
                    <div class="custom-container">
                        <img src="https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(15).png?raw=true" alt="My Day Token" class="custom-image">
                        <p>3,000 points</p>
                        <button class="custom-button">Purchase My Day</button>
                    </div>
                """
                c3.markdown(html_code_token3, unsafe_allow_html=True)
                
with st.container(): 
    # c4, c5, c6 = st.columns(3)
    for col in [c4, c5, c6]: 
        if col == c4:
            with col:  
                c4.markdown(css_code, unsafe_allow_html=True)
                html_code_token4 = """
                    <div class="custom-container">
                        <img src="https://github.com/mergray0521/poc/blob/main/images/ticket.png?raw=true" alt="Minion Glasses" class="custom-image">
                        <p>4,000 points</p>
                        <button class="custom-button">Purchase Park Ticket</button>
                    </div>
                """
                c4.markdown(html_code_token4, unsafe_allow_html=True)
        if col == c5:
            with col: 
                c5.markdown(css_code, unsafe_allow_html=True)
                html_code_token5 = """
                    <div class="custom-container">
                        <img src="https://cdn.dribbble.com/users/1061278/screenshots/14605165/media/f27c0bfd48d70f3aa755d3617b287f3e.png?resize=400x300&vertical=center" alt="Dragon" class="custom-image">
                        <p>4,000 points</p>
                        <button class="custom-button">Purchase Dragon</button>
                    </div>
                """
                c5.markdown(html_code_token5, unsafe_allow_html=True)
        if col == c6:
            with col:
                c6.markdown(css_code, unsafe_allow_html=True)
                html_code_token6 = """
                    <div class="custom-container">
                        <img src="https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Dragon_Egg-512.png" alt="Dragon" class="custom-image">
                        <p>3,000 points</p>
                        <button class="custom-button">Purchase Hatching Egg</button>
                    </div>
                """
                c6.markdown(html_code_token6, unsafe_allow_html=True)
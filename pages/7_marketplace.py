import requests
import streamlit as st

st.header("Token Marketplace")

css_code = """
    <style>
        .custom-container {
            border: 2px solid #1f618d;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 200px;
        }

        .custom-image {
            width: 100%;
            border-radius: 5px;
        }

        .custom-button {
            margin-top: 10px;
        }
    </style>
"""

with st.container():
    col1, col2, col3 = st.columns(3)

    for col in [col1, col2, col3]:
        with col:
            st.markdown(css_code, unsafe_allow_html=True)

            html_code = """
                <div class="custom-container">
                    <img src="https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain" alt="My Say Token" class="custom-image">
                    <p>1,000 points</p>
                    <button class="custom-button">Purchase My Say</button>
                </div>

                <div class="custom-container">
                    <img src="https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png" alt="My Way Token" class="custom-image">
                    <p>2,000 points</p>
                    <button class="custom-button">Purchase My Way</button>
                </div>

                <div class="custom-container">
                    <img src="https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain" alt="My Day Token" class="custom-image">
                    <p>3,000 points</p>
                    <button class="custom-button">Purchase My Day</button>
                </div>

                
            """
            st.markdown(html_code, unsafe_allow_html=True)

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
            height: 400px;
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
    tokens = [
        {"image_url": "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain", "name": "My Say Token", "points": "1,000"},
        {"image_url": "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png", "name": "My Way Token", "points": "2,000"},
        {"image_url": "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain", "name": "My Day Token", "points": "3,000"},
        {"image_url": "https://th.bing.com/th/id/OIP.OLAyoeOOoWuXs2aaZ9FL9QHaKl?rs=1&pid=ImgDetMain", "name": "My Day Token", "points": "3,000"},
        {"image_url": "https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png", "name": "My Day Token", "points": "3,000"},
        {"image_url": "https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain", "name": "My Day Token", "points": "3,000"},
    ]

    tokens_per_row = 3

    for i in range(0, len(tokens), tokens_per_row):
        row_tokens = tokens[i:i + tokens_per_row]

        col1, col2, col3 = st.columns(3)

        for col, token in zip([col1, col2, col3], row_tokens):
            with col:
                st.markdown(css_code, unsafe_allow_html=True)

                html_code = f"""
                    <div class="custom-container">
                        <img src="{token['image_url']}" alt="{token['name']}" class="custom-image">
                        <p>{token['points']} points</p>
                        <button class="custom-button">Purchase {token['name']}</button>
                    </div>
                """
                st.markdown(html_code, unsafe_allow_html=True)

    
       

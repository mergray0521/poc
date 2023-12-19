import requests
import streamlit as st

st.header("Token Marketplace")

# # Sample image URLs
# token_1 = "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain"
# token_2 = "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png"
# token_3 = "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"
# token_4 = "https://th.bing.com/th/id/OIP.OLAyoeOOoWuXs2aaZ9FL9QHaKl?rs=1&pid=ImgDetMain"
# token_5 = "https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png"
# token_6 = "https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain"

css_code = """
    <style>
        .custom-container {
            border: 2px solid #1f618d;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
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

    tokens = [
        {"token_1": "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain", "name": "My Say Token", "points": "1,000"},
        {"token_2": "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png", "name": "My Way Token", "points": "2,000"},
        {"token_3": "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain", "name": "My Day Token", "points": "3,000"},
        {"token_4": "https://th.bing.com/th/id/OIP.OLAyoeOOoWuXs2aaZ9FL9QHaKl?rs=1&pid=ImgDetMain", "name": "My Day Token", "points": "3,000"},
        {"token_5": "https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png", "name": "My Day Token", "points": "3,000"},
        {"token_6": "https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain", "name": "My Day Token", "points": "3,000"},
    ]

    for token in tokens:
        with col1, col2, col3:
            st.markdown(css_code, unsafe_allow_html=True)

            html_code = f"""
                <div class="custom-container">
                    <img src="{token['image_url']}" alt="{token['name']}" class="custom-image">
                    <p>{token['points']} points</p>
                    <button class="custom-button">Purchase {token['name']}</button>
                </div>
            """
            st.markdown(html_code, unsafe_allow_html=True)



# # Create three columns
# # col1, col2, col3 = st.columns(3)
# c1, c2, c3 = st.columns(3)
# c4, c5, c6 = st.columns(3) #just to highlight these are different cols
# with st.container():     
#     c1.image(token_1, caption="My Say Token", use_column_width=True, width=300)
#     c1.text("1,000 points")
#     c1.button("Purchase My Say", key="purchase_my_say", help="my-button")

#     c2.write("c2")
#     c2.image(token_4, caption="Minion Glasses", use_column_width=True, width=300)
#     c2.text("2,000 points")
#     c2.button("Purchase Glasses", key="purchase_glasses", help="my-button")
#     c3.write("c3") 
# with st.container():     
#     c4.write("c4")     
#     c5.write("c5")     
#     c6.write("c6")



# Display images in containers within columns
# with col1:
#     with st.container():
#         st.markdown('<div class="css-1r6slb0 e1tzin5v2">', unsafe_allow_html=True)
#         st.image(token_1, caption="My Say Token", use_column_width=True, width=300)
#         st.text("1,000 points")
#         st.button("Purchase My Say", key="purchase_my_say", help="my-button")
#         st.image(token_4, caption="Minion Glasses", use_column_width=True, width=300)
#         st.text("2,000 points")
#         st.button("Purchase Glasses", key="purchase_glasses", help="my-button")
#         st.markdown('</div>', unsafe_allow_html=True)

# with col2:
#     st.markdown('<div class="css-1r6slb0 e1tzin5v2">', unsafe_allow_html=True)
#     st.image(token_2, caption="My Way Token", use_column_width=True, width=50)
#     st.text("2,000 points")
#     st.button("Purchase My Way", key="purchase_my_way", help="my-button")
#     st.image(token_5, caption="Park Pass", use_column_width=True, width=50)
#     st.text("4,000 points")
#     st.button("Purchase Pass", key="purchase_pass", help="my-button")
#     st.markdown('</div>', unsafe_allow_html=True)

# with col3:
#     st.markdown('<div class="css-1r6slb0 e1tzin5v2">', unsafe_allow_html=True)
#     st.image(token_3, caption="My Day Token", use_column_width=True, width=50)
#     st.text("3,000 points")
#     st.button("Purchase My Day", key="purchase_my_day", help="my-button")
#     st.image(token_6, caption="Dragon", use_column_width=True, width=50)
#     st.text("3,000 points")
#     st.button("Purchase Dragon", key="purchase_dragon", help="my-button")
#     st.markdown('</div>', unsafe_allow_html=True)

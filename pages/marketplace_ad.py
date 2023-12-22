import requests
import streamlit as st
# color:#33ff33;background-color: #EEEEEE;border: 2px solid #CCCCCC;padding: 5% 5% 5% 10%;border-radius: 5px;
st.header("Token Marketplace")
css_code = """
    <style>
        .custom-container {
            border: 2px solid #DCDCDC;
            background: #DCDCDC;
            padding:  5% 5% 5% 10%;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 350px;
        }

        .custom-image {
            width: 100%;
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
                        <img src="https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png" alt="Park Pass" class="custom-image">
                        <p>4,000 points</p>
                        <button class="custom-button">Purchase My Way</button>
                    </div>
                """
                c5.markdown(html_code_token5, unsafe_allow_html=True)
        if col == c6:
            with col:
                c6.markdown(css_code, unsafe_allow_html=True)
                html_code_token6 = """
                    <div class="custom-container">
                        <img src="https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain" alt="Dragon" class="custom-image">
                        <p>3,000 points</p>
                        <button class="custom-button">Purchase Dragon</button>
                    </div>
                """
                c6.markdown(html_code_token6, unsafe_allow_html=True)

# Sample image URLs
# token_1 = "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain"
# token_1_text = st.text('1,00 points')
# token_1_button = st.button("Purchase My Say", key="purchase_my_say", help="my-button")
# token_1_img = st.image(token_1,  caption="My Say Token", use_column_width=True, width=300)
# token_2 = "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png"
# token_3 = "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"
# token_4 = "https://th.bing.com/th/id/OIP.OLAyoeOOoWuXs2aaZ9FL9QHaKl?rs=1&pid=ImgDetMain"
# token_5 = "https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png"
# token_6 = "https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain"

# Create three columns
# col1, col2, col3 = st.columns(3)
# c1, c2, c3 = st.columns(3)
# c4, c5, c6 = st.columns(3) 
# with st.container():   
#     c1.markdown(css_code1, unsafe_allow_html=True)
#     c1.markdown(html_code1, unsafe_allow_html=True)
#     # c1Img = c1.image(token_1,  caption="My Say Token", use_column_width=True, width=300)
#     # # st.markdown('<div class="css-1r6slb0 e1tzin5v2">', unsafe_allow_html=True)
#     # c1.markdown(f'<div style="color:#33ff33;background-color: #EEEEEE;border: 2px solid #CCCCCC;padding: 5% 5% 5% 10%;border-radius: 5px;height: 100px"> {token_1_button} </div>', unsafe_allow_html=True)
#     # Column/Token 1
#     # c1.image(token_1, caption="My Say Token", use_column_width=True, width=300)
#     # c1.text("1,000 points")
#     # c1.button("Purchase My Say", key="purchase_my_say", help="my-button")

#     # Column/Token 2
#     c2.image(token_2, caption="My Way Token", use_column_width=True, width=50)
#     c2.text("2,000 points")
#     c2.button("Purchase My Way", key="purchase_my_way", help="my-button")
#     # c2.markdown(f'<h1 style="color:#33ff33;background-color: #EEEEEE;border: 2px solid #CCCCCC;padding: 5% 5% 5% 10%;border-radius: 5px;height: 100px">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)
#     # Column/Token 3
#     c3.image(token_3, caption="My Day Token", use_column_width=True, width=50)
#     c3.text("3,000 points")
#     c3.button("Purchase My Day", key="purchase_my_day", help="my-button") 

# #second row
# with st.container():     
#     # Column/Token 4
#     c4.image(token_4, caption="Minion Glasses", use_column_width=True, width=300)
#     c4.text("2,000 points")
#     c4.button("Purchase Glasses", key="purchase_glasses", help="my-button")
    
#     # Column/Token 5
#     c5.image(token_5, caption="Park Pass", use_column_width=True, width=50)
#     c5.text("4,000 points")
#     c5.button("Purchase Pass", key="purchase_pass", help="my-button")  

#     # Column/Token 6
#     c6.image(token_6, caption="Dragon", use_column_width=True, width=50)
#     c6.text("3,000 points")
#     c6.button("Purchase Dragon", key="purchase_dragon", help="my-button")

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

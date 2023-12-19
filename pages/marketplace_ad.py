import requests
import streamlit as st

# GitHub repository details
github_repo = "mergray0521/poc"
css_file_path = "pages/style_ad.css"

# Construct the raw URL for the CSS file
raw_url = f'https://raw.githubusercontent.com/{github_repo}/main/{css_file_path}'

# Fetch the CSS content from GitHub
response = requests.get(raw_url)
css_content = response.text

# Apply the CSS to Streamlit
st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)

st.header("Token Marketplace")



# Sample image URLs
token_1 = "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain"
token_2 = "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png"
token_3 = "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"
token_4 = "https://th.bing.com/th/id/OIP.OLAyoeOOoWuXs2aaZ9FL9QHaKl?rs=1&pid=ImgDetMain"
token_5 = "https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png"
token_6 = "https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain"

# Create three columns
# col1, col2, col3 = st.columns(3)
c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3) #just to highlight these are different cols
with st.container():   
    # st.markdown('<div class="css-1r6slb0 e1tzin5v2">', unsafe_allow_html=True)
    c1.markdown(f'<div style="color:#33ff33;background-color: #EEEEEE;border: 2px solid #CCCCCC;padding: 5% 5% 5% 10%;border-radius: 5px;height: 100px"> "My Say Token" </h1>', unsafe_allow_html=True)
    # Column/Token 1
    c1.image(token_1, caption="My Say Token", use_column_width=True, width=300)
    c1.text("1,000 points")
    c1.button("Purchase My Say", key="purchase_my_say", help="my-button")

    # Column/Token 2
    c2.image(token_2, caption="My Way Token", use_column_width=True, width=50)
    c2.text("2,000 points")
    c2.button("Purchase My Way", key="purchase_my_way", help="my-button")
    # c2.markdown(f'<h1 style="color:#33ff33;background-color: #EEEEEE;border: 2px solid #CCCCCC;padding: 5% 5% 5% 10%;border-radius: 5px;height: 100px">{"ColorMeBlue text”"}</h1>', unsafe_allow_html=True)
    # Column/Token 3
    c3.image(token_3, caption="My Day Token", use_column_width=True, width=50)
    c3.text("3,000 points")
    c3.button("Purchase My Day", key="purchase_my_day", help="my-button") 

#second row
with st.container():     
    # Column/Token 4
    c4.image(token_4, caption="Minion Glasses", use_column_width=True, width=300)
    c4.text("2,000 points")
    c4.button("Purchase Glasses", key="purchase_glasses", help="my-button")
    
    # Column/Token 5
    c5.image(token_5, caption="Park Pass", use_column_width=True, width=50)
    c5.text("4,000 points")
    c5.button("Purchase Pass", key="purchase_pass", help="my-button")  

    # Column/Token 6
    c6.image(token_6, caption="Dragon", use_column_width=True, width=50)
    c6.text("3,000 points")
    c6.button("Purchase Dragon", key="purchase_dragon", help="my-button")

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

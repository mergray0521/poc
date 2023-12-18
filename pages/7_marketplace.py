import requests
import streamlit as st

# GitHub repository details
github_repo = "mergray0521/poc"
css_file_path = "pages/style.css"

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
col1, col2, col3 = st.columns(3)

# Display images in containers within columns
with col1:
    st.markdown('<div class="my-container">', unsafe_allow_html=True)
    st.image(token_1, caption="My Say Token", use_column_width=True, width=300)
    st.text("1,000 points")
    st.button("Purchase My Say", key="purchase_my_say", help="my-button")
    st.image(token_4, caption="Minion Glasses", use_column_width=True, width=300)
    st.text("2,000 points")
    st.button("Purchase Glasses", key="purchase_glasses", help="my-button")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="my-container">', unsafe_allow_html=True)
    st.image(token_2, caption="My Way Token", use_column_width=True, width=50)
    st.text("2,000 points")
    st.button("Purchase My Way", key="purchase_my_way", help="my-button")
    st.image(token_5, caption="Park Pass", use_column_width=True, width=50)
    st.text("4,000 points")
    st.button("Purchase Pass", key="purchase_pass", help="my-button")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="my-container">', unsafe_allow_html=True)
    st.image(token_3, caption="My Day Token", use_column_width=True, width=50)
    st.text("3,000 points")
    st.button("Purchase My Day", key="purchase_my_day", help="my-button")
    st.image(token_6, caption="Dragon", use_column_width=True, width=50)
    st.text("3,000 points")
    st.button("Purchase Dragon", key="purchase_dragon", help="my-button")
    st.markdown('</div>', unsafe_allow_html=True)

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

# Sample image URLs
token_1 = "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain"
token_2 = "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png"
token_3 = "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"
token_4 = "https://th.bing.com/th/id/OIP.OLAyoeOOoWuXs2aaZ9FL9QHaKl?rs=1&pid=ImgDetMain"
token_5 = "https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png"
token_6 = "https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain"

# Create three columns
col1, col2, col3 = st.columns(3)

# Loop over columns and apply styling and content
for i, col in enumerate([col1, col2, col3]):
    with col.container(border=True):
        # Adjust the content inside the div according to your styling
        col.markdown(f'<div class="css-1r6slb0 e1tzin5v2">Content for Column {i+1}</div>', unsafe_allow_html=True)

        # Display images in containers within columns
        col.image(token_1, caption="My Say Token", use_column_width=True, width=300)
        col.text("1,000 points")
        col.button("Purchase My Say")

        col.image(token_4, caption="Minion Glasses", use_column_width=True, width=300)
        col.text("2,000 points")
        col.button("Purchase Glasses")

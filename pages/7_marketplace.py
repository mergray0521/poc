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
image_urls = [
    "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain",
    "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png",
    "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"
]

# Number of columns
num_columns = 3

# Loop over columns and apply styling
for i in range(num_columns):
    col = st.column()

    # Adjust the content inside the div according to your styling
    col.markdown(f'<div class="css-1r6slb0 e1tzin5v2" style="width:{box_width}px; height:{box_height}px;">Content for Column {i+1}</div>', unsafe_allow_html=True)

    # Display image, description, and button within columns
    col.image(image_urls[i], caption=f"Image {i+1}", use_column_width=True, width=300)
    col.text(f"Description for Column {i+1}")
    col.button(f"Button for Column {i+1}")

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

# Set explicit width and height for the gray boxes
box_width = 200
box_height = 200

# Column 1
col1 = st.columns(1)[0]

# Customize content for column 1
col1.markdown(f'<div class="css-1r6slb0 e1tzin5v2" style="width:{box_width}px; height:{box_height}px;">Content for Column 1</div>', unsafe_allow_html=True)

# Column 2
col2 = st.columns(1)[0]

# Customize content for column 2
col2.markdown(f'<div class="css-1r6slb0 e1tzin5v2" style="width:{box_width}px; height:{box_height}px;">Content for Column 2</div>', unsafe_allow_html=True)

# Column 3
col3 = st.columns(1)[0]

# Customize content for column 3
col3.markdown(f'<div class="css-1r6slb0 e1tzin5v2" style="width:{box_width}px; height:{box_height}px;">Content for Column 3</div>', unsafe_allow_html=True)



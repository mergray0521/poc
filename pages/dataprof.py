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

# Individual styling for each column
col1, col2, col3 = st.columns(3)

col1.markdown('<div class="css-1r6slb0 e1tzin5v2">Temperature: 70 °F, Change: 1.2 °F</div>', unsafe_allow_html=True)

col2.markdown('<div class="css-1r6slb0 e1tzin5v2">Wind: 9 mph, Change: -8%</div>', unsafe_allow_html=True)

col3.markdown('<div class="css-1r6slb0 e1tzin5v2">Humidity: 86%, Change: 4%</div>', unsafe_allow_html=True)



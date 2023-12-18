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
col1 = st.columns()
col1.markdown('<div class="css-1r6slb0 e1tzin5v2">Styled content for Temperature</div>', unsafe_allow_html=True)
col1.metric("Temperature", "70 °F", "1.2 °F")

col2 = st.columns()
col2.markdown('<div class="css-1r6slb0 e1tzin5v2">Styled content for Wind</div>', unsafe_allow_html=True)
col2.metric("Wind", "9 mph", "-8%")

col3 = st.columns()
col3.markdown('<div class="css-1r6slb0 e1tzin5v2">Styled content for Humidity</div>', unsafe_allow_html=True)
col3.metric("Humidity", "86%", "4%")




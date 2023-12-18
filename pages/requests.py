import requests
import streamlit as st

# GitHub repository details
github_repo = "your_username/your_repo"
css_file_path = "path/to/style.css"
github_token = "your_github_access_token"  # Optional, if the repository is private

# Construct the raw URL for the CSS file
raw_url = f'https://raw.githubusercontent.com/{github_repo}/main/{css_file_path}'

# Fetch the CSS content from GitHub
response = requests.get(raw_url, headers={"Authorization": f"Bearer {github_token}"})
css_content = response.text

# Apply the CSS to Streamlit
st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)

# Rest of your Streamlit code
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

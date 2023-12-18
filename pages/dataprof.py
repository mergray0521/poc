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

# Number of columns
num_columns = 3

# Set explicit width and height for the gray boxes
box_width = 200
box_height = 150

cols = st.columns(3)  # Adjust the number as needed
col = cols[0]  # Use the desired column

# Loop over columns and apply styling
for i, col in enumerate(cols):
    col.markdown(f'<div class="css-1r6slb0 e1tzin5v2" style="width:{box_width}px; height:{box_height}px;">Content for Column {i+1}</div>', unsafe_allow_html=True)
    col.metric(f"Metric {i+1}", f"Value {i+1}", f"Change {i+1}%")



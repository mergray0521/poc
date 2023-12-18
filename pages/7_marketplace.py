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
box_height = 200

cols = st.columns(num_columns)

# Sample data (replace with your actual data)
data = [
    {"image_url": "https://example.com/image1.jpg", "description": "Description 1"},
    {"image_url": "https://example.com/image2.jpg", "description": "Description 2"},
    {"image_url": "https://example.com/image3.jpg", "description": "Description 3"},
]

# Loop over columns and apply styling
for i, col in enumerate(cols):
    # Access data for the current column
    current_data = data[i]

    # Display image
    col.image(current_data["image_url"], width=box_width, caption=f"Image {i+1}")

    # Display description
    col.write(current_data["description"])

    # Display button
    if col.button(f"Button {i+1}"):
        # Action to perform when the button is clicked
        st.write(f"Button {i+1} clicked!")

# You can customize the content of each box based on your specific requirements.


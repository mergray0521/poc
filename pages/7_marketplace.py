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

# Sample data (replace with your actual data)
data = [
    {
        "image_url": "https://example.com/image1.jpg",
        "button_label": "Button 1",
        "token_name": "My Way Token",
        "token_cost": "1,000 points",
    },
    {
        "image_url": "https://example.com/image2.jpg",
        "button_label": "Button 2",
        "token_name": "My Day Token",
        "token_cost": "2,000 points",
    },
    {
        "image_url": "https://example.com/image3.jpg",
        "button_label": "Button 3",
        "token_name": "My Say Token",
        "token_cost": "3,000 points",
    },
]

# Create a row with multiple columns
cols = st.beta_columns(len(data))

# Loop over data and apply styling
for i, col in enumerate(cols):
    # Access data for the current column
    current_data = data[i]

    # Customize content for the column
    content = f'''
    <div class="css-1r6slb0 e1tzin5v2" style="width:{box_width}px; height:{box_height}px;">
        <img src="{current_data["image_url"]}" style="max-width:100%; height:auto;" />
        <div class="caption">
            <p>{current_data["token_name"]}</p>
            <p>{current_data["token_cost"]}</p>
        </div>
        <button>{current_data["button_label"]}</button>
    </div>
    '''
    col.markdown(content, unsafe_allow_html=True)

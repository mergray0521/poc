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
    {"image_url": "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain", "description": "Token 1"},
    {"image_url": "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.pn", "description": "Token 2"},
    {"image_url": "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain", "description": "Token 3"},
]

# Loop over columns and apply styling
for i, col in enumerate(cols):
    # Access data for the current column
    current_data = data[i]

    # Apply existing markdown styling
    col.markdown(f'<div class="css-1r6slb0.e1tzin5v2" style="width:{box_width}px; height:{box_height}px;">', unsafe_allow_html=True)

    # Display image
    col.image(current_data["image_url"], width=box_width, caption=f"Image {i+1}")

    # Display description
    col.markdown(f'<div class="description">{current_data["description"]}</div>', unsafe_allow_html=True)

    # Display button
    if col.button(f"Button {i+1}"):
        # Action to perform when the button is clicked
        st.write(f"Button {i+1} clicked!")

    # Close the div
    col.markdown('</div>', unsafe_allow_html=True)


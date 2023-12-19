import streamlit as st

st.title("My Stuff")

css_code = """
    <style>
        .custom-container {
            border: 2px solid #1f618d;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 200px;
        }
    </style>
"""

# Define html_code outside the loop
html_code = """
    <div class="custom-container">
        1,000 points
    </div>

    <div class="custom-container">
        2,000 points
    </div>
"""


for col in cols:
    st.markdown(css_code, unsafe_allow_html=True)
    st.markdown(html_code, unsafe_allow_html=True)

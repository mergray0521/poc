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

# First row with one container spanning both columns
st.markdown(css_code, unsafe_allow_html=True)
html_code_row1 = """
    <div class="custom-container">
        Top Box
    </div>
"""
st.markdown(html_code_row1, unsafe_allow_html=True)

# Second row with two boxes, each taking up half the page (2 columns)
html_code_row2 = """
    <div class="custom-container">
        Left Box
    </div>

    <div class="custom-container">
        Right Box
    </div>
"""
st.markdown(html_code_row2, unsafe_allow_html=True)

# Third row with two boxes, each taking up half the page (2 columns)
html_code_row3 = """
    <div class="custom-container">
        Left Box
    </div>

    <div class="custom-container">
        Right Box
    </div>
"""
st.markdown(html_code_row3, unsafe_allow_html=True)

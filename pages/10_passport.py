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
cols_row2 = st.columns(2)
html_code_row2_left = """
    <div class="custom-container">
        Left Box
    </div>
"""
html_code_row2_right = """
    <div class="custom-container">
        Right Box
    </div>
"""
cols_row2[0].markdown(html_code_row2_left, unsafe_allow_html=True)
cols_row2[1].markdown(html_code_row2_right, unsafe_allow_html=True)

# Third row with two boxes, each taking up half the page (2 columns)
cols_row3 = st.columns(2)
html_code_row3_left = """
    <div class="custom-container">
        Left Box
    </div>
"""
html_code_row3_right = """
    <div class="custom-container">
        Right Box
    </div>
"""
cols_row3[0].markdown(html_code_row3_left, unsafe_allow_html=True)
cols_row3[1].markdown(html_code_row3_right, unsafe_allow_html=True)

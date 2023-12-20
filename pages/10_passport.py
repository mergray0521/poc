import streamlit as st

st.title("My Stuff")

css_code = """
    <style>
        .custom-container {
            border: 2px solid #DCDCDC;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 400px;
        }

            .custom-box {
            border: 2px solid #DCDCDC;
            padding:  5% 5% 5% 10%;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 200px;
        }

          .custom-header {
            text-align: left;
            font-weight: bold;

        }

        .custom-image {
            width: 100%;
            border-radius: 5px;
            height: 300px;
        }
    </style>  
"""

# First row with one container spanning both columns
st.markdown(css_code, unsafe_allow_html=True)
html_code_row1 = """
    <div class="custom-container">
    <h3 class="custom-header">Redeemables</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/QR_Code.png?raw=true" class="custom-image">
    </div>
"""
st.markdown(html_code_row1, unsafe_allow_html=True)

# Second row with two boxes, each taking up half the page (2 columns)
cols_row2 = st.columns(2)
html_code_row2_left = """
    <div class="custom-box">
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(15).png?raw=true class="custom-image">
    </div>
"""
html_code_row2_right = """
    <div class="custom-box">
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true class="custom-image">
    </div>
"""
cols_row2[0].markdown(html_code_row2_left, unsafe_allow_html=True)
cols_row2[1].markdown(html_code_row2_right, unsafe_allow_html=True)

# Third row with two boxes, each taking up half the page (2 columns)
cols_row3 = st.columns(2)
html_code_row3_left = """
    <div class="custom-box">
        Left Box
    </div>
"""
html_code_row3_right = """
    <div class="custom-box">
        Right Box
    </div>
"""
cols_row3[0].markdown(html_code_row3_left, unsafe_allow_html=True)
cols_row3[1].markdown(html_code_row3_right, unsafe_allow_html=True)

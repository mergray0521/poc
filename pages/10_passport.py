import streamlit as st

st.title("My Stuff")

css_code = """
    <style>
        .custom-container {
            border: 2px solid #DCDCDC;
            border-radius: 5px;
            padding:  0% 0% 0% 5%;
            text-align: center;
            margin-bottom: 10px;
            height: 400px;
        }

            .custom-box {
            border: 2px solid #DCDCDC;
            padding:  0% 0% 0% 5%;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 300px;
        }

          .custom-header {
            text-align: left;
            font-weight: bold;

        }

        .top-image {
            width: 100%;
            border-radius: 5px;
            height: 300px;
        }

        .smaller-image {
            width: 100%;
            border-radius: 5px;
            height: 50px;
        }

    </style>  
"""

# First row with one container spanning both columns
st.markdown(css_code, unsafe_allow_html=True)
html_code_row1 = """
    <div class="custom-container">
    <h3 class="custom-header">Redeemables</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/QR_Code.png?raw=true" class="top-image">
    </div>
"""
st.markdown(html_code_row1, unsafe_allow_html=True)

# Second row with two boxes, each taking up half the page (2 columns)
cols_row2 = st.columns(2)
html_code_row2_left = """
    <div class="custom-box">
    <h3 class="custom-header">Points</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(15).png?raw=true class="smaller-image">
    </div>
"""
html_code_row2_right = """
    <div class="custom-box">
    <h3 class="custom-header">Badges</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true class="smaller-image">
    </div>
"""
cols_row2[0].markdown(html_code_row2_left, unsafe_allow_html=True)
cols_row2[1].markdown(html_code_row2_right, unsafe_allow_html=True)

# Third row with two boxes, each taking up half the page (2 columns)
cols_row3 = st.columns(2)
html_code_row3_left = """
    <div class="custom-box">
    <h3 class="custom-header">Park Tickets</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true">
    </div>
"""
html_code_row3_right = """
    <div class="custom-box">
    <h3 class="custom-header">Hotel Keys</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true">
    </div>
"""
cols_row3[0].markdown(html_code_row3_left, unsafe_allow_html=True)
cols_row3[1].markdown(html_code_row3_right, unsafe_allow_html=True)

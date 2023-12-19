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

with st.container():
    col1, col2 = st.columns(2)

    for col in [col1, col2]:
        with col:
            st.markdown(css_code, unsafe_allow_html=True)

            html_code = """
                <div class="custom-container">
                    <p>1,000 points</p>
                </div>

                <div class="custom-container">
                    <p>2,000 points</p>
                </div>

                
            """
            st.markdown(html_code, unsafe_allow_html=True)

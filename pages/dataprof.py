import streamlit as st

# Your CSS code
css_code = """
    .css-1r6slb0.e1tzin5v2 {
        background-color: #EEEEEE;
        border: 2px solid #CCCCCC;
        padding: 5% 5% 5% 10%;
        border-radius: 5px;
    }
"""

# Apply the CSS to Streamlit
st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

# Streamlit app content
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="css-1r6slb0 e1tzin5v2">', "Temperature", "70" "1.2", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="css-1r6slb0 e1tzin5v2">', unsafe_allow_html=True)
    col2.metric("Wind", "9 mph", "-8%")
    # Additional metrics or content for col2
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="css-1r6slb0 e1tzin5v2">', unsafe_allow_html=True)
    col3.metric("Humidity", "86%", "4%")
    # Additional metrics or content for col3
    st.markdown('</div>', unsafe_allow_html=True)


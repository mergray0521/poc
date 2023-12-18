import requests
import streamlit as st

css_url = "https://github.com/mergray0521.github.io/poc/pages/style.css"

# Fetch the CSS content from the URL
response = requests.get(css_url)
css_content = response.text

# Apply the CSS to Streamlit
st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


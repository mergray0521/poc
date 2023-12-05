import streamlit as st
import snowflake.connector

st.set_page_config(
    page_title="Homepage"
)

st.title('My Passport')
st.sidebar.success("Select a page above.")


import streamlit as st
import pandas as pd
import snowflake.connector

st.title("My Stuff")

  with st.container():
    st.text('Reedemables')
    
    col1, col2 = st.columns(2)
    col1.write('Points')
    col2.write('Badges')

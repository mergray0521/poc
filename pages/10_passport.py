import streamlit as st
import pandas as pd
import snowflake.connector

st.title("My Stuff")

with st.container():
  st.text('Reedemables')
    

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3) #just to highlight these are different cols

c1.write('Points')
c2.write('Badges')

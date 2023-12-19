import streamlit as st
import pandas as pd
import snowflake.connector

st.title("My Stuff")

with st.container():
  st.text('Reedemables')
    

c1, c2 = st.columns(2)
c3, c4 = st.columns(2) #just to highlight these are different cols

c1.write('Points')
c2.write('Badges')
c3.write('Park Tickets')
c4.write('Hotel Keys')

import streamlit as st
import pandas as pd
import snowflake.connector

st.title("My Stuff")

css_code = """
    <style>
        .container {
            border: 2px solid #1f618d;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 350px;
        }
    </style>
"""

with st.container():
  st.text('Reedemables')

with st.container():
  c1, c2 = st.columns(2)
  c3, c4 = st.columns(2) #just to highlight these are different cols
for c in [c1, c2, c3, c4]:
  with c:
    st.markdown(css_code, unsafe_allow_html=True)

  
html_code = """
    <div class="container">
        <p>Points</p>
    </div>
    <div class="container">
        <p>Badges</p>
    </div>
    <div class="Park Tickets">
        <p>Badges</p>
    </div>
    <div class="Hotel Keys">
        <p>Badges</p>
    </div>
"""

import streamlit as st
import pandas as pd
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["token_schemas"])
my_cur = my_cnx.cursor()

st.header("Earned Token") 
st.text ("Congratulations! You earned a new Flying Harness token!")

image_url = "https://insidethemagic.net/wp-content/uploads/2017/05/Screen-Shot-2017-05-05-at-3.44.38-PM.jpg"
st.image(image_url, caption="Token: Flying Harness", use_column_width=True)



        





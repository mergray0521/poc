import streamlit as st
import pandas as pd
import snowflake.connector


# Your database connection
my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.title("Display Points")

# Input user ID
user_id = st.text_input("Enter User ID:")

if st.button("Submit"):
    if user_id:
        # Query the point_ownership table
        query = f"SELECT point_quantity FROM point_ownership WHERE user_id = '{user_id}'"
        my_cur.execute(query)
        result = my_cur.fetchall()



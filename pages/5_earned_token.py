import streamlit as st
import pandas as pd
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.header("Earned New Token") 
st.text("Congrats on recruiting your team of Minions! Here is your Minion Mayhem Badge!")

image_url = "https://i.ytimg.com/vi/H-7_dOS5z9s/maxresdefault.jpg"
st.image(image_url, caption="Token: Minion Mayhem", use_column_width=True)

if st.button("Collect"):
    # Insert the form data into Snowflake
    query = f"INSERT INTO token_ownership (TOKEN_ID, OWNER_ID, QUANTITY) VALUES ('{605}','{3}', '{1}')"
    my_cur.execute(query)
    my_cnx.commit()
    st.success(f"Flying harness token added to user {3}'s wallet")





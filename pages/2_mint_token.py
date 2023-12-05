import streamlit as st
import snowflake.connector

st.title("Mint Token")

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select token_name from token_schemas")
my_data_rows = my_cur.fetchall()
st.header("The current token schemas inclue:")
st.dataframe(my_data_rows)




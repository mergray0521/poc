import streamlit as st
import snowflake.connector

st.title("Mint Token")

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

my_cur.execute("select token_name from token_schemas")
my_data_rows = my_cur.fetchall()
st.header("The current token schemas include:")
st.dataframe(my_data_rows)

try:
    schema_choice = streamlit.text_input('Which schema would you like to add a token to?')
    if not schema_choice:
        streamlit.error("Please select a token schema to proceed.")
    else:
        back_from_function = token_schema(schema_choice)
        streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()




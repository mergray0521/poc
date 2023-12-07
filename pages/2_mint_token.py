import streamlit as st
import snowflake.connector
from urllib.error import URLError

st.title("Mint Token")

my_cnx = snowflake.connector.connect(**st.secrets["token_schemas", "inventory_db"])
my_cur = my_cnx.cursor()

# Query token schema options
def token_schemas(schema_name):
  schema_options = f"SELECT * FROM inventory_db.{schema_name}"
  my_cur.execute(query)
  result_data = my_cur.fetchall()
  return result_data

selected_schema = st.selectbox("Select Token Schema", [schema[0] for schema in schema_options])





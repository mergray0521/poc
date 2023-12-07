import streamlit as st
import snowflake.connector
from urllib.error import URLError

st.title("Mint Token")

my_cnx = snowflake.connector.connect(**st.secrets["inventory_db"])
my_cur = my_cnx.cursor()

def token_schemas():
    query = "SELECT * FROM inventory_db.{schema_name}"  # Update with your actual query
    my_cur.execute(query)
    result_data = my_cur.fetchall()
    return result_data

# Call the function to get schema options
schema_options = st.selectbox("Token Schemas", ["dragon_egg", "egg_nests", "egg_feathers", "trained_dragon", "sketchbook", "avatar_wearables", "weapons", "healing_herbs", "star_maps", "points"] )

# Create dropdown
selected_schema = st.selectbox("Select Token Schema", [schema[0] for schema in schema_options])



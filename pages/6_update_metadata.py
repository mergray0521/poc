import streamlit as st
import snowflake.connector
import pandas as pd

# Snowflake connection
my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

# Load data from Snowflake
query = "SELECT * FROM avatar_wearables"
my_cur.execute(query)
columns = [col[0] for col in my_cur.description]
rows = my_cur.fetchall()
df = pd.DataFrame(rows, columns=columns)


import streamlit as st
import snowflake.connector

# Snowflake connection
my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

# Token information (you can replace this with your Streamlit form input)
token_id = 123
type = "Example Token"
materials = "Fungible"
color = "HTTYD"

# MERGE statement
merge_query = f'''
MERGE INTO avatar_wearables AS target
USING (SELECT {token_id} AS "TOKEN_ID",
              '{type}' AS "TYPE",
              '{materials}' AS "MATERIALS",
              '{color}' AS "COLOR") AS source
ON target."TOKEN_ID" = source."TOKEN_ID"
WHEN MATCHED THEN
  UPDATE SET "TYPE" = COALESCE(source."TYPE", target."TYPE"),
             "MATERIALS" = COALESCE(source."MATERIALS", target."MATERIALS"),
             "COLOR" = COALESCE(source."COLOR", target."COLOR")
WHEN NOT MATCHED THEN
  INSERT ("TOKEN_ID", "TYPE", "MATERIALS", "COLOR")
  VALUES (source."TOKEN_ID", source."TYPE", source."MATERIALS", source."COLOR");
'''

# Execute the MERGE query
my_cur.execute(merge_query)
my_cnx.commit()

st.success("Table updated using MERGE statement")



















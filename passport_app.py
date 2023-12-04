import streamlit

streamlit.title('Welcome to Passport')
streamlit.header('Create Token Schema')

pip install "snowflake-connector-python"

[connections.snowflake]
account = "CNAHFEW.KNB62637"
user = "Mergray0521"
password = "Lakegage0521!"
role = "accountadmin"
warehouse = "compute_wh"
database = "token_schemas"
schema = "token_schemas"
client_session_keep_alive = true

# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from token_schemas;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.token_schema_id}:")

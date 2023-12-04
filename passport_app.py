import streamlit

streamlit.title('Welcome to Passport')
streamlit.header('Create Token Schema')

import snowflake.connector

[connections.snowflake]
account = "CNAHFEW.KNB62637"
user = "mergray0521"
password = "Lakegage0521!"
role = "accountadmin"
warehouse = "compute_wh"
database = "token_schemas"
schema = "token_schemas"
client_session_keep_alive = true


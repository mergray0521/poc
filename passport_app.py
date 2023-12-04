import streamlit

streamlit.title('Welcome to Passport')
streamlit.header('Create Token Schema')

pip install snowflake-connector-python
import snowflake.connector

# Set up the connection parameters
connection_params = {
    'user': 'mergray0521',
    'password': 'Lakegage0521!',
    'account': 'CNAHFEW.KNB62637',
    'warehouse': 'compute_wh',
    'database': 'token_schemas',
    'schema': 'token_schemas'
}

# Establish the connection
conn = snowflake.connector.connect(**connection_params)

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries or commands here
cursor.execute("SELECT * FROM token_schemas")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

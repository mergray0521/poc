import streamlit as st
import snowflake.connector

st.title("Mint Token")

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

def fetch_token_schemas():
    query = "SELECT * FROM inventory_db"  
    my_cur.execute(query)
    result_data = my_cur.fetchall()
    return [schema[0] for schema in result_data]

# Call the function to get token schemas
schema_options = fetch_token_schemas()

# Create dropdown
selected_schema = st.selectbox("Select Token Schema", schema_options)

if __name__ == "__main__":
    main()
        

import streamlit as st
import snowflake.connector

st.title("Update or Add Metadata")

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()
    
# Search by Token ID
token_id = st.text_input('Enter Token ID:')
if st.button('Search'):
    # Fetch data from Snowflake based on token_id
    cursor = conn.cursor()
    query = f"SELECT * FROM avatar_wearables WHERE token_id = '{token_id}'"
    cursor.execute(query)
    data = cursor.fetchone()

    # Display data
    if data:
        st.write('Current Data:')
        st.table(data)

        # Edit and Save
        st.write('Edit Data:')
        # Add input fields for each column you want to edit

        if st.button('Save'):
            # Update the row in Snowflake with the new values
            # Write the update query here

    else:
        st.write('Token ID not found')

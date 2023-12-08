import streamlit as st
import snowflake.connector

# Streamlit UI
st.title('Update Metadata Page')

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

# Search by Token ID
token_id = st.text_input('Enter Token ID:')
if st.button('Search'):
    # Fetch data from Snowflake based on token_id
    query = f"SELECT * FROM avatar_wearables WHERE token_id = '{token_id}'"
    my_cur.execute(query)
    my_cnx.commit()
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
            pass  # placeholder for the update logic

    else:
        st.write('Token ID not found')

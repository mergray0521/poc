import streamlit as st
import snowflake.connector

# Streamlit UI
st.title('Update Metadata Page')

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

# Search by Token ID
token_id = st.text_input('Enter Token ID:')
if st.button('Search'):
    # Fetch data from Snowflake based on token_id with explicit type casting
    query = f"SELECT CAST(token_id AS VARCHAR), CAST(type AS VARCHAR), CAST(materials AS VARCHAR), CAST(color AS VARCHAR) FROM avatar_wearables WHERE token_id = '{token_id}'"
    my_cur.execute(query)
    my_cnx.commit()
    data = my_cur.fetchone()

    # Display data
    if data:
        st.write('Current Data:')
        st.table(data)

        # Edit and Save
        st.write('Edit Data:')
        # Add input fields for each column you want to edit

        updated_values = {}  # Store updated values in a dictionary

        for column_name, column_value in zip(my_cur.description, data):
            col_name = column_name[0]  # Extract the column name from the cursor description
            new_value = st.text_input(f'Edit {col_name}', value=str(column_value))
            updated_values[col_name] = new_value

        if st.button('Save'):
            # Update the row in Snowflake with the new values
            update_query = f"UPDATE avatar_wearables SET "
            update_query += ", ".join([f"{key} = '{value}'" for key, value in updated_values.items()])
            update_query += f" WHERE token_id = '{token_id}'"

            print("Update Query:", update_query)  # Add this line to print the query

            try:
                my_cur.execute(update_query)
                my_cnx.commit()
                st.success('Data updated successfully!')
            except Exception as e:
                st.error(f"Error updating data in Snowflake: {e}")

    else:
        st.write('Token ID not found')

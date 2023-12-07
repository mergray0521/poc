import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.title("Assign Token Ownership")

# Get user input
token_id = st.text_input("Token ID:")
owner_id = st.text_input("Owner ID:")
quantity = st.text_input("Quantity:")

# Check if all fields are filled
if token_id and owner_id and quantity:
    if st.button("Assign Ownership"):
        try:
            # Your SQL query to update the ownership table
            query = f"UPDATE TOKEN_OWNERSHIP SET OWNER_ID = '{owner_id}', Quantity = {quantity} WHERE TOKEN_ID = '{token_id}'"
            
            # Execute the query
            my_cur.execute(query)

            # Commit the changes
            my_cnx.commit()

            st.success("Ownership updated successfully!")

        except Exception as e:
            st.error(f"Error updating ownership: {str(e)}")


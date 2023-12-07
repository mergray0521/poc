import streamlit as st
import snowflake.connector

def main():

    my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
    my_cur = my_cnx.cursor()
    
    st.title("Assign Token Ownership")

    # Get user input
    token_id = st.text_input("Token ID:")
    owner_id = st.text_input("Owner ID:")
    quantity = st.text_input("Quantity:")

    # Check if all fields are filled
    if st.button("Assign Ownership"):
        # Call the function to update ownership in Snowflake
        update_ownership(token_id, owner_id, quantity)

# Function to update ownership in Snowflake
def update_ownership(token_id, owner_id, quantity):
    try:
        # Your SQL query to update the ownership table
        query = f"UPDATE TOKEN_OWNERSHIP SET OWNER_ID = '{owner_id}', Quantity = {quantity} WHERE TOKEN_ID = '{token_id}'"

        st.success("Ownership updated successfully!")

    except Exception as e:
        st.error(f"Error updating ownership: {str(e)}")

    finally:
        # Close the connection
        if my_cnx:
            my_cnx.close()

# Run the app
if __name__ == "__main__":
    main()

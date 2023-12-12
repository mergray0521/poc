import streamlit as st
import snowflake.connector
    
st.title("Assign Token Ownership")

# Get user input
token_id = st.text_input("Token ID:")
owner_id = st.text_input("Owner ID:")
quantity = st.text_input("Quantity:")

# Check if all fields are filled
if st.button("Assign Ownership"):
    #Connect to Snowflake
    my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
    my_cur = my_cnx.cursor()

    # Insert the form data into Snowflake
    query = f"INSERT INTO token_ownership (TOKEN_ID, OWNER_ID, QUANTITY) VALUES ('{token_id}','{owner_id}', '{quantity}')"
    my_cur.execute(query)
    my_cnx.commit()

    st.success(f"New ownership assigned for: {token_id}")
        

import streamlit as st
import pandas as pd
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()


st.title("Display Tokens")

# Input user ID
user_id = st.text_input("Enter User ID:")

if user_id:
    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=snowflake_username,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        role=snowflake_role
    )

    # Query the token_ownership table
    query = f"SELECT token_id FROM token_ownership WHERE owner_id = '{user_id}'"
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

    # Display the result in Streamlit
    if result:
        st.success(f"Tokens for User ID {user_id}:")
        tokens_df = pd.DataFrame(result, columns=["Token ID"])
        st.dataframe(tokens_df)
    else:
        st.warning(f"No tokens found for User ID {user_id}")

    # Close Snowflake connection
    conn.close()

T

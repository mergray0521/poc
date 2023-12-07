import streamlit as st
import snowflake.connector
import pandas as pd

def fetch_avatar_wearables_columns():
    query = "DESCRIBE TABLE avatar_wearables"
    my_cur.execute(query)
    result_data = my_cur.fetchall()
    return [column[0] for column in result_data]

st.title("Select Token Schema")

if st.button("Submit"):
    my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
    my_cur = my_cnx.cursor()

    # Fetch columns for the avatar_wearables table
    columns = fetch_avatar_wearables_columns()

    # Display the columns for the avatar_wearables table
    st.success("Columns for avatar_wearables:")
    st.write(columns)

    # Placeholder for the dynamic query using the avatar_wearables table
    # Replace this with your actual logic to retrieve data based on the avatar_wearables table
    query = "SELECT * FROM avatar_wearables"
    my_cur.execute(query)
    result = my_cur.fetchall()

    # Display the result in Streamlit
    if result:
        st.success("Data for avatar_wearables:")
        tokens_df = pd.DataFrame(result, columns=columns)
        st.dataframe(tokens_df)













import streamlit as st
import snowflake.connector
import pandas as pd

def fetch_token_columns(token_schema):
    query = f"DESCRIBE TABLE {token_schema}"
    my_cur.execute(query)
    result_data = my_cur.fetchall()
    return [column[0] for column in result_data]

st.title("Select Token Schema")

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

token_schema_options = ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"]
selected_token_schema = st.selectbox("Token Schema", token_schema_options)

if selected_token_schema == "avatar wearables" and st.button("Submit"):
    # Fetch columns for the selected table
    columns = fetch_token_columns(selected_token_schema)

    # Display the columns for the selected table
    st.success(f"Columns for {selected_token_schema}:")
    st.write(columns)

    # Placeholder for the dynamic query using the selected token_schema
    # Replace this with your actual logic to retrieve data based on the selected token_schema
    query = f"SELECT * FROM {selected_token_schema}"
    my_cur.execute(query)
    result = my_cur.fetchall()

    # Display the result in Streamlit
    if result:
        st.success(f"Data for {selected_token_schema}:")
        tokens_df = pd.DataFrame(result, columns=columns)
        st.dataframe(tokens_df)






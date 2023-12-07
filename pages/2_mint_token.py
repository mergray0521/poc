import streamlit as st
import snowflake.connector

st.title("Select Token Schema")

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

token_schema_options = ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"]
token_schema = st.selectbox("Token Schema", token_schema_options)

if st.button("Submit"):
    if token_schema:
        # Fetch columns for the selected token_schema
        columns = fetch_token_columns(token_schema)

        # Display the columns
        st.success(f"Columns for {token_schema}:")
        st.write(columns)

        # Placeholder for the dynamic query using the selected token_schema
        # Replace this with your actual logic to retrieve data based on the selected token_schema
        query = f"SELECT * FROM {token_schema}"
        my_cur.execute(query)
        result = my_cur.fetchall()

        # Display the result in Streamlit
        if result:
            st.success(f"Data for {token_schema}:")
            tokens_df = pd.DataFrame(result, columns=columns)
            st.dataframe(tokens_df)

















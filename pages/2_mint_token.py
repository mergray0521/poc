import streamlit as st
import snowflake.connector


def fetch_token_columns(avatar_wearables):
    query = f"DESCRIBE TABLE {avatar_wearables}"
    my_cur.execute(query)
    result_data = my_cur.fetchall()
    return [column[0] for column in result_data]

st.title("Select Token Schema")

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

token_schema_options = ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"]
token_schema = st.selectbox("Token Schema", token_schema_options)

if st.button("Submit"):
    if token_schema:
        # Fetch columns for the selected table
        columns = fetch_token_columns(avatar_wearables)

        # Display the columns
        st.success(f"Columns for {avatar_wearables}:")
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

















import streamlit as st
import snowflake.connector

def fetch_token_columns(token_schemas):
    columns_dict = {}

    for token_schema in token_schemas:
        query = f"DESCRIBE TABLE {token_schema}"
        my_cur.execute(query)
        result_data = my_cur.fetchall()
        columns = [column[0] for column in result_data]
        columns_dict[token_schema] = columns

    return columns_dict

st.title("Select Token Schema")

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

token_schema_options = ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"]
token_schema = st.selectbox("Token Schema", token_schema_options)

if st.button("Submit"):
  if selected_token_schema:
        # Fetch columns for the selected table
        columns_dict = fetch_token_columns([selected_token_schema])

      # Display the columns for the selected table
        for token_schema, columns in columns_dict.items():
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

















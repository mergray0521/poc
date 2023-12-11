import pandas as pd
import json
import streamlit as st
import snowflake.connector

# Snowflake connection
my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

# Streamlit configuration
st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")
st.title("Snowflake Table Editor ❄️")
st.caption("This is a demo of the `st.data_editor`.")

# Function to get dataset from Snowflake
def get_dataset():
    query = "SELECT * FROM AVATAR_WEARABLES"
    my_cur.execute(query)
    result = my_cur.fetchall()
    df = pd.DataFrame(result, columns=[desc[0] for desc in my_cur.description])
    return df

# Get the dataset
dataset = get_dataset()

# Display the editable data editor form
with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.data_editor(dataset, use_container_width=True)
    submit_button = st.form_submit_button("Submit")

# Upon submitting changes
if submit_button:
    try:
        # Fetch the existing data from Snowflake
        existing_data = get_dataset()

        # Identify the rows that have been edited
        edited_rows = pd.merge(existing_data, edited, how="outer", indicator=True).query("_merge == 'right_only'").drop('_merge', axis=1)

        # Update only the edited rows in Snowflake
        for index, row in edited_rows.iterrows():
            set_clauses = []
            token_id = row.get('token_id', '')
            
            # Build set clauses handling empty values for numeric columns
            for col in edited_rows.columns:
                value = row[col]
                if pd.api.types.is_numeric_dtype(edited_rows[col]) and pd.isna(value):
                    set_clauses.append(f"{col} = NULL")
                else:
                    set_clauses.append(f"{col} = '{value}'")

            set_clause = ", ".join(set_clauses)

            if token_id:
                query = f"UPDATE AVATAR_WEARABLES SET {set_clause} WHERE token_id = '{token_id}'"
                my_cur.execute(query)

        my_cnx.commit()

        st.success("Table updated")
    except Exception as e:
        st.warning(f"Error updating table: {e}")


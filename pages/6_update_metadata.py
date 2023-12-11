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
st.caption("This is a demo of the `st.experimental_data_editor`.")

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
    edited = st.experimental_data_editor(dataset, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

# Upon submitting changes
if submit_button:
    try:
        # Update the Snowflake table with the edited data
        for index, row in edited.iterrows():
            set_clause = ", ".join(f"{col} = '{row[col]}'" for col in edited.columns)
            query = f"UPDATE AVATAR_WEARABLES SET {set_clause} WHERE your_condition_column = 'your_condition_value'"
            my_cur.execute(query)
        
        st.success("Table updated")
    except Exception as e:
        st.warning(f"Error updating table: {e}")

    # Update the table to reflect changes in Snowflake
    st.experimental_rerun()

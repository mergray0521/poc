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
        # Update the Snowflake table with the edited data
        my_cur.execute("DELETE FROM AVATAR_WEARABLES")  # Clear the existing data in the table
        my_cnx.commit()
        my_cur.copy_pandas_to_table(edited, "AVATAR_WEARABLES", overwrite=True)
        st.success("Table updated")
    except Exception as e:
        st.warning(f"Error updating table: {e}")

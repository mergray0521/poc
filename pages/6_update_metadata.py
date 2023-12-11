import pandas as pd
import json
import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")
st.title("Snowflake Table Editor ❄️")
st.caption("This is a demo of the `st.experimental_data_editor`.")

def get_dataset():
    # Replace the next line with a SQL query to fetch the data
    query = "SELECT * FROM AVATAR_WEARABLES"
    df = pd.read_sql(query, my_cnx)
    return df

dataset = get_dataset()

with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.experimental_data_editor(dataset, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        # Note the quote_identifiers argument for case insensitivity
        my_cnx.write_pandas(edited, "AVATAR_WEARABLES", overwrite=True, quote_identifiers=False)
        st.success("Table updated")
    except:
        st.warning("Error updating table")
    st.experimental_rerun()














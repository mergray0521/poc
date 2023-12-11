import pandas as pd
import json
import snowflake.connector
import streamlit as st
from snowflake.snowpark import Session
import time

# Snowflake connection
my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")
st.title("Update Metadata Table")

def get_dataset():
    # load messages df
    df = session.table("avatar_wearables")

    return df

dataset = get_dataset()

with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.experimental_data_editor(dataset, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        #Note the quote_identifiers argument for case insensitivity
        session.write_pandas(edited, "avatar_wearables", overwrite=True, quote_identifiers=False)
        st.success("Table updated")
        time.sleep(5)
    except:
        st.warning("Error updating table")
    #display success message for 5 seconds and update the table to reflect what is in Snowflake
    st.experimental_rerun()

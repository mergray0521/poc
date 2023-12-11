import streamlit as st
import snowflake.connector
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

# Snowflake connection
my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

# Load data from Snowflake
query = "SELECT * FROM avatar_wearables"
df = pd.read_sql(query, my_cnx)

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")
st.title("Update Metadata")
st.caption("This is a demo of the `st.data_editor`.")

with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.data_editor(df, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        # Convert the edited format to the old format for compatibility
        edited_cells_old_format = {
            f"{row}:{col}": edited[row][col]
            for row in edited
            for col in edited[row]
        }
        
        # Write the edited cells back to Snowflake for the "avatar_wearables" table
        write_pandas(my_cnx, edited_cells_old_format, 'avatar_wearables', if_exists='replace')
        st.success("Table updated")
    except Exception as e:
        st.warning(f"Error updating table: {e}")

    # Display success message and update the table to reflect what is in Snowflake
    st.success("Data saved in Snowflake!")
    st.experimental_rerun()

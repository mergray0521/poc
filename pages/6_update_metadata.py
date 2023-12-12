import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

st.title("Update Metadata")

# Form for searching token
with st.form("search_token"):
    st.header("Select Token ID")
    search_token = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
    search = st.form_submit_button(label="Search")
    if not search and not st.session_state.get("Search"):
        st.stop()
    st.session_state["Search"] = True
    st.success(f"Update metadata for token: {search_token}")

# Form for updating token metadata
with st.form("update_metadata"):
    st.header("Update Token Metadata")
    token_id = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
    token_type = st.text_input('Token Type', "")
    materials = st.text_input('Materials', "")
    color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 
    update = st.form_submit_button(label="Update")
    if not update and not st.session_state.get("Update"):
        st.stop()

    # Connect to Snowflake
    my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
    my_cur = my_cnx.cursor()

    # Update the row in Snowflake
    query = f"UPDATE avatar_wearables SET TYPE = '{token_type}', MATERIALS = '{materials}', COLOR = '{color}' WHERE TOKEN_ID = {token_id}"
    my_cur.execute(query)
    my_cnx.commit()

    st.session_state["Update"] = True
    st.success(f"Updated token metadata and saved to Snowflake: {token_id}")

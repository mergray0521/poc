import streamlit as st
import snowflake.connector

st.title("Update Token Metadata")
with st.form("select_token"):
    st.header("Select Token")
    selected_token = st.selectbox('Token', ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"])
    search = st.form_submit_button(label="Search")
    if not search and not st.session_state.get("Search"):
        st.stop()
    st.session_state["Search"] = True
    st.success(f"Token schema submitted with: {token_schema}")


with st.form("mint_token"):
    st.header("Create New Token")
    token_id = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
    token_type = st.text_input('Token Type', "")
    materials = st.text_input('Materials', "")
    color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 
    mint = st.form_submit_button(label="Mint")
    if not mint and not st.session_state.get("Mint"):
        st.stop()

    #Connect to Snowflake
    my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
    my_cur = my_cnx.cursor()

    # Insert the form data into Snowflake
    query = f"INSERT INTO avatar_wearables (TOKEN_ID, TYPE, MATERIALS, COLOR) VALUES ('{token_id}','{token_type}', '{materials}', '{color}')"
    my_cur.execute(query)
    my_cnx.commit()
    
    st.session_state["Mint"] = True
    st.success(f"New Token Created and saved to Snowflake: {token_id}")













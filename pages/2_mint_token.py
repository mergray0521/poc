import streamlit as st
import snowflake.connector

st.title("Mint Token")
with st.form("token_schema"):
    st.header("Select Token Schema")
    token_schema = st.selectbox('Token Schema', ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"])
    search = st.form_submit_button(label="Search")
    if not search and not st.session_state.get("Search"):
        st.stop()
    st.session_state["Search"] = True
    st.success(f"Form 1 submitted with input: {token_schema}")


with st.form("mint_token"):
    st.header("Create New Token")
    token_id = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
    token_type = st.text_input('Token Type', "")
    materials = st.text_input('Materials', "")
    color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 
    mint = st.form_submit_button(label="Mint")
    if not mint:
        st.stop()
    st.session_state["Mint"] = False
    st.success(f"Form 2 submitted with input: {token_id}")

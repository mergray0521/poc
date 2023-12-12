import streamlit as st
import snowflake.connector

st.title("Test")
with st.form("form-1"):
    submitted_1 = st.form_submit_button(label="Submit")
    if not submitted_1 and not st.session_state.get("submission-1"):
        st.stop()
    st.session_state["submission-1"] = True
    st.write("1")
with st.form("form-2"):
    submitted_2 = st.form_submit_button(label="Submit")
    if not submitted_2:
        st.stop()
    st.session_state["submission-1"] = False
    st.write("2")

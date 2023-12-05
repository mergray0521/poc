import streamlit as st
import snowflake.connector

st.set_page_config(
    page_title="Homepage"
)

st.title('My Passport')
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
        st.session_state["my_input:] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)

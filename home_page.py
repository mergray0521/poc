import streamlit as st
import snowflake.connector

st.set_page_config(
    page_title="Homepage"
)

st.title('My Passport')
st.sidebar.success("Select a page above.")

admin_pages = ["1_create_token_schema.py", "2_mint_token.py", "3_assign_ownership.py", "4_display_tokens.py", "5_earned_token.py", "6_update_metadata.py"]
user_pages = ["4_display_tokens.py", "5_earned_token.py", "6_update_metadata.py"]


if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)



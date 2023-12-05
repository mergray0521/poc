import streamlit as st
import snowflake.connector

st.set_page_config(
    page_title="Homepage"
)

st.title('My Passport')
st.sidebar.success("Select a page above.")

admin_pages = ["1_create_token_schema.py", "2_mint_token.py", "3_assign_ownership.py", "4_display_tokens.py", "5_earned_token.py", "6_update_metadata.py"]
user_pages = ["4_display_tokens.py", "5_earned_token.py", "6_update_metadata.py"]

# Function to get or create session state
def get_session_state():
    if not hasattr(st.session_state, "role"):
        st.session_state.role = None
    return st.session_state
    
# Home Page
def home_page():
    st.title("Home Page")
    st.header("Choose your role:")

    # Radio button to choose role
    role = st.radio("Select Role", ["Admin", "User"])

    # Set session state role
    get_session_state().role = role

    # Continue button
    if st.button("Continue"):
        st.success(f"You selected {role} role. Proceed to {role} pages.")

# Function to display pages based on role
def display_pages():
    role = get_session_state().role

    if role == "Admin":
        pages = admin_pages
    elif role == "User":
        pages = user_pages
    else:
        pages = []

    return pages

# Main function
def main():
    get_session_state()
    home_page()

    # Display pages based on role
    pages = display_pages()
    if pages:
        selected_page = st.sidebar.selectbox("Select Page", pages)
        st.write(f"You are viewing {selected_page}.")

if __name__ == "__main__":
    main()


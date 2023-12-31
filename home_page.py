import streamlit as st

st.set_page_config(
    page_title="Homepage"
)

st.sidebar.success("Select a page above.")

admin_pages = ["1_create_token_schema.py", "2_mint_token.py", "3_assign_ownership.py", "4_display_points.py", "5_display_tokens.py", "6_update_metadata.py"]
user_pages = ["7_passport.py", "8_earn_points.py", "9_earn_tokens.py", "10_marketplace.py"]

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

        # List accessible pages
        accessible_pages = display_pages()
        st.info(f"Accessible Pages for {role}: {', '.join(accessible_pages)}")

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

if __name__ == "__main__":
    main()

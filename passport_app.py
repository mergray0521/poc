import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

# Function to create session state
def get_session_state():
    session_id = st.report_thread.get_report_ctx().session_id
    session_state = st.session_state.get(session_id=session_id, page="home")
    return session_state

# Page 1: Home
def home_page():
    st.title('My Passport')
    st.header("Home Page Content")
    # Add content for the home page if needed

# Page 2: Token Information Form
def token_info_page():
    st.title('Create Token Schema')
    st.header("Token Information Form")

    # Create input fields for token information
    token_name = st.text_input("Token Name", "")
    fungibility = st.selectbox("Fungibility", ["Fungible", "Non-Fungible", "Semi-Fungible"])
    ip = st.selectbox("IP", ["HTTYD", "HHN", "CINEPHILE", "TOOTHSOME"])
    token_admin = st.selectbox("Token Admin", ["Micah", "Steve", "Mere"])
    metadata = st.text_area("Metadata", "")

    # Submit button
    if st.button("Submit"):
        # Process the form data (you can replace this with your logic)
        result = {
            "Token Name": token_name,
            "Fungibility": fungibility,
            "IP": ip,
            "Token Admin": token_admin,
            "Metadata": metadata
        }

        # Display the result
        st.success("Form submitted successfully!")
        st.write("Result:")
        st.write(result)

# Main function to switch between pages
def main():
    session_state = get_session_state()

   # Navigation
    pages = ["Home", "Token Information Form"]
    selected_page = st.sidebar.radio("Navigation", pages)

    # Display selected page
    if selected_page == "Home":
        home_page()
    elif selected_page == "Token Information Form":
        token_info_page()

if __name__ == "__main__":
    main()

sys.exit()

try:
        # Insert the form data into Snowflake
        query = f"INSERT INTO token_schemas (token_name, fungibility, ip, token_admin, metadata) VALUES ('{token_name}', '{fungibility}', '{ip}', '{token_admin}', '{metadata}')"
        my_cursor.execute(query)
        my_cnx.commit()
        st.success("Data successfully inserted into Snowflake database!")
except Exception as e:
        st.error(f"Error inserting data into Snowflake: {e}")


  

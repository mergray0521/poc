import streamlit as st
from streamlit.report_thread import get_report_ctx
import snowflake.connector

# Function to create session state
def get_session_state():
    session_id = get_report_ctx().session_id
    session_state = st.session_state.get(session_id=session_id, page=1)
    return session_state

# Function to switch between pages
def page_navigation():
    st.sidebar.title("Navigation")
    pages = ["Page 1", "Page 2"]
    selected_page = st.sidebar.radio("Go to", pages)
    return selected_page

# Page 1 content
def page1():
    st.title("Page 1")
    st.write("This is the content of Page 1.")
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

st.title('Create Token Schema')

def main():
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

if __name__ == "__main__":
    main()

# Page 2 content
def page2():
    st.title("Page 2")
    st.write("This is the content of Page 2.")
    # Add Page 2 specific content here

# Main function
def main():
    session_state = get_session_state()

    if session_state.page == 1:
        page1()
    elif session_state.page == 2:
        page2()

    selected_page = page_navigation()

    if selected_page == "Page 1" and session_state.page != 1:
        session_state.page = 1
    elif selected_page == "Page 2" and session_state.page != 2:
        session_state.page = 2

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


  

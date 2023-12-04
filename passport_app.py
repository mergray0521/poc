import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Passport')
streamlit.header('Create Token Schema')


def main():
    st.title("Token Schema Form")

    # Create input fields for token information
    token_name = st.text_input("Token Name", "")
    fungibility = st.selectbox("Fungibility", ["Fungible", "Non-Fungible"])
    ip = st.text_input("IP Address", "")
    token_admin = st.text_input("Token Admin", "")
    metadata = st.text_area("Metadata", "")

    # Submit button
    if st.button("Submit"):
        # Process the form data (you can replace this with your logic)
        result = {
            "Token Name": token_name,
            "Fungibility": fungibility,
            "IP Address": ip,
            "Token Admin": token_admin,
            "Metadata": metadata
        }

        # Display the result
        st.success("Form submitted successfully!")
        st.write("Result:")
        st.write(result)

if __name__ == "__main__":
    main()

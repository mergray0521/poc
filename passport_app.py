import streamlit as st
import snowflake.connector

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


try:
        # Insert the form data into Snowflake
        query = f"INSERT INTO token_schemas (token_name, fungibility, ip, token_admin, metadata) VALUES ('{token_name}', '{fungibility}', '{ip}', '{token_admin}', '{metadata}')"
        my_cursor.execute(query)
        my_cnx.commit()
        st.success("Data successfully inserted into Snowflake database!")
except Exception as e:
        st.error(f"Error inserting data into Snowflake: {e}")


  

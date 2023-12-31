import streamlit as st
import snowflake.connector

st.set_page_config(
    page_title="Create Token Schema"
)

st.title('Create Token Schema')

my_cnx = snowflake.connector.connect(**st.secrets["token_schemas"])
my_cur = my_cnx.cursor()

def main():
    st.header("Token Information Form")

    # Create input fields for token information
    token_schema_id = st.number_input("Token Schema ID", min_value=15, max_value=1000, value=15, step=1)
    token_name = st.text_input("Token Name", "")
    fungibility = st.selectbox("Fungibility", ["Fungible", "Non-Fungible", "Semi-Fungible"])
    ip = st.selectbox("IP", ["HTTYD", "HHN", "CINEPHILE", "TOOTHSOME", "MINIONS"])
    token_admin = st.selectbox("Token Admin", ["Micah", "Steve", "Mere"])
    metadata = st.text_area("Metadata", "")

    # Submit button
    if st.button("Submit"):
        # Process the form data
        result = {
            "Token Id": token_schema_id,
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

        # Insert the form data into Snowflake
        query = f"INSERT INTO token_schemas (TOKEN_SCHEMA_ID,TOKEN_NAME, FUNGIBILITY, IP, TOKEN_ADMIN, METADATA) VALUES ('{token_schema_id}','{token_name}', '{fungibility}', '{ip}', '{token_admin}', '{metadata}')"
        my_cur.execute(query)
        my_cnx.commit()
        st.success("Data saved in snowflake!")

if __name__ == "__main__":
    main()
        

  

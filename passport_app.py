import streamlit as st
import snowflake.connector 

streamlit.title ('Welcome to Passport')
streamlit.header('Create Token Schema')

# Function to update Snowflake database
def update_database(token_name, fungibility, ip, token_admin, metadata):
    # Replace these with your Snowflake credentials
    user = 'Mergray0521'
    password = 'Lakegage0521!'
    account = 'CNAHFEW.KNB62637.snowflakecomputing.com'
    warehouse = 'compute_wh'
    database = 'token_schemas'
    schema = 'token_schemas'

    # Establish a connection to Snowflake
    con = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )

# Create a cursor object
    cursor = con.cursor()

# SQL query to insert data into token_schema table
    query = f"INSERT INTO token_schema (token_name, fungibility, ip, token_admin, metadata) " \
            f"VALUES ('{token_name}', '{fungibility}', '{ip}', '{token_admin}', '{metadata}')"

    # Execute the query
    cursor.execute(query)

    # Commit the changes
    con.commit()

    # Close the cursor and connection
    cursor.close()
    con.close()

# Streamlit app
def main():
    st.title("Token Schema Creator")

    # Form fields
    token_name = st.text_input("Token Name")
    fungibility = st.selectbox("Fungibility", ["Fungible", "Non-Fungible"])
    ip = st.text_input("IP")
    token_admin = st.text_input("Token Admin")
    metadata = st.text_area("Metadata")

    # Submit button
    if st.button("Create Token Schema"):
        # Validate if required fields are not empty
        if token_name and fungibility and ip and token_admin:
            # Update Snowflake database
            update_database(token_name, fungibility, ip, token_admin, metadata)
            st.success("Token Schema created successfully!")
        else:
            st.error("Please fill in all required fields.")

if __name__ == "__main__":
    main()


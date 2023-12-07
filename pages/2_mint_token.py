import streamlit as st
import snowflake.connector

st.title("Select Token Schema")

my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

def fetch_token_schemas():
    query = "SELECT * FROM inventory_db"  
    my_cur.execute(query)
    result_data = my_cur.fetchall()
    return [table[1] for table in result_data]

# Call the function to get token schemas
schema_options = fetch_token_schemas()

# Create dropdown
selected_schema = st.selectbox("Select Token Schema", schema_options)

if __name__ == "__fetch_token_schemas__":
    fetch_token_schemas()

def main():
    st.header("Mint Token")

    # Create input fields for token information
    token_id = st.number_input("Token Schema ID", min_value=606, max_value=1000, value=606, step=1)
    token_type = st.text_input("Token Name", "")
    materials = st.text_input("Materials", "")
    color = st.selectbox("Color", ["green", "black", "silver", "red", "brown"])

    # Submit button
    if st.button("Submit"):
        # Process the form data (you can replace this with your logic)
        result = {
            "Token Id": token_id,
            "Token Type": token_type,
            "Materials": materials,
            "Color": color
            }
    
        # Display the result
        st.success("Form submitted successfully!")
        st.write("Result:")
        st.write(result)

        # Insert the form data into Snowflake
        query = f"INSERT INTO avatar_wearables (TOKEN_ID,TOKEN_TYPE, MATERIALS, COLOR) VALUES ('{token_id}','{token_type}', '{materials}', '{color}')"
        my_cur.execute(query)
        my_cnx.commit()
        st.success("Data saved in snowflake!")

if __name__ == "__main__":
    main()
        

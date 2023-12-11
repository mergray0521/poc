import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["token_schemas"])
my_cur = my_cnx.cursor()

# Function to fetch token data from the database
def fetch_token_data(token_id, type):
    # Your code to fetch data from Snowflake database
    # Replace this with your actual implementation
    token_data = {
        'image_url': 'path/to/token_image.png',
        'type': token_type,
        'materials': 'aerium_fabric',
        'color': 'fabric'
    }
    return token_data

# Function to update ownership database
def update_ownership_database(user_id, token_id):
    # Your code to update the ownership database goes here
    pass

# Main Streamlit app
def main():
    st.title("Flying Harness Token Page")

    # Display pop-up notification
    st.success("Congratulations! You earned a new Flying Harness token!")

    # Fetch and display token information
    token_data = fetch_token_data(605, 'flying_harness')
    st.image(token_data['image_url'])
    st.write(f"Type: {token_data['type']}")
    st.write(f"Materials: {token_data['materials']}")
    st.write(f"Color: {token_data['color']}")

    # Collect button and ownership update
    if st.button('Collect'):
        # Assuming you have a user_id variable
        user_id = 123  # Replace with the actual user ID
        update_ownership_database(user_id, 605)
        st.success(f"You now own the Flying Harness token!")

# Run the app
if __name__ == '__main__':
    main()



import streamlit as st
import pandas as pd
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.title("Display Tokens")

# Input user ID
user_id = st.text_input("Enter User ID:")

if st.button("Submit"):
    if user_id:

        # Query the token_ownership table and join with token_images 
        query = f"""
            SELECT to.token_id, ti.image_url
            FROM token_ownership to
            JOIN token_images ti ON to.token_id = ti.token_id
            WHERE to.owner_id = '{user_id}'
        """
    
        
        if result:
            st.success(f"Tokens for User ID {user_id}:")
        
            # Create a three-column layout
            col1, col2, col3 = st.columns(3)
        
            for token_id, image_url in result:
                # Display image and caption in each column
                with col1:
                    st.image(image_url, caption=f"Token ID: {token_id}", use_column_width=True)
                # Repeat for col2 and col3
        else:
            st.warning(f"No tokens found for User ID {user_id}")
            
    



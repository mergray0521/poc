import streamlit as st
import snowflake.connector
import pandas as pd

def main():
    
    st.title("Select Token Schema")
    
    token_schema_options = ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"]
    selected_token_schema = st.selectbox("Token Schema", token_schema_options)
    
    if st.button("Search"):
        my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
        my_cur = my_cnx.cursor()

        st.header("Create New Token")
            
        # Create form for token information
        with st.form("mint_token"):
            token_id = st.number_input('Token ID"', min_value=606, max_value=1000, value=606, step=1)
            type = st.text_input('Token Type', "")
            materials = st.text_input('Materials', "")
            color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 
            mint_button_clicked = st.form_submit_button('Mint')
      
        if mint_button_clicked:           
            # Insert the form data into Snowflake
            query = f"INSERT INTO avatar_wearables (TOKEN_ID, TYPE, MATERIALS, COLOR) VALUES ('{token_id}', '{type}', '{materials}', '{color}')"
            my_cur.execute(query)
            my_cnx.commit()
            st.success("New token minted!")
            
if __name__ == "__main__":
    main()






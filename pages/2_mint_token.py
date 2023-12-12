import streamlit as st
import snowflake.connector
import pandas as pd

def main():
    
    st.title("Mint Token")

    # Connect to Snowflake
    my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
    my_cur = my_cnx.cursor()

    # form 1 for token schema selection
    with st.form("Token Schema"):
        st.header("Token Schema")
        token_schema = st.selectbox('Token Schema', ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"])
        search = st.form_submit_button("Search")

    if search:
        st.success(f"Form 1 submitted with input: {token_schema}")

        # form 2 for token information
        with st.form("Mint Token"):
            token_id = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
            token_type = st.text_input('Token Type', "")
            materials = st.text_input('Materials', "")
            color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 
            mint = st.form_submit_button("Mint")

        if mint:
            # Insert the form data into Snowflake
            query = f"INSERT INTO avatar_wearables (TOKEN_ID, TYPE, MATERIALS, COLOR) VALUES ('{token_id}','{token_type}', '{materials}', '{color}')"
            my_cur.execute(query)
            my_cnx.commit()
            
if __name__ == "__main__":
    main()

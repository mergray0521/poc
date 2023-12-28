import streamlit as st
import pandas as pd
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.header("Earned New Token") 
st.text("Congrats on collecting a My Way Token!")
st.text("This influence token allows you to vote on Universal polls + topics.")

image_url = "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true"
st.image(image_url, caption="Token: My Way", use_column_width=True)

if st.button("Collect"):
    # Insert the form data into Snowflake
    query = f"INSERT INTO token_ownership (TOKEN_ID, OWNER_ID, QUANTITY) VALUES ('{605}','{3}', '{1}')"
    my_cur.execute(query)
    my_cnx.commit()
    st.success(f"My Way token added to user {1}'s wallet")





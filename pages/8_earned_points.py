import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.header("Earned Points") 
st.text("You’ve earned 50 Park points for your latest park visit! Redeem your points now for the Park Pro Token!")

image_url = "https://i.pinimg.com/originals/4f/72/64/4f7264966212744a1302d8c960abe398.jpg"
st.image(image_url, caption="+50 points", use_column_width=True)

if st.button("Collect"):
    # Insert the form data into Snowflake
    query = f"INSERT INTO token_ownership (TOKEN_ID, OWNER_ID, QUANTITY) VALUES ('{605}','{3}', '{1}')"
    my_cur.execute(query)
    my_cnx.commit()
    st.success(f"50 points added to user {3}'s wallet")
    st.text("Proceed to marketplace page to redeem")

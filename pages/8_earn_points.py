import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.header("Earned Points") 
st.text("You’ve earned 50 points for completing an In-Park AR challenge! Redeem your points.")

image_url = "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(15).png?raw=true"
st.image(image_url, caption="+50 points", use_column_width=True)

user_id = 1

# Retrieve current point_quantity for user_id = 1
query_select = f"SELECT point_quantity FROM point_ownership WHERE user_id = '{user_id}'"
my_cur.execute(query_select)
current_points = my_cur.fetchone()

current_points = current_points[0] if current_points else 0

if st.button("Collect"):
    # Calculate new points
    new_points = current_points + 50

    # Update the row in Snowflake with the new value
    query_update = f"UPDATE point_ownership SET point_quantity = '{new_points}' WHERE user_id = '{user_id}'"
    my_cur.execute(query_update)
    my_cnx.commit()

    st.success(f"50 points added to user {user_id}'s wallet")
    st.text(f"Total points now: {new_points}")
    st.text("Proceed to the marketplace page to redeem") 


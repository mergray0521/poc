import requests
import streamlit as st
import snowflake.connector

# Your database connection
my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.header("Token Marketplace")
css_code = """
    <style>
        .custom-container {
            border: 2px solid #1f618d;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 200px;
        }

        .custom-image {
            width: 80%;
            border-radius: 5px;
            height: 150px;
        }

    </style>
"""

# Token details
tokens = [
    {"name": "My Say", "token_id": "1201", "token_cost": 1000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true"},
    {"name": "My Way", "token_id": "1301", "token_cost": 2000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(17).png?raw=true"},
    {"name": "My Day", "token_id": "1402", "token_cost": 3000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(15).png?raw=true"},
    {"name": "Park Ticket", "token_id": "1002", "token_cost": 4000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/ticket.png?raw=true"},
    {"name": "Trained Dragon", "token_id": "401", "token_cost": 4000, "image_url": "https://cdn.dribbble.com/users/1061278/screenshots/14605165/media/f27c0bfd48d70f3aa755d3617b287f3e.png?resize=400x300&vertical=center"},
    {"name": "Dragon Egg", "token_id": "108", "token_cost": 3000, "image_url": "https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Dragon_Egg-512.png"},
]

user_id = 1

# Function to handle button click
def handle_purchase(token):
    # 1. Get User Points
    user_points_query = f"SELECT point_quantity FROM point_ownership WHERE user_id = {user_id}"
    my_cur.execute(user_points_query)
    user_points = my_cur.fetchone()[0]

    # 2. Check Sufficient Points
    if user_points >= token["token_cost"]:
        # 3. Update Point Ownership
        new_points = user_points - token["token_cost"]
        update_points_query = f"UPDATE point_ownership SET point_quantity = {new_points} WHERE user_id = {user_id}"
        my_cur.execute(update_points_query)
        # 4. Insert Token Ownership
        insert_token_query = f"INSERT INTO token_ownership (owner_id, token_id, quantity, name) VALUES ({user_id}, '{token['token_id']}', 1, '{token['name']}')"
        my_cur.execute(insert_token_query)
        st.success(f"You have successfully purchased token {token['token_id']}!")
    else:
        st.error("Insufficient points to purchase this token.")

# Create 3 columns and two rows
c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with st.container():
    for col, token in zip([c1, c2, c3, c4, c5, c6], tokens):
        with col:
            col.markdown(css_code, unsafe_allow_html=True)
            col.markdown(f'<div class="custom-container"><img src="{token["image_url"]}" alt="{token["name"]}" class="custom-image"><p>{token["name"]} - {token["token_cost"]} points</p></div>', unsafe_allow_html=True)
            
            # Move the st.button block inside the container loop
            if st.button(f'Purchase {token["name"]} - {token["token_cost"]} points', key=f'purchase_button_{token["name"]}'):
                handle_purchase(token)

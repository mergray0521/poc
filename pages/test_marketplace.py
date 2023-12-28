import requests
import streamlit as st
import snowflake.connector

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
            height: 280px;
        }

        .custom-image {
            width: 80%;
            border-radius: 5px;
            height: 150px;
        }

        .custom-button {
            margin-top: 10px;
            border: 2px solid #429DF5;
        }
    </style>
"""

# Token details
tokens = [
    {"name": "My Say Token", "cost": 1000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true"},
    {"name": "My Way Token", "cost": 2000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(17).png?raw=true"},
    {"name": "My Day Token", "cost": 3000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(15).png?raw=true"},
    {"name": "Park Ticket", "cost": 4000, "image_url": "https://github.com/mergray0521/poc/blob/main/images/ticket.png?raw=true"},
    {"name": "Dragon", "cost": 4000, "image_url": "https://cdn.dribbble.com/users/1061278/screenshots/14605165/media/f27c0bfd48d70f3aa755d3617b287f3e.png?resize=400x300&vertical=center"},
    {"name": "Hatching Egg", "cost": 3000, "image_url": "https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Dragon_Egg-512.png"},
]

user_id = 1

# Function to handle button click
def handle_purchase(token_name, token_cost):
    # 1. Get User Points
    user_points_query = f"SELECT point_quantity FROM point_ownership WHERE user_id = {user_id}"
    my_cur.execute(user_points_query)
    user_points = my_cur.fetchone()[0]

    # 2. Check Sufficient Points
    if user_points >= token_cost:
        # 3. Update Point Ownership
        new_points = user_points - token_cost
        update_points_query = f"UPDATE point_ownership SET point_quantity = {new_points} WHERE user_id = {user_id}"
        my_cur.execute(update_points_query)
        # 4. Insert Token Ownership
        insert_token_query = f"INSERT INTO token_ownership (owner_id, token_id, quantity) VALUES ({user_id}, '{token_name}', 1)"
        my_cur.execute(insert_token_query)
        st.success(f"You have successfully purchased {token_name}!")
    else:
        st.error("Insufficient points to purchase this token.")

# Create 3 columns and two rows
c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with st.container(): 
    for col, token in zip([c1, c2, c3, c4, c5, c6], tokens): 
        with col:
            col.markdown(css_code, unsafe_allow_html=True)
            col.image(token["image_url"], width=200)
            col.markdown(f"<p>{token['name']} - {token['cost']} points</p>", unsafe_allow_html=True)
            if col.button(f"Purchase {token['name']}"):
                handle_purchase(token["name"], token["cost"])

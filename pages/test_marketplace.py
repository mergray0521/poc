import requests
import streamlit as st
import snowflake.connector

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

# Token cost dictionary
token_costs = {
    "My Say Token": 1000,
    "My Way Token": 2000,
    "My Day Token": 3000,
    "Minion Glasses": 4000,
    "Dragon": 4000,
    "Hatching Egg": 3000,
}


user_id = 1

# Function to handle button click
def handle_purchase(token_name, token_cost):
    # 1. Get User Points
    user_points_query = f"SELECT point_quantity FROM point_ownership WHERE user_id = {user_id}"
    with connection.cursor() as cursor:
        cursor.execute(user_points_query)
        user_points = cursor.fetchone()[0]

    # 2. Check Sufficient Points
    if user_points >= token_cost:
        # 3. Update Point Ownership
        new_points = user_points - token_cost
        update_points_query = f"UPDATE point_ownership SET point_quantity = {new_points} WHERE user_id = {user_id}"
        with connection.cursor() as cursor:
            cursor.execute(update_points_query)
        # 4. Insert Token Ownership
        insert_token_query = f"INSERT INTO token_ownership (owner_id, token_id, quantity) VALUES ({user_id}, '{token_name}', 1)"
        with connection.cursor() as cursor:
            cursor.execute(insert_token_query)
        st.success(f"You have successfully purchased {token_name}!")
    else:
        st.error("Insufficient points to purchase this token.")


# Assuming you have defined st.container somewhere in your code
with st.container():
    c1, c2, c3 = st.columns(3)
    for col, token_name in zip([c1, c2, c3], ["My Say Token", "My Way Token", "My Day Token"]):
        with col:
            col.markdown(css_code, unsafe_allow_html=True)
            html_code_token = f"""
                <div class="custom-container">
                    <img src="https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true" alt="{token_name}" class="custom-image">
                    <p>{token_costs[token_name]} points</p>
                    <button class="custom-button" onclick="handle_purchase('{token_name}', {token_costs[token_name]})">Purchase {token_name}</button>
                </div>
            """
            col.markdown(html_code_token, unsafe_allow_html=True)

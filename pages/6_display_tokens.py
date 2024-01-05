import streamlit as st
import pandas as pd
import snowflake.connector

# Your database connection
my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

css_code = """
    <style>
         .custom-container {
            border: 2px solid #1f618d;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 220px;
        }

        .custom-image {
            margin-top: 10px;
            width: 80%;
            border-radius: 5px;
            height: 150px;
        }
    </style>
"""

st.title("Display Tokens")

# Input user ID
user_id = st.text_input("Enter User ID:")

if st.button("Submit"):
    if user_id:
        # Query the token_ownership table
        query = f"SELECT token_id FROM token_ownership WHERE owner_id = '{user_id}'"
        my_cur.execute(query)
        result = my_cur.fetchall()

        # Display the result in Streamlit
        if result:
            st.success(f"Tokens for User ID {user_id}:")
            tokens_df = pd.DataFrame(result, columns=["token_id"])

            tokens = [
                {"name": "Dragon Egg", "token_id": "101", "image_url": "https://cdn3.iconfinder.com/data/icons/fantasy-and-role-play-game-adventure-quest/512/Dragon_Egg-512.png"},
                {"name": "Healing Herbs", "token_id": "803", "image_url": "https://cdn-icons-png.flaticon.com/512/628/628283.png"},
                {"name": "Park Ticket", "token_id": "1002", "image_url": "https://github.com/mergray0521/poc/blob/main/images/ticket.png?raw=true"},
                {"name": "Hotel Key", "token_id": "1101", "image_url": "https://github.com/mergray0521/poc/blob/main/images/key.png?raw=true"},
                {"name": "My Say", "token_id": "1201", "image_url": "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true"}
            ]

            # Display images and captions in three columns
            cols = st.columns(3)
            for row in range((len(tokens) + 2) // 3):
                with st.container():
                    for col in cols:
                        token_index = row * 3 + cols.index(col)
                        if token_index < len(tokens):
                            token = tokens[token_index]
                            with col:
                                st.markdown(css_code, unsafe_allow_html=True)
                                html_code_col = f"""
                                    <div class="custom-container">
                                        <img src="{token['image_url']}" class="custom-image">
                                        <p>{token['name']} - Token ID: {token['token_id']}</p>
                                    </div>
                                """
                                st.markdown(html_code_col, unsafe_allow_html=True)

        else:
            st.warning(f"No tokens found for User ID {user_id}")

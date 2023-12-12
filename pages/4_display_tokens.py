import streamlit as st
import pandas as pd
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

#sample dictionary with Token IDs + Image URLs
token_images = {
    "Token_103": "https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg",
    "Token_204": "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
    "Token_305": "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg",
    "Token_404": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4Hn_yZ08PhDB_HnlRhJ4V4cjp3ian_g2RGA&usqp=CAU",
    "Token_602": "https://static.wikia.nocookie.net/vsbattles/images/d/da/Kisspng-phil-the-minion-birthday-minions-despicable-me-cli-minion-5abb7634ceab95.0695696415222349328465.png/revision/latest?cb=20180916000856",
    "Token_703": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTw-W7q0UwDMFFRhdboyw3xaSvi0Pws7Ubh2cCa2BtcDj3gS4jniRaZUbfsgrK-UXeHyZs&usqp=CAU",
    "Token_605": "https://i.etsystatic.com/31006011/r/il/7726c6/3265064700/il_fullxfull.3265064700_ldzy.jpg"
}

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

            # Create a three-column layout
            col1, col2, col3 = st.beta_columns(3)

            for token_id in result:
                if token_id in token_images:
                    # Display image and caption in each column
                    with col1:
                        st.image(token_images["Token_103"], caption=f"Token ID: 103", use_column_width=True)
                        st.image(token_images["Token_204"], caption=f"Token ID: 204", use_column_width=True)
                        st.image(token_images["Token_305"], caption=f"Token ID: 305", use_column_width=True)
                    with col2:
                        st.image(token_images["Token_404"], caption=f"Token ID: 404", use_column_width=True)
                        st.image(token_images["Token_602"], caption=f"Token ID: 602", use_column_width=True)
                    with col3:
                        st.image(token_images["Token_703"], caption=f"Token ID: 703", use_column_width=True)
                        st.image(token_images["Token_605"], caption=f"Token ID: 605", use_column_width=True)
                else:
                    st.warning(f"No image found for Token ID {token_id}")
        else:
            st.warning(f"No tokens found for User ID {user_id}")

    



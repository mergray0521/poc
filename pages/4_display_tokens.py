import streamlit as st
import pandas as pd
import snowflake.connector

# Your database connection
my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

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
            tokens_df = pd.DataFrame(result, columns=["Token ID"])

            # Manually code image URLs for a few tokens
            image_urls = {
                "token1": "https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg",
                "token2": "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
                "token3": "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg",
                # Add more as needed
            }

            # Display images and captions in three columns
            cols = st.beta_columns(3)
            for index, row in tokens_df.iterrows():
                token_id = row["Token ID"]
                
                if f"token{token_id}" in image_urls:
                    image_url = image_urls[f"token{token_id}"]
                    caption = f"Token ID: {token_id}"

                    with cols[index % 3]:
                        st.image(image_url, caption=caption, use_container_width=True)
                else:
                    st.warning(f"No image URL found for Token ID: {token_id}")

        else:
            st.warning(f"No tokens found for User ID {user_id}")

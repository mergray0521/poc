import streamlit as st
import pandas as pd
import snowflake.connector

# Your database connection
my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

css_code = """
    <style>
        .custom-container {
            border: 2px solid #DCDCDC;
            background: #DCDCDC;
            padding: 5% 5% 5% 10%;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 350px;
        }

        .custom-image {
            width: 100%;
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
            tokens_df = pd.DataFrame(result, columns=["Token ID"])

            # Manually code image URLs for a few tokens
            image_urls = {
                101: "https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg",
                107: "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
                108: "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg",
                201: "https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg",
                301: "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
                303: "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg",
                503: "https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg",
                504: "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
                701: "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg",
                803: "https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg",
                600: "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
                1001: "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg",
                1101: "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
                1102: "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg"
            }

            # Display images and captions in three columns
            cols = st.columns(3)
            list_ids = []
            for index, row in tokens_df.iterrows():
                token_id = row["Token ID"]
                id = token_id % 1000  # Extract the last three digits of the token_id
                list_ids.append(id)

            for col in cols:
                for id in list_ids:
                    if id in image_urls.keys():
                        url = image_urls[id]
                        with col:
                            st.markdown(css_code, unsafe_allow_html=True)
                            html_code_col = f"""
                                <div class="custom-container">
                                    <img src="{url}" class="custom-image">
                                    <p>Token ID: {id}</p>
                                </div>
                            """
                            st.markdown(html_code_col, unsafe_allow_html=True)
                    else:
                        st.warning(f"No image URL found for Token ID: {id}")

        else:
            st.warning(f"No tokens found for User ID {user_id}")

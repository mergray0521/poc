import streamlit as st
import requests
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
            padding:  5% 5% 5% 10%;
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
            img_103="https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg"
            img_204="https://cdn-icons-png.flaticon.com/512/5169/5169269.png"
            img_305="https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg"
            image_urls = {
                103: "https://t3.ftcdn.net/jpg/03/40/50/48/360_F_340504802_pm6pOI5JAGJhNVLTntkGnX2S9oFe7Ncn.jpg",
                204: "https://cdn-icons-png.flaticon.com/512/5169/5169269.png",
                305: "https://i.pinimg.com/736x/58/92/f0/5892f0f20598882750a70dda52078ab0.jpg"
            }
            # Display images and captions in three columns
            c1, c2, c3 = st.columns(3)
            c4, c5, c6 = st.columns(3)
            list_ids = []
            for index, row in tokens_df.iterrows():
                token_id = row["Token ID"]
                tokenID=f"token{token_id}"
                id=tokenID[slice(5, 8)]
                list_ids.append(id)
            st.text(list_ids)
            with st.container():
                for col in [c1, c2, c3]:
                    st.text(tokenID)
                    st.text(id)
                    for id in list_ids:                        
                        if id in image_urls.keys():
                            url=image_urls[id_img] 
                            st.text(url)
                            if col == c1:
                                with col:                               
                                    c1.markdown(css_code, unsafe_allow_html=True)
                                    html_code_col1 = """
                                        <div class="custom-container">
                                            <img src={{url}} class="custom-image">
                                            <p>Token ID: </p> <p> {{id}} </p>
                                        </div>
                                    """
                                    c1.markdown(html_code_col1, unsafe_allow_html=True)

                            if col == c2:
                                with col:
                                    c2.markdown(css_code, unsafe_allow_html=True)
                                    html_code_col2 = """
                                        <div class="custom-container">
                                            <img src={{url}} class="custom-image">
                                            <p>Token ID: ' + id+ '</p>
                                        </div>
                                    """
                                    c2.markdown(html_code_col2, unsafe_allow_html=True)
                            else:
                                st.warning(f"No col matching URL found for Token ID: {token_id}")
                    # with cols[index % 3]:
                    #     st.image(image_url, caption=caption, use_container_width=True)
                        else:
                            st.warning(f"No image URL found for Token ID: {token_id}")

        # else:
        #     st.warning(f"No tokens found for User ID {user_id}")

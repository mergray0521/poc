import streamlit as st
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

st.title("Assign Token Ownership")

def assign_ownership(token_id, identity_id):
  ownership_query = f"INSERT INTO ownership_db.token_ownership (token_id, owner_id) VALUES ('{token_id}', {identity_id})"
  my_cur.execute(ownership_query)
  my_cnx.commit() 
  st.success(f"Ownership assigned! Token ID {token_id} is now owned by {identity_id}.")

st.title("Assign Ownership")

inventory_query = "SELECT token_id FROM inventory_db.avatar_wearables"
identity_query = "SELECT user_id FROM identity_db.user_identity"

try:
    # Get token IDs from the 'inventory_db'
    token_ids = my_cur.execute(inventory_query).fetchall()
    token_id_options = [str(token[0]) for token in token_ids]

    # Get user identities from the 'identity_db'
    identity_ids = my_cur.execute(identity_query).fetchall()
    identity_id_options = [str(user[0]) for user in identity_ids]

    # Dropdowns for token ID and user identity
    token_id = st.selectbox("Select Token ID:", token_id_options)
    identity_id = st.selectbox("Select User Identity:", identity_id_options)

    # Assign Ownership button
    if st.button("Assign Ownership"):
        assign_ownership(token_id, user_identity)


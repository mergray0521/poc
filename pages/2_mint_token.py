import streamlit as st
import snowflake.connector

# Function to get or create session state
@st.cache(allow_output_mutation=True)
def get_session_state():
    return {"form_1_submitted": False, "form_2_submitted": False}

def main():
    st.title("Mint Token")

    # Get or create session state
    session_state = get_session_state()

    # form 1 for token schema selection
    with st.form("Token Schema"):
        st.header("Token Schema")
        token_schema = st.selectbox('Token Schema', ["avatar wearables", "dragon egg", "egg feathers", "egg nests", "healing herbs", "sketchbook", "star maps", "trained dragon", "weapons"])
        search = st.form_submit_button("Search")

    if search:
        session_state["form_1_submitted"] = True
        st.success(f"Form 1 submitted with input: {token_schema}")

    # form 2 for token information
    if session_state["form_1_submitted"]:
        with st.form("Mint Token"):
            token_id = st.number_input('Token ID', min_value=606, max_value=1000, value=606, step=1)
            token_type = st.text_input('Token Type', "")
            materials = st.text_input('Materials', "")
            color = st.selectbox('Color', ["Green", "Black", "Silver", "Red", "Brown"]) 

            # Check for form 2 submission
            if st.form_submit_button("Mint"):
                # Connect to Snowflake
                my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
                my_cur = my_cnx.cursor()

                # Insert the form data into Snowflake
                query = f"INSERT INTO avatar_wearables (TOKEN_ID, TYPE, MATERIALS, COLOR) VALUES ('{token_id}','{token_type}', '{materials}', '{color}')"
                my_cur.execute(query)
                my_cnx.commit()
                st.success(f"Form 2 submitted with input: {token_id, token_type, materials, color}")

if __name__ == "__main__":
    main()


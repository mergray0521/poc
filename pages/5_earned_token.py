import streamlit as st
import snowflake.connector

st.title("Earned Token")
st.header("Congratulations you have earned a flying harness!") 






  if st.button("Collect"):
                    
            # Insert the form data into Snowflake
            query = f"INSERT INTO avatar_wearables (TOKEN_ID,TYPE, MATERIALS, COLOR) VALUES ('{token_id}','{type}', '{materials}', '{color}')"
            my_cur.execute(query)
            my_cnx.commit()
            st.success("New token collected!")
            

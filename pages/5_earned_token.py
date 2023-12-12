import streamlit as st
from streamlit_modal import Modal
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["token_schemas"])
my_cur = my_cnx.cursor()

st.header("Earned Token") 

modal = Modal(key="Demo Key",title="test")
for col in st.columns(8):
    with col:
        open_modal = st.button(label='button')
        if open_modal:
            with modal.container():
                st.markdown('testtesttesttesttesttesttesttest')








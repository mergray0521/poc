import streamlit as st
import snowflake.connector

st.title("Mint Token")

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

def main():
    st.header("Select Token Schema")

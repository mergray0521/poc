import streamlit as st
import pandas
import requests
import snowflake.connector

    # Connect to Snowflake
    my_cnx = connect_to_snowflake()

    


streamlit.title('My Passport')
streamlit.header('Create Token Schema')


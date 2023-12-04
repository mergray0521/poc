import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Passport')
streamlit.header('Create Token Schema')

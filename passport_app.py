import streamlit 
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()


my_cur.execute("select * from token_schemas")
my_data_rows = my_cur.fetchall()
streamlit.text("Current token schemas include:")
streamlit.text(my_data_rows)




  

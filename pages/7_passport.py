import streamlit as st
import pandas as pd
import snowflake.connector


# Ownership db connection
my_cnx = snowflake.connector.connect(**st.secrets["TOKEN_OWNERSHIP"])
my_cur = my_cnx.cursor()

# Inventory db connection
my_cnx2 = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur2 = my_cnx2.cursor()

#Define user
user_id = 1

# Query the point_ownership table 
query = f"SELECT user_id, point_quantity FROM point_ownership WHERE user_id = '{user_id}'"
my_cur.execute(query)
result = my_cur.fetchall()

# Grab result to reference as variable in html/ container
if result:
   points_df = pd.DataFrame(result, columns=["User_ID", "Point_Quantity"])

point_quantity_value = points_df["Point_Quantity"].iloc[0] if not points_df.empty else "N/A"


# Query the token_ownership table for token names
token_query = f"SELECT token_name FROM token_ownership WHERE owner_id = '{user_id}'"
my_cur.execute(token_query)
token_result = my_cur.fetchall()

# Extract token IDs and create a comma-separated list
token_names = ", ".join(str(token[0]) for token in token_result) if token_result else "N/A"

# Query the park_ticket table for token_id 1001
park_ticket_query = "SELECT * FROM park_ticket WHERE token_id = 1001"
my_cur2.execute(park_ticket_query)
park_ticket_result = my_cur2.fetchall()

# Extract park ticket information and create a comma-separated list
park_ticket_info = ", ".join(str(info) for info in park_ticket_result) if park_ticket_result else "N/A"

park_ticket_info = []

for info in park_ticket_result:
    ticket_info = (
        f"Location: {info[1]}, {info[2]}\n"
        f"Dates: {info[3].strftime('%m/%d/%y')} - {info[4].strftime('%m/%d/%y')}"
    )
    park_ticket_info.append(ticket_info)

# Join the formatted ticket information into a single string
formatted_park_ticket_info = "\n\n".join(park_ticket_info) if park_ticket_info else "N/A"

# Query the hotel_key table for token_id 1101
hotel_key_query = "SELECT * FROM hotel_key WHERE token_id = 1101"
my_cur2.execute(hotel_key_query)
hotel_key_result = my_cur2.fetchall()

# Extract hotel key information and create a comma-separated list
hotel_key_info = ", ".join(str(info) for info in hotel_key_result) if hotel_key_result else "N/A"

# Extract hotel key information and create a formatted list
hotel_key_info = []

for info in hotel_key_result:
    room_number = info[3]  # Assuming room number is in the 4th column
    checkout_date = info[5]  # Assuming checkout date is in the 6th column
    
    key_info = (
        f"Hotel Name: {info[1]}\n"
        f"Room Number: {room_number}\n"
        f"Checkout Date: {checkout_date}"
    )
    hotel_key_info.append(key_info)

# Join the formatted hotel key information into a single string
formatted_hotel_key_info = "\n\n".join(hotel_key_info) if hotel_key_info else "N/A"


#streamlit app
st.title("My Stuff")
st.text("User 1: Micah Uhrlass")

#css styling
css_code = """
    <style>
        .custom-container {
            border: 2px solid #DCDCDC;
            border-radius: 5px;
            padding:  0% 0% 0% 5%;
            text-align: center;
            margin-bottom: 10px;
            height: 400px;
        }

            .custom-box {
            border: 2px solid #DCDCDC;
            padding:  0% 0% 0% 5%;
            border-radius: 5px;
            text-align: center;
            margin-bottom: 10px;
            height: 330px;
        }

         .footer-container {
            border-radius: 5px;
            padding:  0% 0% 0% 5%;
            text-align: center;
            margin-bottom: 10px;
            height: 400px;
        }

          .custom-header {
            text-align: left;
            font-weight: bold;

        }

        .top-image {
            width: 100%;
            border-radius: 5px;
            height: 300px;
        }

        .smaller-image {
            width: 100%;
            border-radius: 5px;
            height: 50px;
        }

        .ticket-image {
            width: 80%;
            border-radius: 5px;
            height: 210px;
        }

         .key-image {
            width: 50%;
            border-radius: 5px;
            height: 23px;
        }

            .bottom-image {
            width: 100%;
            border-radius: 5px;
            height: 100px;
        }

    </style>  
"""

#html containers
# First row with one container spanning both columns
st.markdown(css_code, unsafe_allow_html=True)
html_code_row1 = """
    <div class="custom-container">
    <h3 class="custom-header">Redeemables</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/QR_Code.png?raw=true" class="top-image">
    </div>
"""
st.markdown(html_code_row1, unsafe_allow_html=True)

# Second row with two boxes/ columns, each taking up half the page
cols_row2 = st.columns(2)
html_code_row2_left = ("""
    <div class="custom-box">
    <h3 class="custom-header">Points</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(15).png?raw=true class="smaller-image">
""" 
    f"<p>{point_quantity_value}</p>"
    "</div>"
)

html_code_row2_right = ("""
    <div class="custom-box">
    <h3 class="custom-header">Badges</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/MicrosoftTeams-image%20(16).png?raw=true class="smaller-image">
"""
    f"<p>{token_names}</p>"
    "</div>"
)

cols_row2[0].markdown(html_code_row2_left, unsafe_allow_html=True)
cols_row2[1].markdown(html_code_row2_right, unsafe_allow_html=True)

# Third row with two boxes, each taking up half the page (2 columns)
cols_row3 = st.columns(2)
html_code_row3_left = ("""
    <div class="custom-box">
    <h3 class="custom-header">Park Tickets</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/ticket.png?raw=true" class="ticket-image">
"""
    f"<p>{formatted_park_ticket_info}</p>"
    "</div>"
)

html_code_row3_right = ("""
    <div class="custom-box">
    <h3 class="custom-header">Hotel Keys</h3>
    <img src= "https://github.com/mergray0521/poc/blob/main/images/key.png?raw=true" class="ticket-image">
"""
    f"<p>{formatted_hotel_key_info}</p>"
    "</div>"
)
cols_row3[0].markdown(html_code_row3_left, unsafe_allow_html=True)
cols_row3[1].markdown(html_code_row3_right, unsafe_allow_html=True)

# First row with one container spanning both columns
st.markdown(css_code, unsafe_allow_html=True)
html_code_row4 = """
    <div class="footer-container">
    <img src= "https://github.com/mergray0521/poc/blob/main/images/bottom.png?raw=true" class="bottom-image">
    </div>
"""
st.markdown(html_code_row4, unsafe_allow_html=True)
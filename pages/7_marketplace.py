import streamlit as st

# Apply the CSS file to Streamlit
st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)

st.header("Token Marketplace")

# Sample image URLs
token_1 = "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain"
token_2 = "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png"
token_3 = "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"
token_4 = "https://th.bing.com/th/id/OIP.OLAyoeOOoWuXs2aaZ9FL9QHaKl?rs=1&pid=ImgDetMain"
token_5 = "https://mickeystravel.com/site/universal/files/2016/06/Universal-Orlando-base-Ticket.png"
token_6 = "https://th.bing.com/th/id/OIP.2JqerB2uBGAwciMukwF5ygHaHJ?rs=1&pid=ImgDetMain"

# Create three columns
col1, col2, col3 = st.columns(3)

# Display images in containers within columns
with col1:
    st.markdown('<div class="my-container">', unsafe_allow_html=True)
    col1.image(token_1, caption="My Say Token", use_column_width=True, width=300)
    col1.text("1,000 points")
    col1.button("Purchase My Say", class="my-button")
    col1.image(token_4, caption="Minion Glasses", use_column_width=True, width=300)
    col1.text("2,000 points")
    col1.button("Purchase Glasses", class="my-button")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="my-container">', unsafe_allow_html=True)
    col2.image(token_2, caption="My Way Token", use_column_width=True, width=50)
    col2.text("2,000 points")
    col2.button("Purchase My Way", class="my-button")
    col2.image(token_5, caption="Park Pass", use_column_width=True, width=50)
    col2.text("4,000 points")
    col2.button("Purchase Pass", class="my-button")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="my-container">', unsafe_allow_html=True)
    col3.image(token_3, caption="My Day Token", use_column_width=True, width=50)
    col3.text("3,000 points")
    col3.button("Purchase My Day", class="my-button")
    col3.image(token_6, caption="Dragon", use_column_width=True, width=50)
    col3.text("3,000 points")
    col3.button("Purchase Dragon", class="my-button")
    st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

st.header("Token Marketplace")

# Sample image URLs
token_1 = "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain"
token_2 = "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png"
token_3 = "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"

# Create three columns
col1, col2, col3 = st.columns(3)

# Display images in columns
col1.image(token_1, caption="My Say Token", use_column_width=True, width=300)
col1.text("Cost: $10")
col1.button("Purchase")

col2.image(token_2, caption="My Way Token", use_column_width=True, width=50)
col2.text("Cost: $5")
col2.button("Purchase")

col3.image(token_3, caption="My Day Token", use_column_width=True, width=50)
col3.text("Cost: $8")
col3.button("Purchase")


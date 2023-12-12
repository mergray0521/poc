import streamlit as st
import snowflake.connector

st.title("Marketplace")

token_1 = "https://th.bing.com/th/id/OIP.Xk44653VMX5ZhgDi0h1oIQHaE8?rs=1&pid=ImgDetMain"
token_2 = "https://cdn4.iconfinder.com/data/icons/slot-machine-icons/200/casino_token-512.png"
token_3 = "https://th.bing.com/th/id/OIP.T2FQy8uhLgynn5M-UTI0ZAHaHa?rs=1&pid=ImgDetMain"

st.image(token_1, caption="Token: X", use_column_width=True, width=200)
st.image(token_2, caption="Token: X", use_column_width=True, width=200)
st.image(token_3, caption="Token: X", use_column_width=True, width=200)


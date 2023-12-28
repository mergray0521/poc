import streamlit as st

# Hardcoded credentials
admin_credentials = {"steve_albonico": "admin", "steve123": "adminpass"}
user_credentials = {"micah_uhrlass": "user", "micah456": "userpass"}

# Function to check credentials
def authenticate(username, password):
    if username == admin_credentials["admin_username"] and password == admin_credentials["admin_password"]:
        return "admin"
    elif username == user_credentials["user_username"] and password == user_credentials["user_password"]:
        return "user"
    else:
        return None

# Login page
def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = authenticate(username, password)

        if role:
            st.success(f"Login successful! Welcome, {role.capitalize()}!")
            return role
        else:
            st.error("Invalid username or password. Please try again.")

    return None

# Main function
def main():
    role = login_page()

    if role:
        # You can now use the 'role' variable to determine the user type and proceed accordingly.
        if role == "admin":
            st.write("You are an admin.")
            # Add admin-specific functionality here
        elif role == "user":
            st.write("You are a normal user.")
            # Add user-specific functionality here

if __name__ == "__main__":
    main()

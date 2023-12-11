import streamlit as st
import snowflake.connector
import pandas as pd

# Snowflake connection
my_cnx = snowflake.connector.connect(**st.secrets["INVENTORY_DB"])
my_cur = my_cnx.cursor()

# Load data from Snowflake
query = "SELECT * FROM avatar_wearables"
my_cur.execute(query)
columns = [col[0] for col in my_cur.description]
rows = my_cur.fetchall()
df = pd.DataFrame(rows, columns=columns)

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")
st.title("Snowflake Table Editor ❄️")
st.caption("This is a demo of the `st.data_editor`.")

with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited = st.data_editor(df, use_container_width=True, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        # Convert the edited format to the old format for compatibility
        edited_cells_old_format = {
            f"{row}:{col}": edited[row][col]
            for row in edited
            for col in edited[row]
        }

        # Write the edited cells back to Snowflake for the "avatar_wearables" table
        for key, value in edited_cells_old_format.items():
            row, col = map(int, key.split(":"))
            if columns[col] != 'row_id':  # Skip updating the 'row_id' column
                update_query = f"UPDATE avatar_wearables SET {columns[col]} = %s WHERE row_id = %s"
                my_cur.execute(update_query, (value, row))

        my_cnx.commit()
        st.success("Table updated")
    except Exception as e:
        st.error(f"Error updating table: {e}")
        st.stop()

    # Display success message and update the table to reflect what is in Snowflake
    st.success("Data saved in Snowflake!")
    st.rerun()


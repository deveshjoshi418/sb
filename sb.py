import streamlit as st
import sqlite3

# Function to establish a persistent SQLite connection
st.cache()
def get_db_connection():
    # Create a connection to SQLite database (it creates the file if it doesn't exist)
    conn = sqlite3.connect('data.db')
    return conn

# Get the persistent connection
conn = get_db_connection()
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS data_table (data TEXT)''')
conn.commit()

# Check if 'data' already exists in session state
if 'data' not in st.session_state:
    st.session_state.data = []  # Initialize the data if not already present

# Add data to the session state
new_data = st.text_input("Enter data:")
if st.button("Save Data"):
    if new_data:
        st.session_state.data.append(new_data)
        st.success("Data saved!")
    else:
        st.warning("Please enter some data to save.")

# Save data to the SQLite database only if data exists in the session
if st.button("Save to Database"):
    if st.session_state.data:
        for data in st.session_state.data:
            cursor.execute("INSERT INTO data_table (data) VALUES (?)", (data,))
        conn.commit()
        st.success("Data saved to database!")
    else:
        st.warning("No data to save to the database.")

# Display the saved data
st.write("Saved Data:", st.session_state.data)

# Note: You don't need to call conn.close() here unless you want to close the connection at the end.

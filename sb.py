import streamlit as st
import pandas as pd
import json

# Storing data in a JSON file
def save_to_json(data, filename="data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)
    return st.write(data)

# Example data
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

# Save data to JSON
if st.button('Save Data to JSON'):
    save_to_json(df.to_dict(), 'data.json')
    st.success("Data saved to JSON!")


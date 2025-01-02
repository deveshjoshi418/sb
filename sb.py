import streamlit as st
import pandas as pd
import json

# Storing data in a JSON file
def save_to_json(data, filename="data.json"):
    with open(filename, 'w') as f:
        json.dump(data, f)
    return st.write(data)

# Example data
if 'inventory' not in st.session_state:
    st.session_state.inventory = pd.DataFrame(columns=['Item', 'Quantity', 'Size (ft)', 'Original Quantity'])

if 'inventory_list' not in st.session_state:
    st.session_state.inventory_list = []

def add_item(item_name, quantity, size):
    # Add new item to the inventory
    new_item = pd.DataFrame([[item_name, quantity, size, quantity]], columns=['Item', 'Quantity', 'Size (ft)', 'Original Quantity'])
    st.session_state.inventory_list.append(item_name)
    st.session_state.inventory = pd.concat([st.session_state.inventory, new_item], ignore_index=True)

action_1 = st.sidebar.radio("Choose action", ["Add Item", "Add Item Picture", "Remove Item", "Display History"])

if action_1 == "Add Item":
    st.subheader("Add Item to Inventory")
    item_name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=1)
    size = st.number_input("Size (ft)", step=1)
    original_quantity = quantity

    if st.button("Add Item") and item_name not in st.session_state.inventory_list:
        add_item(item_name, quantity, size)
        st.success(f"Item '{item_name}' added to inventory.")

df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

# Save data to JSON
if st.button('Save Data to JSON'):
    save_to_json(st.session_state.inventory.to_dict(), 'data.json')
    st.success("Data saved to JSON!")




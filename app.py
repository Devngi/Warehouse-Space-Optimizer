import streamlit as st
import pandas as pd
import numpy as np
import time

# --- DAA CORE: 0/1 KNAPSACK ALGORITHM ---
def solve_knapsack(weights, values, capacity):
    n = len(values)
    # Create the DP table (rows: items, cols: capacity)
    # Using float to handle potential large values
    dp = np.zeros((n + 1, capacity + 1), dtype=int)

    # Building the table bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                # Max of (Value of current item + Value of remaining capacity) OR (Value without current item)
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Backtracking: Finding which items were actually picked
    selected_indices = []
    w_remaining = capacity
    for i in range(n, 0, -1):
        if dp[i][w_remaining] != dp[i-1][w_remaining]:
            selected_indices.append(i-1)
            w_remaining -= weights[i-1]
            
    return dp, selected_indices

# --- STREAMLIT UI ---
st.set_page_config(page_title="DAA Warehouse Optimizer", layout="centered")

# Hide Streamlit Default Menu, Footer and Element Toolbars
hide_st_style = """
            <style>
            /* Make app background white and hide default chrome */
            /* Core page elements */
            html, body, .stApp, .main, .block-container, [data-testid="stAppViewContainer"], [data-testid="stToolbar"], [data-testid="stSidebar"] {
                background-color: #ffffff !important;
                color: #000000 !important;
            }

            /* Sidebar specific */
            [data-testid="stSidebar"] > div, .stSidebar, .sidebar .sidebar-content {
                background-color: #ffffff !important;
                color: #000000 !important;
            }

            /* Dataframes / tables */
            table, .stDataFrame, .stTable, .dataframe, .stDataFrame td, .stDataFrame th, .st-table {
                background-color: #ffffff !important;
                color: #000000 !important;
            }

            /* Ensure nested blocks don't carry unexpected backgrounds */
            [data-testid="stVerticalBlock"] > div, .css-18e3th9, .css-1v3fvcr {
                background: transparent !important;
            }

            /* Fallback: force most common containers to white */
            main, section, header, footer, aside, div[class*="css-"] {
                background-color: #ffffff !important;
                color: #000000 !important;
            }

            /* Hide Streamlit auto-generated header anchor links */
            .stMarkdown a, h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
                display: none !important;
            }

            /* Hide Streamlit chrome */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stDeployButton {display:none;}
            [data-testid="stElementToolbar"] {display: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Warehouse Space Optimization (0/1 Knapsack)")

# 1. User Input Section
st.write("### Warehouse Capacity")
capacity = st.number_input("Max Volume Capacity:", min_value=1, value=100)

st.write("### Add your boxes")
num_boxes = st.number_input("How many boxes do you have?", min_value=1, value=1, step=1)

# Generate empty structure based on user input
input_data = pd.DataFrame({
    "Box Name": [f"Box {i+1}" for i in range(num_boxes)],
    "Length": [0] * num_boxes,
    "Width": [0] * num_boxes,
    "Height": [0] * num_boxes,
    "Price": [0] * num_boxes
})

st.write("Enter length, width and height (same units) and price for each box:")
inventory_df = st.data_editor(input_data, use_container_width=True, hide_index=True)
# Calculate volume for each box (Length * Width * Height)
inventory_df["Volume"] = (
    inventory_df["Length"].fillna(0).astype(float)
    * inventory_df["Width"].fillna(0).astype(float)
    * inventory_df["Height"].fillna(0).astype(float)
).astype(int)

# 2. Execution Section
if st.button("Calculate Optimal Boxes"):
    capacity = int(capacity)
    inventory_df["Status"] = ["Oversized " if vol > capacity else "Valid " for vol in inventory_df["Volume"]]
    
    # Highlight oversized items instantly
    oversized_count = (inventory_df["Volume"] > capacity).sum()
    if oversized_count > 0:
        st.warning(f"Warning: {oversized_count} box(es) exceed the maximum warehouse capacity and cannot possibly fit.", icon="⚠️")
        
    st.write("### Processed Inventory")
    st.dataframe(inventory_df, use_container_width=True, hide_index=True)

    weights = inventory_df["Volume"].astype(int).tolist()
    values = inventory_df["Price"].astype(int).tolist()
    names = inventory_df["Box Name"].astype(str).tolist()
    
    start_time = time.time()
    dp_table, selected_idx = solve_knapsack(weights, values, capacity)
    end_time = time.time()
    
    st.divider()
    
    # 3. Output Results
    st.success(f"Optimal Total Profit Found: **${dp_table[-1][-1]}**")
    
    st.write("### Selected Boxes for Storage:")
    final_items = inventory_df.iloc[selected_idx]
    st.table(final_items)
    
    # 4. The DP Table
    st.write("### DP Matrix (Advanced)")
    # Formatting the DP table for display
    dp_display = pd.DataFrame(
        dp_table, 
        columns=[f"Cap {i}" for i in range(capacity + 1)],
        index=["Base"] + names
    )
    
    # Provide a toggle to show the full DP Matrix
    with st.expander("Show the Full DP Computational Matrix"):
        st.info("Scroll horizontally to see all capacity increments.")
        st.dataframe(dp_display, use_container_width=True)

    # 5. Complexity
    st.write("### Analysis")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Time", "O(N * W)")
    with col2:
        st.metric("Space", "O(N * W)")
    with col3:
        execution_ms = (end_time - start_time) * 1000
        st.metric("Time taken", f"{execution_ms:.2f} ms")

else:
    st.info("Fill out the items above and hit Calculate.")

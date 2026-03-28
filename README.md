📦 Warehouse Space Optimizer

Solving the 0/1 Knapsack Problem with Dynamic Programming

This project is a visual demonstration of the 0/1 Knapsack Problem, a classic optimization challenge in computer science. It simulates a warehouse scenario where a manager must decide which boxes to store to maximize total value without exceeding the warehouse's volume capacity.

🧠 The Core Concept: What is 0/1 Knapsack?
The "0/1" indicates a binary choice: for every item, you must either take it (1) or leave it (0). You cannot take a fraction of an item (like half a box) or multiple copies of the same item.

The Challenge

Imagine you have a bag (or warehouse) with a limit of 10kg. You have:

Box A: 8kg, Value $60

Box B: 5kg, Value $40

Box C: 5kg, Value $40

If you are "greedy" and take the most valuable item first (Box A), you fill 8kg and can't fit anything else (Total: $60).
The Optimal Solution is to take Box B and Box C (Total: $80), even though they are individually worth less than Box A.

🛠️ How the Algorithm Works
This app uses Dynamic Programming (DP). Instead of calculating every possible combination (which would take 2 
n
  time), DP breaks the problem into smaller sub-problems and stores the results in a table.

1. The Decision Matrix

The algorithm builds a table where:

Rows represent the items available.

Columns represent increasing weight capacities (from 0 to Max).

2. The Logic

For every cell in the table, the algorithm asks:

"Is the value of adding this current item plus the remaining space better than the best value I found without this item?"

DP[i][w]=max(Value 
i
​	
 +DP[i−1][w−Weight 
i
​	
 ],DP[i−1][w])
🚀 Key Features
Interactive Data Entry: Input Box dimensions (L×W×H) and the app calculates volume automatically.

Backtracking Logic: The app doesn't just give a number; it traces back through the matrix to tell you exactly which boxes to pick.

Computational Transparency: An expandable "DP Matrix" view allows evaluators to see the math happening under the hood.

📊 Technical Analysis
Feature	Detail
Algorithm	Bottom-Up Dynamic Programming
Time Complexity	O(N×W) — Linear relative to capacity and items.
Space Complexity	O(N×W) — Required for the memoization table.
Frontend	Streamlit (Python-based Web Framework)
Data Handling	Pandas & NumPy
🚦 Getting Started
Install Requirements: pip install streamlit pandas numpy

Run the App: streamlit run app.py

Test Case: * Set Capacity to 10.

Add Box 1 (Vol: 6, Price: 10).

Add Box 2 (Vol: 5, Price: 7).

Add Box 3 (Vol: 5, Price: 7).

Result should select Box 2 and 3 for a total of 14.

🔮 Future Enhancements
3D Bin Packing: Adding logic to check if boxes physically fit (orientation), not just volume.

Fractional Knapsack: Implementing a Greedy approach for items that can be divided (like grains or liquids).

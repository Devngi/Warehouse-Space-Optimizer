# 📦 Warehouse Space Optimizer (0/1 Knapsack)

An interactive web application built with **Streamlit** that uses the **0/1 Knapsack Algorithm** to solve a real-world logistics challenge: maximizing profit within a limited storage volume.

---

## 🧠 The Concept: What is the 0/1 Knapsack Problem?

The **0/1 Knapsack Problem** is a classic optimization puzzle in computer science. 

### The Scenario
You have a warehouse with a fixed maximum **Capacity** (Volume) and a set of **Items** (Boxes). Each item has a:
1.  **Weight** (Calculated as $Length \times Width \times Height$)
2.  **Value** (Price)

### The Constraint ("0/1")
The "0/1" means you cannot take a fraction of an item. You either take the box (**1**) or leave it (**0**). You must decide which combination of boxes yields the highest total price without exceeding the warehouse volume.

---

## 🛠️ How It Works: Dynamic Programming (DP)

Instead of checking every possible combination (which is inefficient), this app uses **Bottom-Up Dynamic Programming**. 

### 1. The Recurrence Relation
The algorithm fills a 2D grid where each cell represents the maximum value attainable for a given capacity using a subset of items:

$$
DP[i][w] = 
\begin{cases} 
\max(v_i + DP[i-1][w-w_i], DP[i-1][w]) & \text{if } w_i \leq w \\
DP[i-1][w] & \text{otherwise}
\end{cases}
$$

### 2. Backtracking
Once the table is complete, the app "walks backward" from the final cell to identify exactly which boxes were selected to reach that optimal value.

---

## ✨ Features

* **Custom Inventory:** Add as many boxes as you need with specific dimensions.
* **Automatic Volume Calculation:** Converts $L \times W \times H$ into total volume instantly.
* **Visual DP Matrix:** An expandable section that shows the "brain" of the algorithm (the computational table).
* **Efficiency Metrics:** Real-time tracking of execution time and complexity analysis.

---

## 📊 Technical Analysis

| Metric | Complexity | Why? |
| :--- | :--- | :--- |
| **Time Complexity** | $O(N \cdot W)$ | We iterate through $N$ items for every unit of capacity $W$. |
| **Space Complexity** | $O(N \cdot W)$ | We store a 2D table to remember sub-problem solutions (Memoization). |

> **Note:** $N$ = Number of items, $W$ = Warehouse Capacity.

---

## 🚀 Installation & Usage

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/warehouse-optimizer.git](https://github.com/your-username/warehouse-optimizer.git)

2. **Install dependencies:**
   ```bash
   pip install streamlit pandas numpy

3. **Run the application:**
   ```bash
   streamlit run app.py

For better visualization - use it in Light mode

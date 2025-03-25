import numpy as np
import matplotlib.pyplot as plt


# Function to calculate NPV for a series of cash flows given discount rate r
def npv(cash_flows, r):
    return sum(cf / ((1 + r) ** t) for t, cf in enumerate(cash_flows))


# Define cash flows for two projects:
# Project A: smaller early inflows, larger later inflows
project_A = [-1000, 200, 700, 300]
# Project B: larger early inflows, smaller later inflows
project_B = [-1000, 500, 300, 300]

# Create a range of discount rates (e.g., 0% to 60%)
r_values = np.linspace(0, 0.6, 300)

# Compute NPVs for each project at each discount rate
npv_A = [npv(project_A, r) for r in r_values]
npv_B = [npv(project_B, r) for r in r_values]

# Determine the crossover rate (where NPVs are equal)
# Compute the difference between NPVs
diff = np.array(npv_A) - np.array(npv_B)
# Find index where the sign of the difference changes
crossover_indices = np.where(np.diff(np.sign(diff)))[0]
if len(crossover_indices) > 0:
    idx = crossover_indices[0]
    r_crossover = r_values[idx]
    NPV_crossover = npv_A[idx]
else:
    r_crossover = None

# Plot the NPV curves for both projects
plt.figure(figsize=(8, 6))
plt.plot(r_values, npv_A, label="Project A NPV")
plt.plot(r_values, npv_B, label="Project B NPV")


plt.xlabel("Discount Rate")
plt.ylabel("Net Present Value (NPV)")
plt.title("NPV vs Discount Rate (Crossover Analysis)")
plt.legend()
plt.grid(True)
plt.show()

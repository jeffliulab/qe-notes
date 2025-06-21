import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===========================
# Model parameters
# ===========================
initial_inflation = 3.2   # starting inflation rate (%)
natural_rate = 2.0        # neutral interest rate (%)
inflation_target = 2.0    # target inflation (%)
phi_pi = 1.5              # Fed reaction to inflation gap
rho_pi = 0.8              # inflation persistence
T = 8                     # number of quarters to simulate

# ===========================
# Simulate paths
# ===========================
inflation_path = [initial_inflation]
interest_path = []
np.random.seed(42)

for _ in range(T):
    shock = np.random.normal(0, 0.3)  # inflation shock
    next_inflation = rho_pi * inflation_path[-1] + shock
    policy_rate = natural_rate + phi_pi * (inflation_path[-1] - inflation_target)
    
    inflation_path.append(next_inflation)
    interest_path.append(policy_rate)

# ===========================
# Build time index
# ===========================
future_dates = pd.date_range(start=pd.Timestamp.today(), periods=T+1, freq='Q')

# ===========================
# Plot results
# ===========================
plt.figure(figsize=(10, 5))
plt.plot(future_dates[:-1], interest_path, label='Predicted Interest Rate (%)', linewidth=2)
plt.plot(future_dates, inflation_path, label='Predicted Inflation Rate (%)', linewidth=2)
plt.axhline(y=inflation_target, color='gray', linestyle='--', label='Inflation Target (%)')

plt.xlabel('Date')
plt.ylabel('Percent (%)')
plt.title('Projected U.S. Inflation and Interest Rate Over Next 8 Quarters')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

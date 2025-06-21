import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.ar_model import AutoReg
import pandas_datareader.data as web

# 1. Fetch annual Gini index (personal income)
start = datetime(2000, 1, 1)
end   = datetime.today()
gini = web.DataReader('CNP16OV', 'fred', start, end)  
# 'CNP16OV' is Census Gini for personal income

# Convert annual to quarterly by forward-filling
gini_q = gini.resample('Q').ffill()

# 2. Fit an AR(1) on the last N observations
series = gini_q['CNP16OV'].dropna()
model = AutoReg(series, lags=1, old_names=False).fit()
phi, intercept = model.params['CNP16OV.L1'], model.params['const']

# 3. Simulate next 8 quarters
T = 8
last = series.iloc[-1]
sim_vals = []
np.random.seed(0)
for _ in range(T):
    eps = np.random.normal(scale=model.resid.std())
    next_g = intercept + phi * last + eps
    sim_vals.append(next_g)
    last = next_g

# Build a date index for the forecast
future_q = pd.date_range(start=series.index[-1] + pd.offsets.QuarterEnd(), periods=T, freq='Q')
sim_series = pd.Series(sim_vals, index=future_q)

# 4. Plot history + forecast
plt.figure(figsize=(10, 5))
plt.plot(series.index, series.values, label='Historical Gini')
plt.plot(sim_series.index, sim_series.values, '--', label='Forecasted Gini')
plt.title('U.S. Gini Index: Historical + AR(1) Forecast')
plt.ylabel('Gini coefficient')
plt.xlabel('Date')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

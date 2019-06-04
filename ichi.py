# %%
import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import config
mpl.rcParams['figure.dpi'] = 300
plt.style.use('seaborn')

quandl.ApiConfig.api_key = config.api_key

btc = quandl.get('GDAX/BTC_USD', paginate=True)
df = pd.DataFrame(data=btc, columns=['Open', 'High', 'Low'])

# length of conversion line
CL_period = 20
# length of base line
BL_period = 60
# length of leading span
Lead_span = 120
# length of lagging span
Lag_span = 30

df['Conv_line'] = (df.High.shift(CL_period) + df.Low.shift(CL_period)) / 2
df['Base'] = (df.High.shift(BL_period) + df.Low.shift(BL_period)) / 2
df['Lead_span_A'] = (df['Conv_line'] + df['Base']) / 2
df['Lead_span_B'] = (df.High.shift(Lead_span) + df.Low.shift(Lead_span)) / 2
df['Lagging_span'] = df.Open.shift(Lag_span)
df.dropna(inplace=True)


fig, ax = plt.subplots(1, 1, sharex=True, figsize=(20, 9))

ax.plot(df.index, df.Open, linewidth=4)

ax.plot(df.index, df.Lead_span_A)

ax.plot(df.index, df.Lead_span_B)

ax.fill_between(df.index, df.Lead_span_A, df.Lead_span_B,
                where=df.Lead_span_A >= df.Lead_span_B, color='lightgreen')
ax.fill_between(df.index, df.Lead_span_A, df.Lead_span_B,
                where=df.Lead_span_A < df.Lead_span_B, color='lightcoral')
plt.legend(loc=0)

plt.grid()

plt.show()

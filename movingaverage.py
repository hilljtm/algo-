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

btc = pd.DataFrame(btc)
btc.info()

btc['High'].plot(grid=True)
plt.title('Bitcoin on GDAX')

short_window = 50
long_window = 100

signals = pd.DataFrame(index=btc.index)
signals['signal'] = 0.0

signals['short_mavg'] = btc['High'].rolling(
    window=short_window, min_periods=1, center=False).mean()

signals['long_mavg'] = btc['High'].rolling(
    window=long_window, min_periods=1, center=False).mean()

signals['signal'][short_window:] = np.where(
    signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

signals['positions'] = signals['signal'].diff()
print(signals)

fig = plt.figure(figsize=(20, 15))

ax1 = fig.add_subplot(111, ylabel='Price in $')

btc['High'].plot(ax=ax1, color='black', lw=2.)

signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)


ax1.plot(signals.loc[signals.positions == 1.0].index,
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=20, color='g')

ax1.plot(signals.loc[signals.positions == -1.0].index,
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=20, color='r')


plt.savefig('ma.png', facecolor='w', edgecolor='w')
plt.show()
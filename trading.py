#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns



#df.drop(['Symbol'])
#df.head()
df = pd.read_csv('mexhist.csv', names=['Time', 'Symbol'])
df.tail()

fig, ax = plt.figure()


plt.plot(df)
plt.show()


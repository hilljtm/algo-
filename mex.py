#%%
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set()
mpl.rcParams['figure.dpi'] = 300
plt.style.use('seaborn')

df = pd.read_csv('finexhourly.csv', parse_dates=True)

df.head()
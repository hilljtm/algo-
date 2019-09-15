#%%
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set(context='notebook', style='darkgrid', palette='deep',color_codes=True, rc=None)


df = pd.read_csv('finexhourly.csv')

sns.lineplot(df)

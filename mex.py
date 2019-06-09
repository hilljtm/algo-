#%%
import config 
import requests
import pandas as pd
import matplotlib.pyplot as plt


apiKey = "compare_key"

url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=USD&limit=24&aggregate=3&e=CCCAGG"

result = requests.get(url)
result.json()

#TODO create columns and plug result into DF
df = pd.DataFrame(result)
df.head()
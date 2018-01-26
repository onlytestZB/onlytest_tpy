import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
stock_day_change = np.load('./stock_day_change.npy')
print(stock_day_change.shape)
days = pd.date_range('2017-1-1',periods=stock_day_change.shape[1],freq='1d')
stock_symbols = ['股票 '+str(x) for x in
                 range(stock_day_change.shape[0])]
df = pd.DataFrame(stock_day_change,index=stock_symbols, columns=days)

df = df.T
#df_20 = df.resample('21D', how='mean')
#df_20 = df.resample('21D').mean()

df_stock0 = df['股票 0']
print(type(df_stock0))
print(df_stock0.head())
df_stock0.cumsum().plot()
plt.show()
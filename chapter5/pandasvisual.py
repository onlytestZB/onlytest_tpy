import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from abupy import ABuSymbolPd
import matplotlib.finance as mpf
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
'''
5.3.1
tsla_df_copy = tsla_df.copy()
tsla_df_copy['return'] = np.log(tsla_df['close']/tsla_df['close'].shift(1))
tsla_df_copy['mov_std'] = pd.rolling_std(tsla_df_copy['return'],
                                         window=20,
                                         center = False)*np.sqrt(20)
tsla_df_copy['std_ewm'] = pd.ewmstd(tsla_df_copy['return'],span=20,
                                    min_periods=20,
                                    adjust=True)*np.sqrt(20)
tsla_df_copy[['close','mov_std','std_ewm','return']].plot(
    subplots = True,grid = True)
plt.show()
5.3.2
tsla_df.close.plot()
pd.rolling_mean(tsla_df.close,window=30).plot()
pd.rolling_mean(tsla_df.close,window=60).plot()
pd.rolling_mean(tsla_df.close,window=90).plot()
plt.legend(['close','30 mv','60 mv','90 mv'],loc='best')
plt.show()
'''

low_to_high_df = tsla_df.iloc[tsla_df[
    (tsla_df.close>tsla_df.open)&(tsla_df.key!=(tsla_df.shape[0]-1))].key.values+1]
change_ceil_floor  = np.where(low_to_high_df['p_change']>0,
                              np.ceil(
                                  low_to_high_df['p_change']),
                              np.floor(
                                  low_to_high_df['p_change']))
change_ceil_floor = pd.Series(change_ceil_floor)
print('低开高收的下一个交易日所有下跌的跌幅取整和sum：'+str(
    change_ceil_floor[change_ceil_floor<0].sum()))
print('低开高收的下一个交易日所有上涨的跌幅取整和sum：'+str(
    change_ceil_floor[change_ceil_floor>0].sum()))

_,axs = plt.subplots(nrows=2,ncols=2,figsize=(12,10))
change_ceil_floor.value_counts().plot(kind='bar',ax=axs[0][0])
change_ceil_floor.value_counts().plot(kind='barh',ax=axs[0][1])
change_ceil_floor.value_counts().plot(kind='kde',ax=axs[1][0])
change_ceil_floor.value_counts().plot(kind='pie',ax=axs[1][1])
plt.show()


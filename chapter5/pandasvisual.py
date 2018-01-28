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

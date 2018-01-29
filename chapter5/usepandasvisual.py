import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abupy import ABuSymbolPd
import matplotlib.finance as mpf
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
demo_list = np.array([2,4,16,20])
demo_window = 3
print(pd.rolling_std(demo_list,window=demo_window,
                     center=False)*np.sqrt(demo_window))
tsla_df_copy = tsla_df.copy()
tsla_df_copy['return'] = np.log(tsla_df['close'/tsla_df['close'].shift(1))
tsla_df_copy['mov_std'] = pd.rolling_std(tsla_df_copy['return'])
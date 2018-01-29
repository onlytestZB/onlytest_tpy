import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from abupy import ABuSymbolPd
import matplotlib.finance as mpf
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
def plot_demo(axs = None,just_series = False):
    drawer = plt if axs is None else axs
    drawer.plot(tsla_df.close,c='r')
    if not just_series:
        drawer.plot(tsla_df.close.index,tsla_df.close.values+10,c='g')
        drawer.plot(tsla_df.close.index.tolist(),
                    (tsla_df.close.values+20).tolist(),c='b')
    plt.xlabel('time')
    plt.ylabel('close')
    plt.title('TSLA CLOSE')
    plt.grid(True)
def plot_trade(buy_date,sell_date):
    start = tsla_df[tsla_df.index==buy_date].key.values[0]
    end = tsla_df[tsla_df.index == sell_date].key.values[0]
    plot_demo(just_series=True)
    plt.fill_between(tsla_df.index,0,tsla_df['close'],color='blue',alpha=0.38)
    plt.ylim(np.min(tsla_df['close'])-5,
             np.max(tsla_df['close'])+5)
    plt.legend(['close'],loc='best')
plot_trade('2016-02-01','2016-05-01')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import abupy
from abupy import ABuSymbolPd
import matplotlib.finance as mpf
tsla_df = ABuSymbolPd.make_kl_df('usTSLA', n_folds=2)
print(tsla_df)
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
    '''
    老版本
def plot_trade(buy_date,sell_date):
    start = tsla_df[tsla_df.index == buy_date].key.values[0]
    end = tsla_df[tsla_df.index == sell_date].key.values[0]
    plot_demo(just_series=True)
    plt.fill_between(tsla_df.index[start:end],0,tsla_df['close'][start:end],color='green',alpha=0.38)
    plt.ylim(np.min(tsla_df['close'])-5,
             np.max(tsla_df['close'])+5)
    plt.legend(['close'],loc='best')
    '''
def plot_trade(buy_date,sell_date):
    start = tsla_df[tsla_df.index == buy_date].key.values[0]
    end = tsla_df[tsla_df.index == sell_date].key.values[0]
    plot_demo(just_series=True)
    #底色蓝色
    plt.fill_between(tsla_df.index,0,tsla_df['close'],color='blue',alpha=0.08)
    #如果赚钱是红色，亏钱就是绿色
    if tsla_df['close'][end]<tsla_df['close'][start]:
        plt.fill_between(tsla_df.index[start:end],0,tsla_df['close'][start:end],color='green',alpha=0.38)
        is_win=False
    else:
        plt.fill_between(tsla_df.index[start:end], 0, tsla_df['close'][start:end], color='red', alpha=0.38)
        is_win = True

    plt.ylim(np.min(tsla_df['close'])-5,
             np.max(tsla_df['close'])+5)
    plt.legend(['close'],loc='best')
    return is_win
def plot_trade_with_annotate(buy_date,sell_date):
    '''
        :param buy_date: 交易买入日期
        :param sell_date: 交易卖出日期
        :param annotate: 卖出原因
        :return:
    '''
    is_win=plot_trade(buy_date,sell_date)
    plt.annotate('sell for stop win'if is_win else 'sell for stop loss',xy=(sell_date,tsla_df['close'].asof(sell_date)),arrowprops=dict(facecolor='yellow'),
                 horizontalalignment='left',verticalalignment='top')
plot_trade_with_annotate('2017-02-1','2017-03-15')

plt.show()
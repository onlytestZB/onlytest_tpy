import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import abupy
from abupy import ABuSymbolPd
import matplotlib.finance as mpf
tsla_df = ABuSymbolPd.make_kl_df('usTSLA', n_folds=2)
goog_df = ABuSymbolPd.make_kl_df('usGOOG',n_folds=2)
print(round(goog_df.close.mean(),2),round(goog_df.close.median(),2))
print(goog_df.tail())

def plot_two_stock(tsla,good,axs=None):
    drawer = plt if axs is None else axs
    drawer.plot(tsla,c='r')
    drawer.plot(good,c='g')
    drawer.grid(True)
    drawer.legend(['tsla','google'],loc='best')
plot_two_stock(tsla_df.close,goog_df.close)
plt.title('TSLA and Google CLOSE')
plt.xlabel('time')
plt.ylabel('close')
plt.show()

def two_mean_list(one, two, type_look='look_max'):
    """
    只针对俩个输入的均值归一化
    :param one:
    :param two:
    :param type_look:
    :return:
    """
    one_mean = one.mean()
    two_mean = two.mean()
    if type_look == 'look_max':
        """
            向较大的均值序列看齐
        """
        one, two = (one, one_mean / two_mean * two) \
            if one_mean > two_mean else (
            one * two_mean / one_mean, two)
    elif type_look == 'look_min':
        """
            向较小的均值序列看齐
        """
        one, two = (one * two_mean / one_mean, two) \
            if one_mean > two_mean else (
            one, two * one_mean / two_mean)
    return one, two

def regular_std(group):
    # z-score规范化也称零-均值规范化
    return (group - group.mean()) / group.std()

def regular_mm(group):
    # 最小-最大规范化
    return (group - group.min()) / (group.max() - group.min())

# 2行2列，4个画布
_, axs = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))

# 第一个regular_std, 如图5-16左上所示
drawer = axs[0][0]
plot_two_stock(regular_std(tsla_df.close), regular_std(goog_df.close),
               drawer)
drawer.set_title('(group - group.mean()) / group.std()')

# 第二个regular_mm，如图5-16右上所示
drawer = axs[0][1]
plot_two_stock(regular_mm(tsla_df.close), regular_mm(goog_df.close),
               drawer)
drawer.set_title(
    '(group - group.min()) / (group.max() - group.min())')

# 第三个向较大的序列看齐，如图5-16左上所示
drawer = axs[1][0]
one, two = two_mean_list(tsla_df.close, goog_df.close,
                         type_look='look_max')
plot_two_stock(one, two, drawer)
drawer.set_title('two_mean_list type_look=look_max')

# 第四个向较小的序列看齐，如图5-16右下所示
drawer = axs[1][1]
one, two = two_mean_list(tsla_df.close, goog_df.close,
                         type_look='look_min')
plot_two_stock(one, two, drawer)
drawer.set_title('two_mean_list type_look=look_min')
plt.show()

_, ax1 = plt.subplots()
ax1.plot(tsla_df.close, c='r', label='tsla')
# 第一个ax的标注
ax1.legend(loc=2)
ax1.grid(False)
# 反向y轴 twinx
ax2 = ax1.twinx()
ax2.plot(goog_df.close, c='g', label='google')
# 第二个ax的标志
ax2.legend(loc=1)
plt.show()

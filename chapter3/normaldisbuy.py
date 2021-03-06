import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs
stock_day_change = np.load('./stock_day_change.npy')

keep_days = 50
stock_cnt=200
view_days=504
stock_day_change_test = stock_day_change[:stock_cnt,
                        0:view_days-keep_days]
print(np.sort(np.sum(stock_day_change_test,axis=1))[:3])
stock_lower_array = np.argsort(np.sum(stock_day_change_test,axis=1))[0:3]
print(stock_lower_array)

def show_buy_lower(stock_ind):
    _,axs = plt.subplots(nrows=1, ncols=2, figsize=(16, 5))
    axs[0].plot(np.arange(0, view_days-keep_days),
                stock_day_change_test[stock_ind].cumsum())
    cs_buy = stock_day_change[stock_ind][
        view_days-keep_days:view_days].cumsum()
    axs[1].plot(np.arange(view_days-keep_days, view_days), cs_buy)
    plt.show()
    return cs_buy[-1]

profit = 0
for stock_ind in stock_lower_array:
    tmp_profit = show_buy_lower(stock_ind)
    print('买入第{}只股票，从454个交易日开始持有盈亏:{:.2f}%'.format(stock_ind, tmp_profit))
    profit += tmp_profit
print('买入第{}只股票，从454个交易日开始持有盈亏:{:.2f}%'.format(stock_lower_array,profit))

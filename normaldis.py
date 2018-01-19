import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs
stock_day_change = np.load('./stock_day_change.npy')

stock_mean = stock_day_change[0].mean()
stock_std = stock_day_change[0].std()
print('股票0 mean均值期望:{:.3f}'.format(stock_mean))
print('股票0 std振幅标准差:{:.3f}'.format(stock_std))
plt.hist(stock_day_change[0],bins=50,normed=True)
fit_linspace = np.linspace(stock_day_change[0].min(),
                           stock_day_change[0].max())
pdf = scs.norm(stock_mean,stock_std).pdf(fit_linspace)
plt.plot(fit_linspace,pdf,lw=2,c='r')
plt.show()
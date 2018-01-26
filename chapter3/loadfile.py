import numpy as np
import matplotlib.pyplot as plt
stock_day_change = np.load('./stock_day_change.npy')
print(stock_day_change.shape)

stock_day_change_four = stock_day_change[:4,:4]
print(stock_day_change_four)
print('最大涨幅{}'.format(np.max(stock_day_change_four,axis=1)))
print('最大跌幅{}'.format(np.min(stock_day_change_four,axis=1)))
print('振幅幅度{}'.format(np.std(stock_day_change_four,axis=1)))
print('平均涨跌{}'.format(np.mean(stock_day_change_four,axis=1)))

a = np.random.normal(loc=100,scale = 50,size=(1000,1))

b = np.random.normal(loc=100,scale = 20,size=(1000,1))

print('a交易期望{0:.2f}元,标准差{1:.2f},方差{2:.2f}'.format(a.mean(),a.std(),a.var()))
print('b交易期望{0:.2f}元,标准差{1:.2f},方差{2:.2f}'.format(b.mean(),b.std(),b.var()))
a_mean = a.mean()
a_std = a.std()
plt.plot(a)
plt.axhline(a_mean+a_std,color='r')
plt.axhline(a_mean,color = 'y')
plt.axhline(a_mean-a_std,color ='g')

b_mean = b.mean()
b_std = b.std()
plt.plot(b)
plt.axhline(b_mean+b_std,color='r')
plt.axhline(b_mean,color = 'y')
plt.axhline(b_mean-b_std,color ='g')
plt.show()
import numpy as np

stock_cnt = 200
view_days = 504
stock_day_change = np.random.standard_normal((stock_cnt,view_days))
print(stock_day_change.shape)
print(stock_day_change[0:2,:5])
print(stock_day_change[-2:,-5:])
print(np.any( stock_day_change[0:2,0:5] >0.5))
print(np.maximum(stock_day_change[0:2,0:5],stock_day_change[-2:,-5:]))
print( np.where(np.logical_and(stock_day_change[0:2,0:5]>0.5,stock_day_change[0:2,0:5]<1),1,0))

np.save('./stock_day_change',stock_day_change)
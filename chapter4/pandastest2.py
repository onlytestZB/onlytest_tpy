from abupy import ABuSymbolPd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
'''
tsla_df.tail()

tsla_df[['close','volume']].plot(subplots=True, style=['r','g'],
                                 grid=True)
tsla_df.info()
tsla_df.describe()
tsla_df.loc['2017-07-23':'2017-07-31','open']
'''

#tsla_df.p_change.hist(bins=80)
plt.hist(tsla_df.p_change,bins=80)
plt.show()

bins = [-np.inf,-7.0,-5,-3,0,3,5,7,np.inf]
cats = pd.cut(tsla_df.p_change,bins)
change_ration_dummies = pd.get_dummies(cats,prefix='cr_dummies')
print(change_ration_dummies.tail())
print(pd.concat([tsla_df,change_ration_dummies], axis=1).tail())
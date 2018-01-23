from abupy import ABuSymbolPd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
tsla_df['positive'] = np.where(tsla_df.p_change>0,1,0)
print(tsla_df)
xt = pd.crosstab(tsla_df.date_week, tsla_df.positive)
print(xt)
xt_pct = xt.div(xt.sum(1).astype(float),axis=0)
print(xt_pct)
xt_pct.plot(
    figsize =(8,5),
    kind = 'bar',
    stacked=True,
    title='date_week->positive')
plt.xlabel('date_week')
plt.ylabel('positive')
plt.show()

print(tsla_df.pivot_table(['positive'],index=['date_week']))

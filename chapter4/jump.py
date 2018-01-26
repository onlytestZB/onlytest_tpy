from abupy import ABuSymbolPd
from abupy import ABuMarketDrawing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
jump_threshold = tsla_df.close.median()*0.03
print(jump_threshold)
#print(tsla_df)
jump_pd = pd.DataFrame()
def judge_jump(today):
    global jump_pd
    if today.p_change>0 and (today.low-today.pre_close)>jump_threshold:
        """
        符合向上跳空
        """
        today['jump']=1
        today['jump_power'] =(today.low-today.pre_close)/ jump_threshold
        jump_pd = jump_pd.append(today)
    elif today.p_change<0 and (today.pre_close-today.high)>jump_threshold:
        """
              符合向下跳空
              """
        today['jump'] = -1
        today['jump_power'] = (today.pre_close - today.high) / jump_threshold
        jump_pd = jump_pd.append(today)
for kl_index in np.arange(0,tsla_df.shape[0]):
    today = tsla_df.ix[kl_index]
    judge_jump(today)
print(jump_pd.filter(['jump','jump_power','close','date',
                      'p_change','pre_close']))
ABuMarketDrawing.plot_candle_form_klpd(tsla_df,view_indexs=jump_pd.index)

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
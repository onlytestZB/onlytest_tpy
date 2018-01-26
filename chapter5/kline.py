import matplotlib.pyplot as plt
from abupy import ABuSymbolPd
import matplotlib.finance as mpf
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
print(tsla_df)
__colorup__= "red"
__colordown__ = "green"
tsla_part_df = tsla_df[:30]
fig,ax = plt.subplots(figsize=(14,7))
qutotes=[]
for index,(d,o,c,h,l) in enumerate(
    zip(tsla_part_df.index,tsla_part_df.open,tsla_part_df.close,
        tsla_part_df.high,tsla_part_df.low)):
    d=mpf.date2num(d)
    val = (d,o,c,h,l)
    qutotes.append(val)
mpf.candlestick_ochl(ax,qutotes,width=0.6,colorup=__colorup__,
                     colordown=__colordown__)
ax.autoscale_view()
ax.xaxis_date()
plt.show()
from abupy import ABuMarketDrawing
ABuMarketDrawing.plot_candle_form_klpd(tsla_df,html_bk=True)
from abupy import ABuIndustries,ABuScalerUtil
import matplotlib.pyplot as plt
r_symbol = 'usTSLA'
p_date,_= ABuIndustries.get_industries_panel_from_target(r_symbol,show = False)
print(p_date)
print(p_date['usTTM'].head())
p_date_it = p_date.swapaxes('items','minor')
print(p_date_it)
p_date_it_cose = p_date_it['close'].dropna(axis=0)
print(p_date_it_cose.tail())

p_date_it_cose = ABuScalerUtil.scaler_std(p_date_it_cose)
p_date_it_cose.plot()
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
plt.ylabel('Price')
plt.xlabel('Time')
plt.show()
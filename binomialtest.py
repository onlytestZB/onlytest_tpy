import numpy as np
import matplotlib.pyplot as plt
gamblers =100
def casino(win_rate,win_once=1,loss_once=1,commission=0.01):
    my_money=10000
    play_cnt = 10000
    commission = commission
    for _ in np.arange(0, play_cnt):
        w = np.random.binomial(1, win_rate)
        if w:
            my_money += win_once
        else:
            my_money-= loss_once
        my_money -= commission
        if my_money <=0:
            break
    return my_money
heaven_moneys = [casino(0.5,commission=0) for _ in np.arange(0, gamblers)]
_ =plt.hist(heaven_moneys,bins=30)
plt.show()
cheat_moneys = [casino(0.4,commission=0) for _ in np.arange(0, gamblers)]
_ =plt.hist(cheat_moneys,bins=30)
plt.show()
commission_moneys= [casino(0.5,commission=0.01) for _ in np.arange(0, gamblers)]
_ =plt.hist(commission_moneys,bins=30)
plt.show()
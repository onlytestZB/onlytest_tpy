import matplotlib.pyplot as plt
from abupy import ABuSymbolPd
tsla_df = ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
print(tsla_df)

def plot_demo(axs = None,just_series = False):
    drawer = plt if axs is None else axs
    drawer.plot(tsla_df.close,c='r')
    if not just_series:
        drawer.plot(tsla_df.close.index,tsla_df.close.values+10,c='g')
        drawer.plot(tsla_df.close.index.tolist(),
                    (tsla_df.close.values+20).tolist(),c='b')
    plt.xlabel('time')
    plt.ylabel('close')
    plt.title('TSLA CLOSE')
    plt.grid(True)
    plt.show()

plot_demo()
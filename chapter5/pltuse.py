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


_,axs = plt.subplots(nrows=2,ncols=2,figsize=(14,10))
drawer = axs[0][0]
plot_demo(drawer)
drawer.legend(['Series','Numpy','List'],loc=0)
drawer = axs[0][1]
plot_demo(drawer)
drawer.legend(['Series','Numpy','List'],loc=1)
drawer= axs[1][0]
plot_demo(axs[1][0])
plot_demo(drawer)
drawer.legend(['Series','Numpy','List'],loc=2)
drawer=axs[1][1]
plot_demo(drawer)
drawer.legend(['Series','Numpy','List'],bbox_to_anchor=(1.05,1),loc=2,
              borderaxespad=0.)
plt.show()
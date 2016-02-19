import matplotlib.pyplot as plt
import numpy as np

#data
np.random.seed(42)
data = np.random.rand(5)
names = ['A:GBC_1233','C:WERT_423','A:LYD_342','B:SFS_23','D:KDE_2342']

ax = plt.subplot(111)
width=0.3
bins = map(lambda x: x-width/2,range(1,len(data)+1))
ax.bar(bins,data,width=width)
ax.set_xticks(map(lambda x: x, range(1,len(data)+1)))
ax.set_xticklabels(names,rotation=45)

plt.show()
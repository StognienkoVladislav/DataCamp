import matplotlib.pyplot as plt
import numpy as np
df_swing = []   #some Data

x = np.sort(df_swing['dem_share'])
y = np.arange(1, len(x) + 1/ len(x))

_ = plt.plot(x, y, marker = '.', linestyle = 'none')
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('ECDF')
plt.margins(0.02)           #Keeps data off plot edges
plt.show()


_ = sns.swarmplot(x = 'state', y = 'dem_share', data = df_swing)    #more detail then histogram
_ = plt.xlabel('state')
_ = plt.ylabel('percent of vote for Obama')
plt.show()
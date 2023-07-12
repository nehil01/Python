# TO CREATE A SIMPLE BAR-GRAPH USING TWO ARRAYS X AND Y

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)
y = np.random.uniform(1, 10, 10)
fig, ax = plt.subplots()
ax.bar(x, y)
fig.show()

# TO CREATE A SIMPLE SCATTER-PLOT USING TWO ARRAYS X AND Y

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[3,5,7,9,11,13]
plt.scatter(x, y)
plt.show()


# TO CREATE LINEAR GRAPH USING FUNCTIONS


import matplotlib.pyplot  as plt
fig,axes= plt.subplots(2,3)

import numpy as np

x=np.arange(1,5,0.2)
axes[0][0].plot(x,x*x)#plot at (0,0)
axes[0][0].set_title('square') 

axes[0][1].plot(x,np.sqrt(x))#plot at (0,1)
axes[0][1].set_title('square root')

axes[0][2].plot(x,np.exp(x))#plot at (0,2)
axes[0][2].set_title('exp')

axes[1][0].plot(x,np.log10(x))#plot at (1,0)
axes[1][0].set_title('log')

axes[1][1].plot(x,2*x+5)#plot at (1,1)
axes[1][1].set_title('linear')

axes[1][2].plot(x,2*x**2 -11*x +10)#plot at (1,2)
axes[1][2].set_title('polynomial')

plt.tight_layout() # spaces out the plots
plt.show()

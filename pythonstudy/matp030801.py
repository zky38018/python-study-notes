import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-np.pi,np.pi,500,endpoint=True)
y=np.sin(x)

plt.plot(x,y)

ax=plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()

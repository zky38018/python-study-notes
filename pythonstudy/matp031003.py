import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,10,1)
#y=np.log(x)
y=np.log(x)

xe=0.1* np.abs(np.random.randn(len(y)))

plt.bar(x,y,yerr=xe,width=0.4,align='center',ecolor='r',
        color='cyan',label='experiment #1')

plt.xlabel('# measurement')
plt.ylabel('Measured values')
plt.title('Measurements')
plt.legend(loc='upper left')

plt.show()

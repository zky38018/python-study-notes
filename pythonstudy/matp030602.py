from pylab import *
ax=gca()
ax.locator_params(tight=True,nbins=10)
ax.plot(np.random.normal(10,0.1,100))
show()

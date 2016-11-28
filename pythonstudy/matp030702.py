from matplotlib.pyplot import *

x1=np.random.normal(30,3,100)
x2=np.random.normal(20,2,100)
x3=np.random.normal(10,3,100)

plot(x1,label='plot')
plot(x2,label='2nd plot')
plot(x3,label='last plot')

legend(bbox_to_anchor=(0.,1.02,1.0,.102),loc=3,
       ncol=3,mode="expand",borderaxespad=0.0)
annotate("Important value",(55,20),xycoords='data',xytext=(5,38),
         arrowprops=dict(arrowstyle='->'))
show()

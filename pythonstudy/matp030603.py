from pylab import *
import matplotlib as mpl
import datetime

fig=figure()
ax=gca()

start=datetime.datetime(2013, 1, 1)
stop=datetime.datetime(2013, 12, 31)
delta=datetime.timedelta(days=1)

dates=mpl.dates.drange(start,stop,delta)

values=np.random.rand(len(dates))

ax=gca()

ax.plot_date(dates,values,linestyle='-',marker=' ')

date_format=mpl.dates.DateFormatter('%Y-%m-%d')

ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()

show()

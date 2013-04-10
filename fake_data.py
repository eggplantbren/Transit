from pylab import *

def transit_shape(t, width=1., smooth=0.05, amplitude=1.):
	y = amplitude*(1./(1. + exp(-(abs(t) - 0.5*width)/smooth)) - 1.)
	return y

# Data timestamps
t = linspace(-10., 10., 10001)

plot(t, transit_shape(t, amplitude=3.))
show()



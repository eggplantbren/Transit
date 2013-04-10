from pylab import *

def logistic(x, scale=1.):
	return 1./(1. + exp(-x/scale))

def transit_shape(tt, smooth=0.02):
	"""
	A single transit of unit width and depth, centered at zero
	"""
	return logistic(abs(tt) - 0.5, smooth) - 1.

def transit(t, amplitude=1., period=1., width=0.1, offset=0., smooth=0.02):
	"""
	An actual transit, periodic and all that.
	Width is in units of the period
	"""
	phase = mod(t/period - offset - 0.5, 1.) - 0.5
	return amplitude*transit_shape(phase/width, smooth)

# Data timestamps
t = linspace(-10., 10., 10001)

subplot(2,1,1)
plot(t, transit_shape(t, smooth=0.02))
ylim([-1.1, 0.1])
subplot(2,1,2)
plot(t, transit(t, period=1.7, width=0.1, offset=0.15, smooth=0.02))
ylim([-1.1, 0.1])
show()


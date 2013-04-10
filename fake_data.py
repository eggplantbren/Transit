from pylab import *

def logistic(x, scale=1.):
	"""
	Made-up functional form for ingress shape
	"""
	return 1./(1. + exp(-x/scale))

def transit_shape(tt, smooth=0.02):
	"""
	A single transit of unit width and depth, centered at zero
	"""
	return logistic(abs(tt) - 0.5, smooth) - 1.

def transit(t, amplitude=1., period=1., width=0.1, offset=0., smooth=0.02):
	"""
	An actual transit, periodic and all that.
	Width is in units of the period, smooth is in units of the width
	"""
	phase = mod(t/period - offset - 0.5, 1.) - 0.5
	return amplitude*transit_shape(phase/width, smooth)

# Reproducibility
seed(123)

# Data timestamps
t = linspace(0., 3., 100001)

# Parameter values
amplitude = 1.
period = 1.
width = 0.1
offset = 0.15
smooth = 0.02

# Noise variance
sigma = 1.

# Noise-free transit signal
y = transit(t, amplitude=amplitude, period=period, width=width, offset=offset,
		smooth=smooth)

# Make noisy data
data = empty((t.size, 3))
data[:,0] = t
data[:,1] = y + sigma*randn(y.size)
data[:,2] = sigma

# Save it
savetxt('fake_data.txt', data)

# Plot the signal and the data
subplot(2,1,1)
plot(t, y)
yRange = y.max() - y.min()
ylim([y.min() - 0.1*yRange, y.max() + 0.1*yRange])
ylabel('Flux (DC=0)')
title('Noise-Free Signal')

subplot(2,1,2)
plot(t, data[:,1], 'b.', markersize=1)
xlabel('$t$ (years)')
ylabel('Flux (DC=0)')
title('Noisy Data')
show()


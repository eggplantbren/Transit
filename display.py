from pylab import *
from fake_data import *

data = loadtxt('fake_data.txt')
posterior_sample = atleast_2d(loadtxt('posterior_sample.txt'))

ion()
for i in xrange(0, posterior_sample.shape[0]):
	# Noise-free transit signal
	y = transit(data[:,0],
			amplitude=posterior_sample[i, 0],
			period=posterior_sample[i, 1],
			width=posterior_sample[i, 2],
			offset=posterior_sample[i, 3],
			smooth=posterior_sample[i, 4])

	# Plot the data and the model
	hold(False)
	plot(data[:,0], data[:,1], 'b.', markersize=1)
	hold(True)
	plot(data[:,0], y, 'r')

	diff = data[:,1].max() - data[:,1].min()
	ylim([data[:,1].min() - 0.1*diff, data[:,1].max() + 0.1*diff])
	xlabel('Time')
	ylabel('Flux')
	title((i+1))
	draw()

ioff()
show()


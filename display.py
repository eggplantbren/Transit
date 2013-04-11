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


which = posterior_sample[:,0] > 0.
print('Prob(Exists | Data) = ' + str(which.mean()))

figure(1)
subplot(2,1,1)
hist(log10(posterior_sample[which,0]), 100, alpha=0.5)
axvline(log10(0.2), linewidth=3, color='r')
xlabel('$\\log_{10}$(Amplitude)')
xlim([-3, 3])

subplot(2,1,2)
hist(log10(posterior_sample[which,1]), 100, alpha=0.5)
axvline(log10(1.), linewidth=3, color='r')
xlabel('$\\log_{10}$(Period)')

figure(2)
plot(log10(posterior_sample[which, 0]), log10(posterior_sample[which, 1]), 'b.')
plot(log10(0.2), log10(1.), 'r*', markersize=10)
xlabel('$\\log_{10}$(Amplitude)')
ylabel('$\\log_{10}$(Period)')
xlim([-3, 3])

show()


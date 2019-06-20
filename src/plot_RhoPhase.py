import matplotlib.pylab as plt


def plot_RhoPhase(freq, rho_xy, phase_xy,  rho_yx, phase_yx, siteName, rmin = 1, rmax = 1000, pmin = 0, pmax = 90):

	plt.figure(1)
	plt.subplot(211)
	plt.loglog(freq, rho_xy, 'r')
	plt.loglog(freq, rho_xy, 'ro')
	plt.loglog(freq, rho_yx, 'b')
	plt.loglog(freq, rho_yx, 'bo')
	plt.title(siteName)
	plt.ylim(rmin, rmax)
	plt.xlim(min(freq), max(freq))
	plt.ylabel('App. Resistivity')
	plt.grid(True, which='both')

	plt.subplot(212)
	plt.semilogx(freq, phase_xy, 'r')
	plt.semilogx(freq, phase_xy, 'ro')
	plt.semilogx(freq, phase_yx, 'b')
	plt.semilogx(freq, phase_yx, 'bo')
	plt.ylim(pmin, pmax)
	plt.xlim(min(freq), max(freq))
	plt.xlabel('Periode')
	plt.ylabel('Phase')
	plt.grid(True, which='both')

	plt.show()
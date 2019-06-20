from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1,2,3,4]
y = [0,0,0,0]
X, Y = np.meshgrid(x, y)

Z = [[1, 1, 1, 1], [1.5, 1.5, 1.5, 1.5], [3, 3, 3, 3], [8, 8, 8, 8]]
Z = np.asarray(Z)

colors = [[1, 10, 100], [40, 50, 60], [70, 80, 1000]]

resMin = 1
resMax = 1000

m = cm.ScalarMappable(cmap=cm.jet_r, norm=LogNorm())
m.set_array([resMin, resMax])

cbar = plt.colorbar(m)
cbar.set_label('Resistivity', rotation=270)

colVal = plt.get_cmap('jet_r')
logRes = np.log10(colors)/(np.log10(resMax))

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=1, antialiased=False, shade=False, norm=cbar, facecolors=colVal(logRes))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()


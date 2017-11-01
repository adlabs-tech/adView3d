import numpy as np
from matplotlib.colors import LogNorm
from mpl_toolkits.mplot3d import Axes3D, axes3d
from matplotlib import cm
import matplotlib.pyplot as plt


def surface(x1, x2, y1, y2, z1, z2, xSum, ySum, zSum, res):
    
    logRes = np.log10(res) / 3
    colVal = plt.get_cmap('jet_r')

    if x1 == min(xSum):
        ax.plot_surface(([x1, x1]), ([y1, y2], [y1, y2]), ([z1, z1], [z2, z2]), linewidth=1,
                        color=colVal(logRes),
                        rstride=1, cstride=1, antialiased=False, shade=False)
    if x2 == max(xSum):
        ax.plot_surface(([x2, x2]), ([y1, y2], [y1, y2]), ([z1, z1], [z2, z2]), linewidth=1,
                        color=colVal(logRes),
                        rstride=1, cstride=1, antialiased=False, shade=False)
    if y1 == min(ySum):
        ax.plot_surface(([x1, x2], [x1, x2]), ([y1, y1]), ([z1, z1], [z2, z2]), linewidth=1,
                        color=colVal(logRes),
                        rstride=1, cstride=1, antialiased=False, shade=False)
    if y2 == max(ySum):
        ax.plot_surface(([x1, x2], [x1, x2]), ([y2, y2]), ([z1, z1], [z2, z2]), linewidth=1,
                        color=colVal(logRes),
                        rstride=1, cstride=1, antialiased=False, shade=False)
    if z1 == max(zSum):
        ax.plot_surface(([x1, x1], [x2, x2]), ([y1, y2], [y1, y2]), ([z1, z1]), linewidth=1,
                        color=colVal(logRes),
                        rstride=1, cstride=1, antialiased=False, shade=False)
    if z2 == min(zSum):
        ax.plot_surface(([x1, x1], [x2, x2]), ([y1, y2], [y1, y2]), ([z2, z2]), linewidth=1,
                        color=colVal(logRes),
                        rstride=1, cstride=1, antialiased=False, shade=False)

def wireframe(x1, x2, y1, y2, z1, z2):
    #
    if x1 == min(xSum):
        ax.plot_wireframe(([x1, x1]), ([y1, y2], [y1, y2]), ([z1, z1], [z2, z2]), linewidth=1)
    if x2 == max(xSum):
        ax.plot_wireframe(([x2, x2]), ([y1, y2], [y1, y2]), ([z1, z1], [z2, z2]), linewidth=1)

    if y1 == min(ySum):
        ax.plot_wireframe(([x1, x2], [x1, x2]), ([y1, y1]), ([z1, z1], [z2, z2]), linewidth=1)
    if y2 == max(ySum):
        ax.plot_wireframe(([x1, x2], [x1, x2]), ([y2, y2]), ([z1, z1], [z2, z2]), linewidth=1)

    if z1 == max(zSum):
        ax.plot_wireframe(([x1, x1], [x2, x2]), ([y1, y2], [y1, y2]), ([z1, z1]), linewidth=1)
    if z2 == min(zSum):
        ax.plot_wireframe(([x1, x1], [x2, x2]), ([y1, y2], [y1, y2]), ([z2, z2]), linewidth=1)

'''
Main program starts from here
'''
resMin = 1
resMax = 1000

xStart = 0
yStart = 0
zStart = 0

x = [100, 50 , 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 50, 100]
y = [100, 50 , 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 50, 100]
z = [10, 20, 30, 40, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]


z = np.multiply(z, -1)

res = 10

xSum = [xStart, np.sum(x)]
ySum = [yStart, np.sum(y)]
zSum = [zStart, np.sum(z)]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

m = cm.ScalarMappable(cmap=cm.jet_r, norm=LogNorm())
m.set_array([resMin, resMax])


cbar = plt.colorbar(m, shrink=0.8, aspect=10)
cbar.set_label('Resistivity', rotation=270)

x1 = xStart
x2 = x1 + x[0]
for i in range(0, len(x)):
    y1 = yStart
    y2 = y1 + y[0]
    for j in range(0, len(y)):
        z1 = zStart
        z2 = (z1 + z[0])
        for k in range(0, len(z)):
            if x1 == min(xSum) or x2 ==max(xSum) or y1 == min(ySum) or y2 ==max(ySum) or z2 == min(zSum) or z1 == max(zSum):
                surface(x1, x2, y1, y2, z1, z2, xSum, ySum, zSum, res)
                wireframe(x1, x2, y1, y2, z1, z2)
            if k < len(z) - 1:
                z1 = z2
                z2 = z1 + z[1 + k]
        if j < len(y)-1:
            y1 = y2
            y2 = y1 + y[1+j]
    if i < len(x)-1:
        x1 = x2
        x2 = x1 + x[1+i]

ax.set_xlabel('X')
# ax.set_xlim3d(0, 500)
ax.set_ylabel('Y')
# ax.set_ylim3d(0, 500)
ax.set_zlabel('Z')
# ax.set_zlim3d(-200, 0)

plt.show()
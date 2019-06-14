from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt


def plot_cub(center, xx, yy, zz, res):
    ox, oy, oz = center

    temp = 0
    x = []
    x.append(temp)
    for i in range(0,len(xx)):
    	temp += xx[i]
    	x.append(temp)

    temp = 0
    y = []
    y.append(temp)
    for i in range(0,len(yy)):
    	temp += yy[i]
    	y.append(temp)

    temp = 0
    z = []
    z.append(temp)
    for i in range(0,len(zz)):
    	temp -= zz[i]
    	z.append(temp)


    x1, z1 = np.meshgrid(x, z)
    y11 = np.zeros_like(x1)+(oy)
    y12 = np.zeros_like(x1)+(oy+max(y))
    x2, y2 = np.meshgrid(x, y)
    z21 = np.zeros_like(x2)+(oz)
    z22 = np.zeros_like(x2)+(oz+min(z))
    y3, z3 = np.meshgrid(y, z)
    x31 = np.zeros_like(y3)+(ox)
    x32 = np.zeros_like(y3)+(ox+max(y))

    #set resistivity value
    
    resMin = 1
    resMax = 1000

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    m = cm.ScalarMappable(cmap=cm.jet_r, norm=LogNorm())
    m.set_array([resMin, resMax])
    cbar = plt.colorbar(m, shrink=0.8, aspect=10)
    cbar.set_label('Resistivity', rotation=270)
    logRes = np.log10(res) / (np.log10(resMax))
    colVal = plt.get_cmap('jet_r')

    #linewidth
    lWidth = 0.003

    # outside surface
    ax.plot_surface(x1, y11, z1, color=colVal(logRes), rstride=1, cstride=1, alpha=1, antialiased=False, shade=False, linewidth=lWidth, edgecolors='xkcd:black')
    # inside surface
    ax.plot_surface(x1, y12, z1, color=colVal(logRes), rstride=1, cstride=1, alpha=1, antialiased=False, shade=False, linewidth=lWidth, edgecolors='xkcd:black')
    
    # left surface
    ax.plot_surface(x31, y3, z3, color=colVal(logRes), rstride=1, cstride=1, alpha=1, antialiased=False, shade=False, linewidth=lWidth, edgecolors='xkcd:black')
    # right surface
    ax.plot_surface(x32, y3, z3, color=colVal(logRes), rstride=1, cstride=1, alpha=1, antialiased=False, shade=False, linewidth=lWidth, edgecolors='xkcd:black')

    # bottom surface
    ax.plot_surface(x2, y2, z21, color=colVal(logRes), rstride=1, cstride=1, alpha=1, antialiased=False, shade=False, linewidth=lWidth, edgecolors='xkcd:black')
    # upper surface
    ax.plot_surface(x2, y2, z22, color=colVal(logRes), rstride=1, cstride=1, alpha=1, antialiased=False, shade=False, linewidth=lWidth, edgecolors='xkcd:black')
    
    ax.set_aspect('equal')
    
    # set axes name
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()




if __name__ == '__main__':

    center = [0, 0, 0]

    X = [1000, 500, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200, 500, 1000]
    Y = [1000, 500, 200, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 200, 500, 1000]
    Z = [10, 20, 30, 40, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]

    res = 100

    plot_cub(center, X, Y, Z, res)
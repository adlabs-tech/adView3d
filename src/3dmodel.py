from rgf_modem_datafile import readModelFile
from rgf_plot import *

from mayavi import mlab

import numpy as np

def calc(valval, code):

    temp = 0
    val = []
    val.append(temp)
    for i in range(0,len(valval)):
        if code == 'z':
            temp -= valval[i]
            val.append(temp)
        else:
            temp += valval[i]
            val.append(temp)

    return val

def calcMeshGrid(val_1, val_2, val_3, o, code):

    temp_1, temp_2 = np.meshgrid(val_1, val_3)
    temp_3 = np.zeros_like(temp_1) + (o)
    if code == 'z':
        temp_4 = np.zeros_like(temp_1) + (o + min(val_2))
    else:
        temp_4 = np.zeros_like(temp_1) + (o + max(val_2))

    return temp_1, temp_2, temp_3, temp_4

def setPlot(center, xx, yy, zz, res, resMin, resMax):

    ox, oy, oz = center

    x = calc(xx,'x')
    y = calc(yy,'y')
    z = calc(zz,'z')

    y3, z3, x31, x32 = calcMeshGrid(y, x, z, ox, 'x')
    x1, z1, y11, y12 = calcMeshGrid(x, y, z, oy, 'y')
    x2, y2, z21, z22 = calcMeshGrid(x, z, y, oz, 'z')

    res = np.full_like(z3, np.log10(500))
 
    # plot3DCubMlab(y3, z3, x31, x32, x1, z1, y11, y12, x2, y2, z21, z22, res, resMin, resMax)
    # plot3DCubPlt(y3, z3, x31, x32, x1, z1, y11, y12, x2, y2, z21, z22, 500, resMin, resMax)

if __name__ == '__main__':

	file = '../data/model.mod'

	nX, nY, nZ, x, y, z, array = readModelFile(file)

	center = [0, 0, 0]

	res = 100
	resMin = 1
	resMax = 1000

	# x = [100, 50, 50, 100]
	# y = [100, 50, 50, 100]
	# z = [10, 20, 30, 40]

	setPlot(center, x, y, z, res, resMin, resMax)

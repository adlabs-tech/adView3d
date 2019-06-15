from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt

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

def plotCub(ax, val_1, val_2, val_3, colVal, logRes, lWidth=None):

    ax.plot_surface(val_1, val_2, val_3, 
        color=colVal(logRes), 
        rstride=1, 
        cstride=1, 
        alpha=1, 
        antialiased=False, 
        shade=False, 
        linewidth=lWidth, 
        edgecolors='xkcd:black')

def setPlot(center, xx, yy, zz, res, resMin, resMax):

    ox, oy, oz = center

    x = calc(xx,'x')
    y = calc(yy,'y')
    z = calc(zz,'z')

    y3, z3, x31, x32 = calcMeshGrid(y, x, z, ox, 'x')
    x1, z1, y11, y12 = calcMeshGrid(x, y, z, oy, 'y')
    x2, y2, z21, z22 = calcMeshGrid(x, z, y, oz, 'z')

 
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    m = cm.ScalarMappable(cmap=cm.jet_r, norm=LogNorm())
    m.set_array([resMin, resMax])
    cbar = plt.colorbar(m)
    cbar.set_label('Resistivity', rotation=270)
    logRes = np.log10(res) / (np.log10(resMax))
    colVal = plt.get_cmap('jet_r')

    # x
    plotCub(ax, x31, y3, z3, colVal, logRes, 0.003)
    plotCub(ax, x32, y3, z3, colVal, logRes, 0.003)

    # y
    plotCub(ax, x1, y11, z1, colVal, logRes, 0.003)
    plotCub(ax, x1, y12, z1, colVal, logRes, 0.003)
    
    # z
    plotCub(ax, x2, y2, z21, colVal, logRes, 0.003)
    plotCub(ax, x2, y2, z22, colVal, logRes, 0.003)
       
    # set axes name
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Resistivity Model')
    plt.show()

def readFileElement(file):
	temp = file.readline().split()
	temp = [float(i) for i in temp] #convert a list containing string  to float

	return temp

def readFile(file):
	temp = file.readline() #read 1st line
	temp = file.readline() #read 2nd line - ignore it, will define using len
	
	x = readFileElement(file) #read 3rd line
	y = readFileElement(file) #read 4th line
	z = readFileElement(file) #read 5th line

	return x, y, z

if __name__ == '__main__':

	file = open('../data/model.mod','r')
	x, y, z = readFile(file)

	center = [0, 0, 0]

	res = 100
	resMin = 1
	resMax = 1000

	# x = [100, 50, 50, 100]
	# y = [100, 50, 50, 100]
	# z = [10, 20, 30, 40]

	setPlot(center, x, y, z, res, resMin, resMax)

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt

def plot_cub(center, xx, yy, zz, res, resMin, resMax):
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
    


    fig = plt.figure()
    ax = fig.gca(projection='3d')

    m = cm.ScalarMappable(cmap=cm.jet_r, norm=LogNorm())
    m.set_array([resMin, resMax])
    cbar = plt.colorbar(m)
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
    
    # ax.set_aspect('equal')
    
    # set axes name
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def readFileElement(file):
	temp = file.readline().split(' ')
	temp = [x for x in temp if x != ''] #remove element '' in list temp
	temp.remove('\n')
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

	file = open('model.mod','r')
	x, y, z = readFile(file)

	center = [0, 0, 0]

	res = 100
	resMin = 1
	resMax = 1000

	x = [1000, 500, 500, 1000]
	y = [1000, 500, 500, 1000]
	z = [10, 20, 30, 40]

	plot_cub(center, x, y, z, res, resMin, resMax)

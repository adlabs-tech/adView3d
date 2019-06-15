import numpy as np 

from mayavi import mlab

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
from matplotlib import cm
import matplotlib.pyplot as plt

def local_plot3DCubMlab(val_1, val_2, val_3, res, resMin, resMax):

    mlab.mesh(val_1, val_2, val_3, vmin=np.log10(resMin), vmax=np.log10(resMax), colormap="jet", opacity=1)
    # mlab.mesh(val_1, val_2, val_3, representation='wireframe', line_width=1, colormap="jet")

def plot3DCubMlab(y3, z3, x31, x32, x1, z1, y11, y12, x2, y2, z21, z22, res, resMin, resMax):
	# x
    local_plot3DCubMlab(x31, y3, z3, res, resMin, resMax)
    local_plot3DCubMlab(x32, y3, z3, res, resMin, resMax)

    # y
    local_plot3DCubMlab(x1, y11, z1, res, resMin, resMax)
    local_plot3DCubMlab(x1, y12, z1, res, resMin, resMax)
    
    # z
    local_plot3DCubMlab(x2, y2, z21, res, resMin, resMax)
    local_plot3DCubMlab(x2, y2, z22, res, resMin, resMax)
       
    mlab.scalarbar(orientation='horizontal', title='Resistivity', nb_labels=4, label_fmt='%.0f')
    # mlab.colorbar(orientation='horizontal', title='Resistivity', nb_labels=5, label_fmt='%.0f')
    
    mlab.axes()
    mlab.orientation_axes()
    mlab.show()

def local_plot3DCubPlt(ax, val_1, val_2, val_3, colVal, logRes, lWidth=None):

    ax.plot_surface(val_1, val_2, val_3, 
        color=colVal(logRes), 
        rstride=1, 
        cstride=1, 
        alpha=1, 
        antialiased=False, 
        shade=False, 
        linewidth=lWidth, 
        edgecolors='xkcd:black')

def plot3DCubPlt(y3, z3, x31, x32, x1, z1, y11, y12, x2, y2, z21, z22, res, resMin, resMax):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    m = cm.ScalarMappable(cmap=cm.jet_r, norm=LogNorm())
    m.set_array([resMin, resMax])
    cbar = plt.colorbar(m)
    cbar.set_label('Resistivity', rotation=270)
    logRes = np.log10(res) / (np.log10(resMax))
    colVal = plt.get_cmap('jet_r')

    # x
    local_plot3DCubPlt(ax, x31, y3, z3, colVal, logRes, 0.003)
    local_plot3DCubPlt(ax, x32, y3, z3, colVal, logRes, 0.003)

    # y
    local_plot3DCubPlt(ax, x1, y11, z1, colVal, logRes, 0.003)
    local_plot3DCubPlt(ax, x1, y12, z1, colVal, logRes, 0.003)
    
    # z
    local_plot3DCubPlt(ax, x2, y2, z21, colVal, logRes, 0.003)
    local_plot3DCubPlt(ax, x2, y2, z22, colVal, logRes, 0.003)
       
    # set axes name
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Resistivity Model')
    plt.show()
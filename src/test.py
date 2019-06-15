#Minimum working example
from numpy import array, sin, cos, mgrid, pi, sqrt
from mayavi import mlab

mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))
u, v = mgrid[- 0.035:pi:0.01, - 0.035:pi:0.01]

X = 2 / 3. * (cos(u) * cos(2 * v)
    + sqrt(2) * sin(u) * cos(v)) * cos(u) / (sqrt(2) -
                                             sin(2 * u) * sin(3 * v))
Y = 2 / 3. * (cos(u) * sin(2 * v) -
    sqrt(2) * sin(u) * sin(v)) * cos(u) / (sqrt(2)
    - sin(2 * u) * sin(3 * v))
Z = -sqrt(2) * cos(u) * cos(u) / (sqrt(2) - sin(2 * u) * sin(3 * v))

for i in range(1,2):
    S = Y
    print(S)
    _m = mlab.mesh(X, Y, Z, scalars=S, colormap='YlGnBu', )
    mlab.view(.0, - 5.0, 4)
    mlab.colorbar(orientation='vertical')
    _m.module_manager.scalar_lut_manager.use_default_range = False
    _m.module_manager.scalar_lut_manager.data_range = array([-1., 10.])
    _m.module_manager.scalar_lut_manager.scalar_bar.position = array([ 0.01,  0.15])
    _m.module_manager.scalar_lut_manager.scalar_bar.position2 = array([ 0.1,  0.8])
    mlab.show()
    mlab.close(all=True)
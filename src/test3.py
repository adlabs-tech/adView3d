import numpy as np 
from mayavi import mlab 

import time

# Create cone 
n = 8 
t = np.linspace(-np.pi, np.pi, n) 
z = np.exp(1j*t) 
x = z.real.copy() 
y = z.imag.copy() 
z = np.zeros_like(x) 
triangles = [(0, i, i+1) for i in range(n)] 
x = np.r_[0, x] 
y = np.r_[0, y] 
z = np.r_[1, z] 
t = np.r_[0, t] 

# These are the scalar values for each triangle 
f = np.mean(t[np.array(triangles)], axis=1) 

# Plot it 
mesh = mlab.triangular_mesh(x, y, z, triangles, 
                                    representation='wireframe', 
                                                                opacity=0) 
mesh.mlab_source.dataset.cell_data.scalars = f 
mesh.mlab_source.dataset.cell_data.scalars.name = 'Cell data' 
mesh.mlab_source.update() 
mesh.parent.update()

mesh2 = mlab.pipeline.set_active_attribute(mesh, 
                cell_scalars='Cell data') 
s2 = mlab.pipeline.surface(mesh2) 


mlab.show()
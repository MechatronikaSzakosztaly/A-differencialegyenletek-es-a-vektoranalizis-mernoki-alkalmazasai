# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:08:37 2019

@author: Bence Sipos
"""
import numpy as np
import matplotlib.pyplot as plt


size_u = 12
size_v = 12

# https://stackoverflow.com/questions/42147776/producing-2d-perlin-noise-with-numpy
def perlin(x,y,seed=0):
    # permutation table
    np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
    p = np.stack([p,p]).flatten()
    # coordinates of the top-left
    xi = x.astype(int)
    yi = y.astype(int)
    # internal coordinates
    xf = x - xi
    yf = y - yi
    # fade factors
    u = fade(xf)
    v = fade(yf)
    # noise components
    n00 = gradient(p[p[xi]+yi],xf,yf)
    n01 = gradient(p[p[xi]+yi+1],xf,yf-1)
    n11 = gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
    n10 = gradient(p[p[xi+1]+yi],xf-1,yf)
    # combine noises
    x1 = lerp(n00,n10,u)
    x2 = lerp(n01,n11,u) # FIX1: I was using n10 instead of n01
    return lerp(x1,x2,v) # FIX2: I also had to reverse x1 and x2 here

def lerp(a,b,x):
    "linear interpolation"
    return a + x * (b-a)

def fade(t):
    "6t^5 - 15t^4 + 10t^3"
    return 6 * t**5 - 15 * t**4 + 10 * t**3

def gradient(h,x,y):
    "grad converts h to the right gradient vector and return the dot product with (x,y)"
    vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
    g = vectors[h%4]
    return g[:,:,0] * x + g[:,:,1] * y

lin = np.linspace(0,5,size_u,endpoint=False)
x,y = np.meshgrid(lin,lin) 

noise = perlin(x,y,seed=22)
plt.imshow(noise,origin='upper')

from geomdl import construct
from geomdl import fitting
from geomdl.visualization import VisMPL as vis


points = []

for i in range(1, size_v):
    for j in range(1, size_u):
        #print([i,j,noise[i,j]*10])
        points.append([i,j,(noise[i,j])])


degree_u = 4
degree_v = 4

# Do global surface approximation
surf = fitting.interpolate_surface(points, size_u-1, size_v-1, degree_u, degree_v)
# surf = fitting.approximate_surface(points, size_u, size_v, degree_u, degree_v, ctrlpts_size_u=3, ctrlpts_size_v=4)

# Extract curves from the approximated surface
surf_curves = construct.extract_curves(surf)
plot_extras = [
    dict(
        points=surf_curves['u'][0].evalpts,
        name="u",
        color="cyan",
        size=5
    ),
    dict(
        points=surf_curves['v'][0].evalpts,
        name="v",
        color="magenta",
        size=5
    )
]

# Plot the interpolated surface
surf.delta = 0.05
surf.vis = vis.VisSurface()
surf.render()#extras=plot_extras)


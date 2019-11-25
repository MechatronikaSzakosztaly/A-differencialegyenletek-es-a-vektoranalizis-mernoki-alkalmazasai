# -*- coding: utf-8 -*-
#%matplotlib qt
import numpy as np
import matplotlib.pyplot as plt

L = 0.1
n = 20
T0 = 0
T1s = 0
T2s = 0
dx = L/n
alpha = 0.0002
t_final = 10
dt = 0.05
probeT=[]

x = np.linspace(dx/2, L-dx/2, n)

T = np.sin(1*np.pi*x/L)*60
dTdt = np.empty(n)

t = np.arange(0, t_final, dt)

probeT = np.zeros(int(t_final/dt))

for j in range(1, len(t)):
    plt.clf()
    for i in range(1, n-1):
        dTdt[i] = alpha*(-(T[i]-T[i-1])/dx**2+(T[i+1]-T[i])/dx**2)
    dTdt[0] = alpha*(-(T[0]-T1s)/dx**2+(T[1]-T[0])/dx**2)
    dTdt[n-1] = alpha*(-(T[n-1]-T[n-2])/dx**2+(T2s-T[n-1])/dx**2)

    T = T + dTdt*dt
    probeT[j]=T[5]
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(x, T)
    plt.axis([0, L, -50, 50])
    plt.xlabel('Hossz [m]')
    plt.ylabel('Hőmérséklet [C fok]')
    
    
    plt.subplot(2,1,2)
    plt.plot(t, probeT)
    plt.axis([0, 10, -50, 50])
    plt.xlabel('Idő [t]')
    plt.ylabel('Hőmérséklet [C fok]')
    
    plt.show()
    plt.pause(0.01)

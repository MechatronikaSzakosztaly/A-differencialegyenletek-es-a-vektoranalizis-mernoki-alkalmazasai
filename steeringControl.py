# -*- coding: utf-8 -*-

#%matplotlib qt <-ez csak akkor ha jupíter notebook

import numpy as np
import matplotlib.pyplot as plt
dList = [0]
eList=[2.75]
ddList = [0]
IdList = [0]
fiList = [0]

tList = [0]
t = 0
v = 30 #m/sec
dDesired = 2.75
desiredList = [dDesired]
dt = 0.0001

P=0.05
I=0.01
D=0

steeringBound = 0.00001

while t < 10:
    tList.append(t)
    d = dList[-1]
    
    ### Ide írjátok meg a szabályozó függvényeteket! ###
    ### elist[-1]<- előző hiba, IdList[-1]<-hiba téglaintegrálja, ddList[-1]<- hiba közelítő deriváltja ###
    fi = eList[-1]*P+IdList[-1]*I+ddList[-1]*D
    ### szabályozó függény vége ###
    
    dfi = fi-fiList[-1]
    if dfi>0.001:
        fi = fiList[-1]+steeringBound
    if dfi<-0.001:
        fi = fiList[-1]-steeringBound
    fiList.append(fi)
    d += v*dt*np.sin(fi)
    dList.append(d)
    eList.append(dDesired-d)
    Id = IdList[-1] + eList[-1]*dt
    IdList.append(Id)
    dd = (eList[-1]-eList[-2])/dt
    ddList.append(dd)
    desiredList.append(dDesired)
    t+=dt
    
plt.figure('Az autó útja')
plt.plot(tList, dList)
plt.plot(tList, desiredList)
#plt.plot(tList, eList)
plt.show()
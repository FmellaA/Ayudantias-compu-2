import numpy as np 
import matplotlib.pyplot as plt 
from InterpolationMethods import Lagrangian

## el libro de donde se baso la ayudantia: https://e6.ijs.si/~roman/files/tmp/M.Heath-SComputing/scientific-computing-michael-t-heath.pdf

# Datapoints: 

t = np.array([1,2,3,4,5])
y = np.array([1,1,2,6,24])

# a ----------------------------------------------

#Usando "Lagrangian Interpolation": 

x = np.linspace(1,5,100)

plt.scatter(t,y, color='red')
plt.plot(x,Lagrangian(x,t,y))
plt.show()

# b -----------------------------------------------

M = [0,(6+18/14)/4,-18/14,(84+18/14)/4,0]

def splines(x): 
    p = np.zeros(len(x))
    for k, xe in enumerate(x): 
        i = np.searchsorted(t,xe) - 1 #procura qye estemos dentro del intervalo 
        if i== len(t)-1: 
            i -=1

        p[k] = (M[i]*(t[i+1] - xe)**3 / (6) 
        +  M[i+1]*(xe-t[i])**3/6
        +(y[i] - M[i]/6)*(t[i+1]-xe) 
        + (y[i+1] - M[i+1]/6)*(xe-t[i]))
    
    return p 




plt.scatter(t,y, color='red')
plt.plot(x, splines(x))
plt.show()
import matplotlib.pyplot as plt 
import numpy as np


def Newton(f,h,x0,eps=1e-4): 
    n=0
    while np.abs(f(x0)/h(x0))> eps and np.abs(f(x0))>eps and n<30: 
        x0 = x0 - f(x0)/h(x0)  
        n= n+1
    return x0

 
l = lambda x: np.exp(1)*x**5-4
dl = lambda x: 5*np.exp(1)*x**4    

re, im = np.mgrid[-10:10:500j, -10:10:500j] #ahi el j dice que tenga 10 elementos

x0 = re + 1j*im

# plt.scatter(x0.real, x0.imag)
# plt.show()

x = x0.copy()
for i, RE in enumerate(re): #le da un indice a cada uno de los elementos (indice, valor)
    for j,IM in enumerate(im): 
        x[i,j] = Newton(l,dl, x0=x0[i,j], eps=1e-4)


plt.scatter(x0.real, x0.imag)
plt.pcolor(x0.real, x0.imag, np.angle(x) )
# plt.scatter(x.real, x.imag, color='red')
plt.colorbar()
plt.show()

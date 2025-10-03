import numpy as np 
import matplotlib.pyplot as plt 
import os

datos = np.genfromtxt("Datos01.txt", delimiter="\t", skip_header=2)

t = datos[:, 0]
Voltaje = datos[:, 1]
dV_dt = (Voltaje[1:] - Voltaje[:-1]) / (t[1:] - t[:-1])
t_prime = (t[1:] + t[:-1]) / 2

plt.scatter(t,Voltaje, label= 'Normal')
plt.scatter(t_prime, dV_dt, label=r"$\frac{\Delta V}{\Delta t}$")

# Detalles del Canvas
plt.xlabel('t [s]')
plt.ylabel('[V]')
plt.legend()
#plt.xlim(0,1)
plt.legend()
plt.show()

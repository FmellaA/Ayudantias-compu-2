import numpy as np 
import matplotlib.pyplot as plt 
import os

'''
Descargue los datos "Datos01.txt", corra este código y proponga una derivada finita numérica para aplicarla a los datos. Al correr el código tenga precaución de la ubicación del archivo de datos, del código y la ubicación en la que esta la terminal. 
'''

datos = np.genfromtxt("Datos01.txt", delimiter="\t", skip_header=2)

t = datos[:, 0]
Voltaje = datos[:, 1]
dV_dt = (Voltaje[1:] - Voltaje[:-1])/(t[1:] - t[:-1])
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

'''
with open("output.txt", "w") as file: 
        for i in range(len(t)):
            file.write(f"{t[i]}\t{funcion de su preferencia(t[i])}\n")'''




















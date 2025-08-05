import numpy as np 

# Para funciones f(x,t), donde se deben definir las condiciones iniciales

# Métido de Euler

def euler(f, x, N, dt=0.01): 
    # se debe definir la condición inicial para x : x[0].
    for i in range(N-1): 
        x[i+1] = x[i] + f(x[i], i*dt)*dt

    return x

# Método de Euler-Cromer


# Método del Salto de Rana 

def Rana(f,x,v,N, dt=0.01):
    for n in range(N-1):
        vmedio = v[n] + 0.5*dt*f(x[n])
        x[n+1] = x[n] + dt*vmedio
        v[n+1] = vmedio + 0.5*dt*f(x[n+1])
    return x, v 

# Método de Runge-Kutta (cuarto orden)

def runge_kutta(f, u, t, h=0.01):

    for n in range(t.size - 1):
        k1 = f(u[n], t[n])
        k2 = f(u[n] + 0.5*h*k1, t[n] + 0.5*h)
        k3 = f(u[n] + 0.5*h*k2, t[n] + 0.5*h)
        k4 = f(u[n] + h*k3, t[n] + h)

        u[n+1] = u[n] + (h/6)*(k1 + 2*k2 + 2*k3 + k4) 
    return u

# Con N y h a gusto del consumidor. 
# x = np.zeros(N)
# x[0] = 1
# x = runge_kutta(f, x, t ,h)




import numpy as np

# Se definirán método de búsqueda de raíces para funciones f de un argumento. Para funciones de más argumentos deberán editar las reglas.  

# Método de Bisección

def biseccion(f, a, b, N=100, *args, **kwargs): 
    x = np.linspace(a, b, N)
    F = f(x, *args, **kwargs)
    dF = F[1:]*F[:-1]

    i = np.where(dF<0)[0]
    return x[i]

# Método de la secante

def secante(f, x0, x1, tol = 1e-3, *args, **kwargs): 
    # x0 y x1 se necesitarán dos semillas
    def g(x): 
        return f(x,*args, **kwargs)
    while np.abs(x1-x0)>tol: 
        x2 = x0 - (g(x0)*(x1-x0))/(g(x1)-g(x0))
        x0,x1 = x1,x2
    return x2 

# Método de Newton Rhapson    

def newton_rhapson1(f,h,x0,eps=1e-4, nmax =30): 
    n=0
    while np.abs(f(x0)/h(x0))> eps and np.abs(f(x0))>eps and n<nmax: 
        # mientras este fuera del radio de convergencia
        x0 = x0 - f(x0)/h(x0)  
        n= n+1
    return x0


# Regla del Punto Fijo
def punto_f(g, x0, eps=1e-6, max_it=50, *args, **kwargs): 
    iteracion = 0 

    while iteracion < max_it: 
        x_nueva = g(x0, *args, **kwargs)
        if abs(x_nueva-x0) < eps: 
            # print(f'Convergencia alcanzada con {iteracion + 1} iteraciones')
            return x_nueva
        
        x0 = x_nueva
        iteracion += 1
    # print('No convergió')
    return None

#Método de Euler Implicito: 

def euler_implicito(y, f, x0, t, h, *args, **kwargs): #orden 1 
    for n in range(len(t)-1): 
        y[n+1] = punto_f(f,y[n], *args, **kwargs)
    return y

# Método de Newton

def Newton(f,h,x0,eps=1e-4): 
    n=0
    while np.abs(f(x0)/h(x0))> eps and np.abs(f(x0))>eps and n<30: 
        x0 = x0 - f(x0)/h(x0)  
        n= n+1
    return x0
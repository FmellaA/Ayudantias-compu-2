import numpy as np 

# Se definirán diferentes métodos de integración numéricos para una función f de un argumento. Para funciones de más argumentos deberán editar las reglas. 

# Regla de Simpson

def simp(f, a, b): 
    simpson = ((b-a)/6)*(f(a) + 4*f((a+b)*0.5) + f(b))
    return simpson

# Regla del trapecio

def trap(f, a, b):
    return ((b-a)*(f(a)+f(b)))*0.5

# Regla del punto medio

def pmed(f,a,b): 
    return (b-a)*f((b+a)*0.5)

# Podremos integrar: 

# def integ(f,a,x,g): #definimos: (la funcion a integrar, limite inferior, eje x, tecnica d integracion)
#     intervalos = np.linspace(a,x,10000) #intervalos de integracion
#     integ = 0.0 
#     for i in range(len(intervalos)-1): 
#         integ +=  g(f, intervalos[i], intervalos[i+1]) #en cada intervalito se hace la regla para que se más preciso 
#     return integ 
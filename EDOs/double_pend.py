#En este código resolveremos el problema del péndulo sobre usando el método de Runge-Kutta de 4to orden.
#Lo primero que tenemso que hacer es importar todos los paquetes y módulos necesarios;
import numpy as np
import matplotlib.pyplot as plt

#Luego, definimos los parámetros iniciales, como lo son;
dt = 0.01 #Paso de tiempo
t = np.linspace(0,30, int(30/dt)) #Tiempo seteado para 30 segundos

#Luego, usando los parámetros que se han indicado en las instrucciones, planteamos las ecuaciones de movimiento como ecuaciones vectoriales, pasando de tener 2 ecuaciones diferenciales ordinarias acopladas de 2do orden a tener 4 ecuaciones diferenciales ordinarias acopladas, pero de primer orden;

def double_pend(u,t, m1, m2, l1, l2, g):
    """
    Ecuaciones de movimiento para el péndulo doble derivadas del Lagrangeano (visitar wikipedia para más información)
    Args:
        u : El vector a resolver usando métodos numéricos para ecuaciones diferenciales ordinarias
        m1, m2: Masas de los dos péndulos.
        l1, l2: Largo de los dos péndulos.
        g: Aceleración de gravedad en la tierra.
    """
    #Primero lo primero definimos el vector u a resolver, que está compuesto de theta 1 y 2 y sus derivadas w1 y 2
    theta1, theta2, w1, w2 = u

    #Luego empezamos a armar el lego de ecuaciones por partes, esto es siempre recomendable siempre que se tengan ecuaciones de movimiento muy complicadas, con tendencia a equivocarse a la hora de escribirlas en el computador, es más fácil trabajarlas por pedazos

    alpha = (m1 + m2) * l1**2
    beta = m2 * l1 * l2 * np.cos(theta1 - theta2)
    gamma = m2 * l2**2
    delta = m2 * l1 * l2 * (w2**2) * np.sin(theta1 - theta2) + l1 * g * (m1 + m2) * np.sin(theta1)
    epsilon = -m2 * l1 * l2 * (w1**2) * np.sin(theta1 - theta2) + l2 * m2 * g * np.sin(theta2)
    
    #Ahora devolvemos las ecuacioens de movimiento según las ecuaciones planteadas de forma vectorial, es decir, devolver a lo que son iguales los theta 1 y 2 tanto como w 1 y 2 en las ecuaciones de movimiento dadas.

    return np.array([w1,
                     w2,
                     (-beta / alpha) * (((delta * beta) / alpha - epsilon) / (gamma - (beta**2) / alpha)) - delta / alpha,
                     ((beta * delta) / alpha - epsilon) / (gamma - (beta**2) / alpha)])

#Con esto tenemos lista la función a resolver;

plt.style.use("dark_background") #Use el que más le guste, a mi me duelen los ojos con el blanco xd

#Este es uno de los pasos más importantes, en el cual definirán las condiciones iniciales que darán origen a su resultado (juegue cambiand las condicioens iniciales por valores muy pequeños entre sí y note cómo cambia la trayectoria de los péndulos :O)

m1 , m2 , l1 , l2 , g = 1 ,2 ,3 ,1 ,9.81

initial_conditions = np.array([np.pi/4,
                                np.pi/4,
                                0,
                                0])
#Ahora cocinamos el resultado usando el método de Runge-Kutta de 4to orden, en este caso estará explícito en el códido pero se recomiento usarlo como un módulo para limpieza;
def runge_kutta_4(f, u0, t, *args, **kwargs):
    """
    Resuelve una ecuación diferencial ordinaria (EDO) utilizando el método de Runge-Kutta de cuarto orden.

    Args:
        f: La función que define la EDO, de la forma f(u, t, *args, **kwargs).
        u0: El valor inicial de la variable dependiente (u) en el tiempo t[0].
        t: Un array de NumPy que representa los puntos de tiempo en los que se desea calcular la solución.
        *args: Argumentos adicionales para pasar a la función f.
        **kwargs: Argumentos de palabra clave adicionales para pasar a la función f.

    Returns:
        Un array de NumPy que contiene la solución aproximada de la EDO en los puntos de tiempo especificados en t.
    """
    N = len(t) #Size of the time array
    u = np.zeros([N, len(u0)], dtype=u0.dtype) # Initialize u as a 2D array
    dt = t[1] - t[0] #Consistent time step among the time array
    u[0] = u0 # Set the initial condition

    for n in range(N - 1):
        
        k1 = f(u[n], t[n], *args, **kwargs)
        k2 = f(u[n] + 0.5 * dt * k1, t[n] + 0.5 * dt, *args, **kwargs)
        k3 = f(u[n] + 0.5 * dt * k2, t[n] + 0.5 * dt, *args, **kwargs)
        k4 = f(u[n] + dt * k3, t[n] + dt, *args, **kwargs)

        u[n + 1] = u[n] + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    return u
# Por tanto, ahora simplemente llamamos a nuestra función y cocinamos los resultados con los parámetros y condiciones iniciales que hemos definido;

results = runge_kutta_4(double_pend, initial_conditions, t, m1, m2, l1, l2, g)

#Ahora, como estamos en coordenadas polares, es necesario pasar a coordenadas cartesianas para así calcular la trayectoria de los péndulos;
#Primero extraemos los resultados de forma explícita
# Extraer resultados
theta1 = results[:, 0]
theta2 = results[:, 1]
w1 = results[:, 2]
w2 = results[:, 3]

# Convertir a coordenadas cartesianas
x1 = l1 * np.sin(theta1)
y1 = -l1 * np.cos(theta1)
x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)

# Energía cinética
v1_squared = (l1 * w1)**2
v2_squared = (l1 * w1)**2 + (l2 * w2)**2 + 2 * l1 * l2 * w1 * w2 * np.cos(theta1 - theta2)

T1 = 0.5 * m1 * v1_squared
T2 = 0.5 * m2 * v2_squared
T = T1 + T2

# Energía potencial (CORRECTA)
U1 = m1 * g * (-l1 * np.cos(theta1))  # Altura desde el punto de pivote
U2 = m2 * g * (-l1 * np.cos(theta1) - l2 * np.cos(theta2))
U = U1 + U2

E_total = T + U
#Finalmente, graficamos todo en un hermoso subplots para ver todos los resultados de una vez
plt.subplot(2, 2, 1)
plt.plot(x1, y1, label='Péndulo 1', alpha=0.7)
plt.plot(x2, y2, label='Péndulo 2', alpha=0.7)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trayectorias de los Péndulos')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axis('equal')

# Graficar espacio de fases
plt.subplot(2, 2, 2)
plt.plot(theta1, w1, label='Péndulo 1', alpha=0.7)
plt.plot(theta2, w2, label='Péndulo 2', alpha=0.7)
plt.xlabel('θ (rad)')
plt.ylabel('ω (rad/s)')
plt.title('Espacio de Fases')
plt.legend()
plt.grid(True, alpha=0.3)

# Graficar ángulos vs tiempo
plt.subplot(2, 2, 3)
plt.plot(t, theta1, label='θ₁', alpha=0.7)
plt.plot(t, theta2, label='θ₂', alpha=0.7)
plt.xlabel('Tiempo (s)')
plt.ylabel('θ (rad)')
plt.title('Ángulos vs Tiempo')
plt.legend()
plt.grid(True, alpha=0.3)

# Graficar energía total
plt.subplot(2, 2, 4)
plt.plot(t, E_total, 'r-', label='Energía Total', alpha=0.7)
plt.xlabel('Tiempo (s)')
plt.ylabel('Energía (J)')
plt.title('Energía Total del Sistema')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

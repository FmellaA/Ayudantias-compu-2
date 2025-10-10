import numpy as np

'''
%%%%%%%%%%%%%%%%%%%%%%%%%%%% ¡¡¡¡ Disclaimer !!! %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


 No se aconseja utilizar los siguientes métodos para el curso ya que no están dentro de los contenidos, sino que se añanden a modo demostrativo/dato curioso para futuro

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Como dato curioso, el método de Runge-Kutta puede ser definido para ordenes mayores, lo que le otorga mucha más precisión, que puede ser útiles en sistemas altamente sensibles (como lo es la mecánica celeste).
He aquí el método de Runge-Kutta de 8vo orden versión simplificada de carácter demostrativo, no usar, ya que los coeficientes reales son de la siguiente función.
'''
def runge_kutta_8_simplified(f, u0, t, *args, **kwargs):
    """
    Versión simplificada de Runge-Kutta de 8vo orden.
    """
    N = len(t)
    u = np.zeros([N, len(u0)], dtype=u0.dtype)
    dt = t[1] - t[0]
    u[0] = u0

    for n in range(N - 1):
        # 13 etapas para RK8 (versión simplificada)
        k1 = f(u[n], t[n], *args, **kwargs)
        k2 = f(u[n] + dt * (1/18) * k1, t[n] + dt/18, *args, **kwargs)
        k3 = f(u[n] + dt * (1/48) * k1 + dt * (1/16) * k2, t[n] + dt/12, *args, **kwargs)
        k4 = f(u[n] + dt * (1/32) * k1 + dt * (3/32) * k3, t[n] + dt/8, *args, **kwargs)
        k5 = f(u[n] + dt * (5/16) * k1 - dt * (75/64) * k3 + dt * (75/64) * k4, 
               t[n] + 5*dt/16, *args, **kwargs)
        k6 = f(u[n] + dt * (3/80) * k1 + dt * (3/16) * k4 + dt * (3/20) * k5, 
               t[n] + 3*dt/8, *args, **kwargs)
        k7 = f(u[n] + dt * (29443841/614563906) * k1 + dt * (77736538/692538347) * k4 + 
               dt * (28693883/1125000000) * k5 + dt * (23124283/1800000000) * k6, 
               t[n] + 59*dt/400, *args, **kwargs)
        k8 = f(u[n] + dt * (16016141/946692911) * k1 + dt * (61564180/158732637) * k4 + 
               dt * (22789713/633445777) * k5 + dt * (545815736/2771057229) * k6 + 
               dt * (180193667/1043307555) * k7, t[n] + 93*dt/200, *args, **kwargs)
        
        # Combinación final de 8vo orden (coeficientes simplificados)
        u[n + 1] = u[n] + dt * (
            0.03488520 * k1 +
            0.14001010 * k2 + 
            0.19712567 * k3 +
            0.20816796 * k4 +
            0.16571417 * k5 +
            0.14309107 * k6 +
            0.08500503 * k7 +
            0.02600080 * k8
        )

    return u

#Nótese que esta versión es altamente simplificada, la versión algo más cercana a la que debería ser es la siguiente.

def runge_kutta_8(f, u0, t, *args, **kwargs):
    """
    Resuelve una ecuación diferencial ordinaria (EDO) utilizando el método de 
    Runge-Kutta de octavo orden (Dormand-Prince 8(7)).
    
    Args:
        f: La función que define la EDO, de la forma f(u, t, *args, **kwargs).
        u0: El valor inicial de la variable dependiente (u) en el tiempo t[0].
        t: Un array de NumPy con espaciado constante que representa los puntos de tiempo.
        *args: Argumentos adicionales para pasar a la función f.
        **kwargs: Argumentos de palabra clave adicionales para pasar a la función f.
    
    Returns:
        Un array de NumPy que contiene la solución aproximada de la EDO en los puntos 
        de tiempo especificados en t.
    """
    N = len(t)
    u = np.zeros([N, len(u0)], dtype=u0.dtype)
    dt = t[1] - t[0]
    u[0] = u0

    # Coeficientes Butcher tableau para Dormand-Prince 8(7)
    # (Simplificado - en la práctica se usarían coeficientes completos)
    for n in range(N - 1):
        k1 = f(u[n], t[n], *args, **kwargs)
        k2 = f(u[n] + dt * (1/18) * k1, t[n] + dt * (1/18), *args, **kwargs)
        k3 = f(u[n] + dt * (1/48) * k1 + dt * (1/16) * k2, 
               t[n] + dt * (1/12), *args, **kwargs)
        k4 = f(u[n] + dt * (1/32) * k1 + dt * (3/32) * k3, 
               t[n] + dt * (1/8), *args, **kwargs)
        k5 = f(u[n] + dt * (5/16) * k1 - dt * (75/64) * k3 + dt * (75/64) * k4, 
               t[n] + dt * (5/16), *args, **kwargs)
        k6 = f(u[n] + dt * (3/80) * k1 + dt * (3/16) * k4 + dt * (3/20) * k5, 
               t[n] + dt * (3/8), *args, **kwargs)
        k7 = f(u[n] - dt * (29443841/614563906) * k1 + dt * (77736538/692538347) * k4 - 
               dt * (28693883/1125000000) * k5 + dt * (23124283/1800000000) * k6, 
               t[n] + dt * (59/400), *args, **kwargs)
        k8 = f(u[n] + dt * (16016141/946692911) * k1 + dt * (61564180/158732637) * k4 + 
               dt * (22789713/633445777) * k5 + dt * (545815736/2771057229) * k6 - 
               dt * (180193667/1043307555) * k7, 
               t[n] + dt * (93/200), *args, **kwargs)
        k9 = f(u[n] + dt * (39632708/573591083) * k1 - dt * (433636366/683701615) * k4 - 
               dt * (421739975/2616292301) * k5 + dt * (100302831/723423059) * k6 + 
               dt * (790204164/839813087) * k7 + dt * (800635310/3783071287) * k8, 
               t[n] + dt * (5490023248/9719169821), *args, **kwargs)
        k10 = f(u[n] - dt * (246121993/1340847787) * k1 - dt * (37695042795/15268766246) * k4 - 
                dt * (309121744/1061227803) * k5 - dt * (12992083/490766935) * k6 + 
                dt * (6005943493/2108947869) * k7 + dt * (393006217/1396673457) * k8 + 
                dt * (123872331/1001029789) * k9, 
                t[n] + dt * (13/20), *args, **kwargs)
        k11 = f(u[n] - dt * (1028468189/846180014) * k1 + dt * (8478235783/508512852) * k4 + 
                dt * (1311729495/1432422823) * k5 - dt * (10304129995/1701304382) * k6 - 
                dt * (48777925059/3047939560) * k7 + dt * (15336726248/1032824649) * k8 - 
                dt * (45442868181/3398467696) * k9 + dt * (3065993473/597172653) * k10, 
                t[n] + dt * (1201146811/1299019798), *args, **kwargs)
        k12 = f(u[n] + dt * (185892177/718116043) * k1 - dt * (3185094517/667107341) * k4 - 
                dt * (477755414/1098053517) * k5 - dt * (703635378/230739211) * k6 + 
                dt * (5731566787/1027545527) * k7 + dt * (5232866602/850066563) * k8 - 
                dt * (4093664535/808688257) * k9 + dt * (3962137247/1805957418) * k10 + 
                dt * (65686358/487910083) * k11, 
                t[n] + dt, *args, **kwargs)
        
        # Combinación final de 8vo orden
        u[n + 1] = u[n] + dt * (
            (14005451/335480064) * k1 + 
            (0) * k2 + 
            (0) * k3 + 
            (0) * k4 + 
            (-59238493/1068277825) * k5 + 
            (181606767/758867731) * k6 + 
            (561292985/797845732) * k7 + 
            (-1041891430/1371343529) * k8 + 
            (760417239/1151165299) * k9 + 
            (118820643/751138087) * k10 + 
            (-528747749/2220607170) * k11 + 
            (1/4) * k12
        )

    return u

#En la mayoría de casos no es necesario usar un método tan largo y basta con tan solo usar Runge-Kutta de 4to orden.
#Para más información, buscar Butcher Tableau.

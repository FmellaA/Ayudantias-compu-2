## **Ayudantía 24/10** -  *Física computacional II*

#### El péndulo doble

Considerando las siguientes ecuaciones diferenciales

$$
\begin{align}
    (m_1 + m_2)l_1^2 \ddot{\theta}_1 + m_2 l_1 l_2 \ddot{\theta}_2 \cos(\theta_1 - \theta_2) + m_2 l_1 l_2 \dot{\theta}_2^2 \sin(\theta_1 - \theta_2) + (m_1 + m_2) g l_1 \sin(\theta_1) &= 0 \\
    m_2 l_2^2 \ddot{\theta}_2 + m_2 l_1 l_2 \ddot{\theta}_1 \cos(\theta_1 - \theta_2) - m_2 l_1 l_2 \dot{\theta}_1^2 \sin(\theta_1 - \theta_2) + m_2 g l_2 \sin(\theta_2) &= 0
\end{align}
$$

también llamadas Ecuaciones Diferenciales de Euler-Lagrange para los ángulos $\theta_1$ y $\theta_2$ respectivamente, mientras $m_1$ y $m_2$ son las masas del objeto uno y dos; y $l_1$ y $l_2$ serán los largos de las respectivas cuerdas. **(1)** Reescriba el sistema utilizando las siguientes substituciones:

$$
\begin{align*}
    \alpha &\equiv (m_1 + m_2)l_1^2, \\
    \beta &\equiv m_2l_1l_2\cos(\theta_1 - \theta_2), \\
    \gamma &\equiv m_2l_2^2, \\
    \delta &\equiv m_2l_1l_2\dot{\theta}_2^2\sin(\theta_1 - \theta_2) + l_1g(m_1 + m_2)\sin(\theta_1), \\
    \epsilon &\equiv -m_2l_1l_2\dot{\theta}_1^2\sin(\theta_1 - \theta_2) + l_2m_2g\sin(\theta_2).
\end{align*}
$$

<!--
Al hacerlo se llega a

$$
\begin{align}
    \alpha \ddot \theta_1 + \beta \ddot \theta_2 + \delta &= 0 \label{p2_1} \\
    \gamma \ddot \theta_2 + \beta \ddot \theta_1 + \epsilon &= 0. \label{p2_2}
\end{align}
$$
-->

**(2)** A partir de la expresion a la que se llega, defina la función vectorial **analítica y numéricamente.**

<!--
Analíticamente:
$$
\begin{align}
    \dot \omega_1 &=\frac{-\beta \left( \frac{\beta \delta}{\alpha} -\epsilon\right)}{\alpha\left(\gamma -\frac{\beta^2}{\alpha}\right)} - \frac{\delta}{\alpha}\\
    \dot \omega_2 &= \frac{\frac{\beta \delta}{\alpha} - \epsilon}{\gamma - \frac{\beta^2}{\alpha}}.
\end{align}
$$
Numéricamente: 

```python
    def f_vectorial(X, t, m1=m1, m2=m2, l1=l1, l2=l2): 
        O1, O2, w1, w2 = X  #theta_1, theta_2, omega_1, omega_2
        a = (m1 + m2) * l1**2 
        b = m2 * l1 * l2 * np.cos(O1 - O2)
        y = m2 * l2**2
        d = m2 * l1 * l2 * w2**2 * np.sin(O1 - O2) + l1 * g * (m1 + m2) * np.sin(O1)
        e = -m2 * l1 * l2 * w1**2 * np.sin(O1 - O2) + l2 * m2 * g * np.sin(O2)
        return np.array([w1, w2, -b * ((b * d) / a - e) / (a * (y - b**2 / a)) - d / a, (b * d / a - e) / (y - b**2 / a)]) #retorna las derivadas de cada variable
```
-->

**(3)** Utilice el Método de Runge-Kutta para encontrar una solución para este sistema. Grafique (a) la solución de ambos péndulos en el tiempo, (b) el espacio de fase, (c) la energía total en el tiempo. 

<!--
```python
    #Posiciones y velocidades en coordenadas cartesianas
    x1 = l1*np.sin(X[:,0])
    x2 = x1 + l2*np.sin(X[:,1])

    y1 = l1*np.cos(X[:,0])
    y2 = y1 + l2*np.cos(X[:,1])

    v1_x = l1*X[:,2]*np.cos(X[:,0])
    v2_x = v1_x + l2*X[:,3]*np.cos(X[:,1])

    v1_y = -l1*X[:,2]*np.sin(X[:,0])
    v2_y = v1_y -l2*X[:,3]*np.sin(X[:,1])

    #Energias Cineticas:
    K1 = 0.5*m1*l1**2*X[:,2]**2
    K2 = 0.5*m2*(v2_x**2 + v2_y**2)

    #Energia Potencial: 
    U = m1*g*y1 + m2*g*y2 

    E = K1 + K2 + U 
```
-->
**(4)** Comente como (b) y (c) indican si es que se conserva la energía o no.

**(5)** Repita el procedimiento (3) con (a) el Método de la Rana y (b) un Método de Runge-Kutta a mayor orden.

<!--
![alt text](<img/pendulo-doble-todo.png>)

![alt text] (<img/solucion pendulo doble.png>)

![alt text](<img/energias_p2.png>)
-->


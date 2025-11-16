## **Ayudantía 14/11** -  *Física computacional II*
#### **Actividad :Erorr de método de Newton-Raphson en ceros múltiples (a mano)**
Encuentre el orden de error del método de Newton-Raphson cuado se encuentra un cero múltiple; para un cero múltiple se cumple que; 
$$ f(x^*) = f'(x^*) = 0 $$
Usando el algoritmo del método de la bisección, encuentre el error absoluto del método. Recuerde como funciona el método y lo que hace en cada iteración para derivar el error. El método de Newton-Raphson para encontrar ceros funciona de la siguiente manera;
$$ x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}  $$
Y como ya vimos, si $x^*$ corresponde a un cero múltiple, entonces tanto la función como la derivada se anulan. Para encontrar el error hagamos serie de Taylor alrededor de $x_n=x^* + \epsilon_n$, primero para la función
$$ f(x^* + \epsilon_n) = f(x^*)  + f'(x^*)\epsilon_n +  \frac{1}{2} f''(x^*)\epsilon_n^2 + \frac{1}{3!}f'''(\xi)\epsilon_n^3 $$
Luego hacemos lo mismo pero con la derivada de la función f;
$$  f'(x^*+\epsilon_n) = f'(x^*) + f''(x^*)\epsilon_n + \frac{1}{2}f'''(\eta)\epsilon_n^2 $$
Luego, reemplazamos esto en la relación de recursisivad que da origen al método de Newton-Raphson;
$$ \epsilon_{n+1} = \epsilon_n - \frac{\frac{1}{2}f''(x^*)\epsilon_n + \frac{1}{3!}f'''(\xi)\epsilon_n^2}{f''(x^*) + \frac{1}{2}f'''(\eta)\epsilon}  $$
Ahora, como tenemos términos muy pequeños, podemos usar la expansión en series (para x<<1);
$$  \frac{1}{1+x} \sim 1 - x $$
Con lo cual, podemos expresar la fracción dentro de la relación de recursión como;
$$ \epsilon_{n+1} = \epsilon_n  \left[ 1 - \frac{(\frac{1}{2}f''(x^*) + \frac{1}{3!}f'''(\xi)\epsilon_n)}{f''(x^*)} \left( 1 - \frac{1}{2} \frac{f'''(\eta)}{f''(x^*)}\epsilon_n \right) \right]  $$
Lo que, como $\epsilon_n<<1$ es un número muy pequeño, entonces podemos tomar solo los términos lineales;
$$  \epsilon_{n+1} = \frac{1}{2}\epsilon_n + O(\epsilon_n^2) $$
Así, hemos demostrado que el error en el método de Newton-Raphson, cuando los ceros son múltiples, es lineal, que es mucho peor con lo que pasa cuando los ceros no son múltiples, en donde el error es del tipo;
$$ \epsilon_{n+1} = k\epsilon_n^2 $$
#### **Actividad: Fractal de Newton**



El fractal de Newton es una frontera en el plano complejo delimitada mediante el método de Newton aplicado a un polinomio fijo $p(Z) \in ℂ[Z]$. Es el conjunto de Julia  de la función meromorfa $\frac{p(z)}{p´(z)}$ que es el **conjunto de puntos donde la interacción con el método de Newton forma fronteras fractales entre las raíces. Para estudiarlos, partimos definiendo numéricamente nuestro método. 

```python
def Newton(f,h,x0,eps=1e-4): 
    n=0
    while np.abs(f(x0)/h(x0))> eps and np.abs(f(x0))>eps and n<30: 
        x0 = x0 - f(x0)/h(x0)  
        n= n+1
    return x0
```

Sabemos que para utilizarlo, debemos definir a una función y su derivada. Definamos una función polinomial: 

```python
l = lambda x: x**3 -1
dl = lambda x: 3*x**2
```
Notar que también pueden utilizar métodos numéricos para definir la derivada de la función $l$. En este caso lo haremos analiticamente y utilizaremos una función polinomial de grado 3: $l(x) = x^3 -1$.

Ahora, grafiquemos c:

Definamos nuestro espacio en el plano complejo $\mathbb{C}$ 


```python
re, im = np.mgrid[-10:10:300j, -10:10:300j] #ahi el j dice que tenga 10 elementos

x0 = re + 1j*im
```

Grafiquemos el fractal. Para hacerlo hay que tomar ciertas consideraciones. utilizamos "enumerate" ya que necesitamos guardar no solo el valor de cada elemento de x, sino que también necesitamos saber su posición.  Por lo que el indice nos dirá la posición y el valor nos indicará el valor.

```python
x = x0.copy()
for i, RE in enumerate(re): #le da un indice a cada uno de los elementos (indice, valor)
    for j,IM in enumerate(im): 
        x[i,j] = Newton(l,dl, x0=x0[i,j], eps=1e-4)


plt.scatter(x0.real, x0.imag)
plt.pcolor(x0.real, x0.imag, np.angle(x) )
# plt.scatter(x.real, x.imag, color='red')
plt.colorbar()
plt.show()
```

Obtenemos: 

![alt text](Figure_1-1.png)

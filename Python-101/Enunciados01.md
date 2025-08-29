### **Ejercicio 1, Algoritmo de Shor**

El Algoritmo de Shor es un algoritmo utilizado en computación cuántica para factorizar números enteros de gran tamaño como el producto de dos enteros menores $A = B*C$. Escriba un código en python extrapolando este Algoritmo para numeros entre 1 y 60. 

Tal que al ingresar un número $A \in  [1, 60]$, el código imprima la factorización de estos dos números $(B*C)$. 

**Pista: Utilice el Teorema Fundamental de la Aritmética para desarrollar la factorización.*

### **Ejercicio 2, Fórmula de Willan**

La fórmula de Willans permite calcular el enésimo número primo sin necesidad de generar todos los primos anteriores mediante un proceso iterativo clásico. Esta fórmula se expresa como:

$$
\begin{equation}
p_n = 1 + \Sigma_{i=1}^{2^n} \left[\frac{n}{\Sigma_{j=1}^i F(j)}  \right]^{1/n}
\end{equation}
$$

con: 

$$
\begin{align*}
F(j) &= \cos^2[\pi \frac{(j-1)!+1}{j}]\\
&= 

\begin{cases}
1,  \quad \text{para j=1 o j primo}\\
0, \quad \text{otro}
\end{cases}
\end{align*}
$$

Calcule los números primos n-ésimo usando esta fórmula utilizando un código en Python.

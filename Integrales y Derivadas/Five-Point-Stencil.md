## **Ayudantía 4** - *Física computacional II*

#### **Actividad: Derivación del Five point stencil**
La plantilla de cinco puntos (five-point stencil) proporciona una aproximación numérica para la derivada de una función real, dada por la expresión:
 $$f^{(1)}(x)\approx\frac{f(x-2h)-8f(x-h)+8f(x+h)-f(x+2h)}{12h}$$
#### **Tarea 1**
Su objetivo es derivar dicha regla de derivación, valga la redundancia, mediante la manipulación (a mano) de la función usando métodos vistos en clase.
(Opcional)
Obtener el orden de error de truncamiento que possee dicha regla mediante el teorema de valor medio.
### **Tarea 2**
Luego de entender el cómo se obtiene la plantilla de 5 puntos o "five point stencil" desarolle una función en Python que aplique dicha regla de derivación a una funcion cualquiera f(x)
## **Tarea 3**
Aplique, finalmente, la regla de derivación a la función
$$g(x) = \frac{1-\cos{x}}{x} $$
alrededor de x=0 y compare el resultado numérico con el analítico.


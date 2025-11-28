import numpy as np
import matplotlib.pyplot as plt

	 
###Lagrange Interpolation 
# considerando los datos como (x[j], y[j]). con n+1 datapoints:

n = len(x)-1

def f(o):
  sum = 0

  for i in range(n+1):
    prod = y[i]

    for j in range(n+1):
        if i!= j:
            prod=prod*(o-x[j])/(x[i]-x[j])

    sum = sum + prod

  return sum


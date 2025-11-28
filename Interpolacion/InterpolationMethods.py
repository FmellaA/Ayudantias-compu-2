import numpy as np
import matplotlib.pyplot as plt

	 
###Lagrange Interpolation 
# considerando los datos como (x[j], y[j]). con n+1 datapoints:



def Lagrangian(o,x,y):
  n = len(x)-1
  sum = 0

  for i in range(n+1):
    prod = y[i]

    for j in range(n+1):
        if i!= j:
            prod=prod*(o-x[j])/(x[i]-x[j])

    sum = sum + prod

  return sum


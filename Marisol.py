import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#Constante
#x=2
#Ap=0.8
#Variables
#Hacer 2 casos, uno para Beta<<1 y otro para Beta>>1
#En este caso Beta_IIp es menor que 1 (no me acuerdo si era simplemente un numero menor que 1 o todos los numeros menores que 1)
def S(Ap, x):
    a = 1 
    O =1
    d=10
    n=0.5
    B=0.1
    return (np.sqrt(np.pi)/(2*(a)))* O *(Ap*(1-x)-x)*np.exp(-(((1-x)**2)/(B**2))*(1+(B/2)*(((Ap*(1-x))-x)/((1-x)**3)))/(((1+d)/(1-x))+((4*n)/(1-4*x))))*((x**2)*(((1+d)/(1-x))+((4*n)/(1-(4*x)))))**(-1)

Ap_values = np.linspace(0.1, 3, 25)
x_values = np.linspace(0.1, 0.99, 25)

S_values = S(Ap_values, x_values)

plt.plot(x_values, S_values)
plt.xlabel("x (0,1 - 0,99)")
plt.ylabel("S")
plt.title("Grafico de x vs S")

#figure, axis = plt.subplots(1, 2)

#axis[0].plot(x_values, S_values)
#axis[0].set_title("x vs S")

#axis[1].plot(Ap_values, S_values)
#axis[1].set_title("Ap vs S")

plt.show()
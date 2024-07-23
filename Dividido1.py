import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#Constante
#x=2
#Ap=0.8
#Variables
#Hacer 2 casos, uno para Beta<<1 y otro para Beta>>1
#En este caso Beta_IIp es menor que 1 (no me acuerdo si era simplemente un numero menor que 1 o 
d=10
n=0.5
B=0.1
x = np.linspace(0.1, 0.99)

S=((x**(2))*(((1+d)/(1-x))+((4*n)/(1-4*x)))/1)

plt.plot(x, S)
plt.xlabel("x (0,1 - 0,99)")
plt.ylabel("S")
plt.title("Grafico de x vs S")

#figure, axis = plt.subplots(1, 2)

#axis[0].plot(x_values, S_values)
#axis[0].set_title("x vs S")

#axis[1].plot(Ap_values, S_values)
#axis[1].set_title("Ap vs S")

plt.show()
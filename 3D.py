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

Ap, x = np.meshgrid(Ap_values, x_values)

S_values = S(Ap, x)

# Graficar
fig = plt.figure(figsize=(24, 18))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
#ax.scatter(Tp, Tr, fk_values, cmap='viridis')
ax.plot_surface(Ap, x, S_values, cmap='cool', alpha=1)


#ax.contour3D(Tp, Tr, fk_values,c=fk_values)
# Configuración del gráfico
ax.set_title('Gráfico 3D de S')
ax.set_xlabel('Ap')
ax.set_ylabel('x')
ax.set_zlabel('S')
#ax.contourf(Ap, x, S(Ap, x), zdir='z', offset=-0.05, cmap='coolwarm')
ax.contourf(Ap, x, S(Ap, x), zdir='x', offset=-1, cmap='coolwarm')
ax.contourf(Ap, x, S(Ap, x), zdir='y', offset=1, cmap='coolwarm')

#ax.set(xlim=(-200,200), ylim=(-200,200), zlim=(0,10), xlabel='X', ylabel='Y', zlabel='Z')

plt.show()
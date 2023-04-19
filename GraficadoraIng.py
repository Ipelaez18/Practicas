import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
from tkinter import simpledialog

ws = Tk()
# Mostramos la lista de funciones y el usuario elige una por medio de un cuadro
ws.title("Elegir la función")
funciones = Label(ws, text="Funciones:\n\n1.Seno\n\n2.Coseno\n\n3.Tangente\n\n4.Exponencial\n\n5.Logaritmica")
funciones.pack(pady=20)

funcion = int(simpledialog.askstring("Elige", "Elige una función: ",
                                    parent=ws))

ws.destroy()
ws.mainloop()

# Definimos la función a graficar
def f(x):
    if funcion == 1:
        return np.sin(x)
    if funcion == 2:
        return np.cos(x)
    if funcion == 3:
        return np.tan(x)
    if funcion == 4:
        return np.exp(x)
    if funcion == 5:
        return np.log(x)

# Generamos los valores para el eje x
x = np.linspace(-np.pi, np.pi, 100)

# Evaluamos la función en los valores de x
y = f(x)

# Creamos la figura y los ejes
fig, ax = plt.subplots()

# Graficamos la función
ax.plot(x, y)
if funcion == 3:
    plt.ylim(-10,10)

# Configuramos los ejes
ax.set(xlabel='x', ylabel='f(x)', title='Gráfico de la función')
ax.grid()

# Mostramos el gráfico
plt.show()
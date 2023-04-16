from tkinter import *
from tkinter import simpledialog

ws = Tk()
ws.title("Elegir la función")

funciones= Label(ws, text="Funciones:\n\n1.Seno\n\n2.Coseno\n\n3.Tangente\n\n4.Exponencial\n\n5.Logaritmica")
funciones.pack(pady=20)

answer1 = simpledialog.askstring("Elige", "Elige una función",
                                parent=ws)

ws.destroy()
ws.mainloop()
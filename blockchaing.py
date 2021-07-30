import tkinter
from tkinter import messagebox
from tkinter import *


def Raices():
    a = int(pantalla.get())
    b = int(pantalla2.get())
    c = int(pantalla3.get())

    d = b**2-4*a*c
    x1 = (-b+d**0.5)/(2*a)
    x2 = (-b-d**0.5)/(2*a)

    messagebox.showinfo(message=('Las raices son ', x1,
                        ' y ', x2), title="Mensaje")


colorventana = '#3F403E'

# INICIAR NUESTRA VENTANA
ventana = Tk()

# PONER NOMBRE A NUUESTRA VENTANA
ventana.title("Cuadrados")

# DEFINIR EL TAMAÃ‘O DE NUESTRA VENTANA
ventana.geometry("300x300")

# EVITAR QUE LOS USUARIOS CAMBIEN DE TAMAÃ‘O A NUESTRA VENTANA
ventana.resizable(width=False, height=False)

# DEFINIR EL COLOR DE NUESTRA VENTANA
ventana.config(bg=colorventana)

label = Label(ventana, text="Ingrese el valor de a")
label.config(font=("Consolas", 14), justify=RIGHT)
label.place(x=0, y=0)
pantalla = Entry(ventana)
pantalla.pack()
pantalla.place(width=50, height=40)
pantalla.config(font=("Consolas", 14), justify=RIGHT)
pantalla.place(x=0, y=30)


label2 = Label(ventana, text="Ingrese el valor de b")
label2.config(font=("Consolas", 14), justify=RIGHT)
label2.place(x=0, y=80)
pantalla2 = Entry(ventana)
pantalla2.pack()
pantalla2.place(width=50, height=40)
pantalla2.config(font=("Consolas", 14), justify=RIGHT)
pantalla2.place(x=0, y=110)

label3 = Label(ventana, text="Ingrese el valor de c")
label3.config(font=("Consolas", 14), justify=RIGHT)
label3.place(x=0, y=160)
pantalla3 = Entry(ventana)
pantalla3.pack()
pantalla3.place(width=50, height=40)
pantalla3.config(font=("Consolas", 14), justify=RIGHT)
pantalla3.place(x=0, y=190)


BotonCalcular = Button(ventana, text="Calcular Las raices",
                       font=("Consolas", 14), command=Raices)
BotonCalcular.place(x=40, y=240)

mainloop()

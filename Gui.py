
import tkinter as tk
from tkinter import Image, ttk
from tkinter import *
from tkinter import font


# funcion para el cifrado y descifrado
def cifrado():
    mensaje1 = texto1.get(1.0, "end-1c").upper()
    key1 = int(w.get())
    opcion1 = "c"
# opcion.get()
    resultado = ""
    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for simabolo in mensaje1:
        if simbolo in letras:
            posicion = letras.find(simbolo)
            if opcion1 == "c":
                posicion = posicion + key1
            elif opcion1 == "d":
                posicion = posicion - key1

            if posicion >= len(letras):
                posicion -= len(letras)
            elif posicion < 0:
                posicion += len(letras)

            resultado += letras[posicion]
        else:
            resultado += simbolo
    salida = StringVar(value=resultado)
    print(salida)
    txtResultado = Entry(frame1, textvariable=salida,
                         width=60).place(x=110, y=180)
    # texto3.insert(0,salida)
    # salida
    #print("SALIDAAAA "+salida)
    # texto3=Entry(frame1,text=salida).place(x=10,y=300,width=350,height=100)
    # texto3.config(width=35,height=5)

    # texto3.place(x=10,y=300)
    # txtResultado=Entry(frame1,textvariable=salida,width=60).place(x=110,y=180)


def decifrado():
    mensaje1 = texto2.get(1.0, "end-1c").upper()
    print("llego asta AQUI2"+mensaje1)
    key1 = int(w.get())
    opcion1 = "d"
# opcion.get()
    resultado = ""
    letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for simbolo in mensaje1:
        if simbolo in letras:
            posicion = letras.find(simbolo)
            if opcion1 == "c":
                posicion = posicion + key1
            elif opcion1 == "d":
                posicion = posicion - key1

            if posicion >= len(letras):
                posicion -= len(letras)
            elif posicion < 0:
                posicion += len(letras)

            resultado += letras[posicion]
        else:
            resultado += simbolo
    salida = StringVar(value=resultado)

    # salida
    #print("SALIDAAAA "+salida)
    texto4 = Entry(frame1, text=salida).place(
        x=400, y=300, width=350, height=100)
    # texto3.config(width=35,height=5,padx=15,pady=15)
    # texto3.place(x=10,y=300)
    # txtResultado=Entry(frame1,textvariable=salida,width=60).place(x=110,y=180)


root = tk.Tk()
root.title("Interfaz tulio")
root.geometry('800x700')
#imagenlogo=ImageTk.PhotoImage(Image.open(r"C:\Users\Lisonds\Desktop\seguridad lab\python\INTERFACE\logo1.jpg"))
# label=Label(root,image=imagenlogo)
# abel.place(relwidth=1,y=0)

label = Label(root, text="INGENIERIA DE SISTEMAS")
label.place(x=200, y=100)
label.pack()

# cuadro madre
cuadroMadre = ttk.Notebook(root)
cuadroMadre.pack(pady=110, expand=True)

frame1 = ttk.Frame(cuadroMadre, width=900, height=600)
frame2 = ttk.Frame(cuadroMadre, width=900, height=600)


frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)


# agregando los frames a cuadro madre
cuadroMadre.add(frame1, text='MINAR CONTRATO')
cuadroMadre.add(frame2, text='CONTRATOS INTELIGENTES')


# cifrado por sustitucion
#abel=Label(frame1,text="HASH ")
label.place(x=100, y=5)

labelContratoAnterior = Label(frame1, text="INGRESE HASH DEL CONTRATO ANTERIOR",
                              font='Helvetica 12 bold')
labelContratoAnterior.place(x=230, y=5)

mensaje = StringVar()
txtMensaje = Entry(frame1, textvariable=mensaje, width=50)
txtMensaje.place(x=230, y=40)

mensaje = StringVar()

botonContrato = ttk.Button(frame1, text="Existe contrato?", command=cifrado)
botonContrato.place(x=540, y=40)


boton3 = ttk.Button(frame1, text="Minar contrato", command=cifrado)
boton3.place(x=320, y=170)

boton4 = ttk.Button(frame1, text="Terminar contrato", command=cifrado)
boton4.place(x=300, y=300)


label = Label(frame1, text="Ingrese el hash")
label.place(x=100, y=40)


label2 = Label(frame1, text="INGRESE NUEVO HASH AL CONTRATO",
               font='Helvetica 12 bold')
label2.place(x=230, y=100)

label3 = Label(frame1, text="Ingrese nuevo Hash")
label3.place(x=100, y=130)

txtMensaje3 = Entry(frame1, textvariable=mensaje, width=50)
txtMensaje3.place(x=230, y=130)
#w=Spinbox(frame1, values=("1","2","3","4","5","6","7","8","9","10"))
# w.place(x=310,y=250)
# w.config(font=("curier,15"))

# texto2=Text(frame1)
# texto2.pack()
# texto2.config(width=35,height=5,padx=15,pady=15,font=("curier,15"))
# texto2.place(x=400,y=25)

# boton=ttk.Button(frame1,text="Decifrar",command=decifrado)
# boton.place(x=520,y=180)

#label=Label(frame1,text="Key ")
# label.place(x=250,y=250)

# texto3=Entry(frame1).place(x=10,y=300,width=350,height=100)
# texto3.config(width=35,height=5)
# texto3.place(x=10,y=300)

# texto4=Text(frame1)
# texto4.config(width=35,height=5,padx=15,pady=15,font=("curier,15"))
# texto4.place(x=400,y=300)


root.mainloop()

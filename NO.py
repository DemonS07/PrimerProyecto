import tkinter as tk
from tkinter import *

ventana = tk.Tk()
ventana.title("ESTO TE PERTENECE PRECIOSO")
ventana.iconbitmap("P1.ico")
ventana.geometry("530x530")
ventana.resizable(False, False)
ventana.config(bg="white")

def mostrar1():
    global mensaje
    mensaje = tk.Label(ventana, text="❤AWWW TE QUIERO MUCHO❤", font=("Arial", 12))  #Definir mensaje como global
    mensaje.place(x=145, y=120)

    #Redimensionar la imagen a la mitad
    foto = tk.PhotoImage(file="F7.png").subsample(3)
    label_foto = tk.Label(ventana, image=foto)
    label_foto.image = foto
    label_foto.place(x=82, y=150)  #Mover la imagen a la nueva posición

#Tamaño inicial de los botones
tamanio_botones = 12

#Crear botón 1
boton1 = tk.Button(ventana, text="CLARO QUE LO ERES", command=mostrar1, font=("Arial", 12))
boton1.place(x=175, y=50)  # Posicionar el botón 1

def mostrar2():
    global mensaje
    mensaje = tk.Label(ventana, text="❤CAMBIA DE OPINION YAAA.❤", font=("Arial", 12))
    mensaje.place(x=145, y=120)

    foto = tk.PhotoImage(file="F6.png").subsample(2)
    label_foto = tk.Label(ventana, image=foto)
    label_foto.image = foto
    label_foto.place(x=145, y=160)

#Crear botón 2
boton2 = tk.Button(ventana, text="NO LO ERES", command=mostrar2, font=("Arial", tamanio_botones))
boton2.place(x=210, y=83)  #Posicionar el botón 2

pregunta_boton1 = tk.Label(ventana, text="🐝¿SOY LINDA PARA TI?🐝", font=("Arial", 12))
pregunta_boton1.place(x=164, y=10)  #Posicionar la pregunta arriba del botón 1

ventana.mainloop()
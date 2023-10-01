import PIL
from PIL import ImageTk
import math
import graflib as gl
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

# Crear Tkinter
app = tk.Tk()

# Configuracion de la interfaz
app.geometry('800x400')
app.title('Sombreado de un Poligono')
app.title('Selecciona un color')
app.geometry('300x150')
# Tamaño de la imagen
ancho_var = tk.StringVar()
alto_var = tk.StringVar()


# Coordenadas de los vértices del polígono
vertices = [(-200, -200), (-50, 80), (170, 170), (50,-80)]
color = (0, 0, 0)

# Creacion Frames
frame1 = tk.Frame(app, bg='white')
frame2 = tk.Frame(app, bg='#F2545B')

#color definido por el usuario 

# Funcion button
def saludar():
    tk.Label(frame2, fg='white', bg='#F2545B').pack()
    
    ancho = int(ancho_var.get())
    alto = int(alto_var.get())

    #Definir un lienzo
    canvas = PIL.Image.new('RGB', (ancho, alto), (255,255,255))
    
    gl.drawWireframePolygon(vertices, color, canvas)

    tkpic = ImageTk.PhotoImage(canvas)
    label = tk.Label(frame2, image=tkpic)
    label.image = tkpic  # Save reference to image
    label.pack()

    app.geometry(f"{ancho+300}x{alto+100}")
    print('Hola')


def pintar():
    tk.Label (frame2, fg='white', bg='#F2545B').pack()

    ancho = int(ancho_var.get())
    alto = int(alto_var.get())
    
    canvas = PIL.Image.new('RGB', (ancho,alto),(255,255,255))

    color=askcolor(title="Selecciona un color")  

    gl.drawFilledPolygon(vertices, color, canvas)

    tkpic = ImageTk.PhotoImage(canvas)
    label = tk.Label(frame2,image=tkpic)
    label.image=tkpic
    label.pack()
    app.geometry(f"{ancho+300}x{alto+100}")
    print('Disque estamos pintando')

def degradar():
    tk.Label(frame2,fg='white', bg='#F2545B').pack()

    ancho = int(ancho_var.get())
    alto = int(alto_var.get())

    canvas = PIL.Image.new('RGB', (ancho,alto),(255,255,255))

    gl.drawGradientPolygon(vertices, color, canvas, centroid=None)

    tkpic = ImageTk.PhotoImage(canvas)
    label = tk.Label(frame2,image=tkpic)
    label.image=tkpic
    label.pack()
    app.geometry(f"{ancho+300}x{alto+100}")
    print('disque estamos degradando')
    


# Creacion de elementos
tk.Label(
    frame1,
    text='Tamaño del Canva',
    fg='black',
    bg='white',
    font=('Arial', 17)
).pack(pady=10)

tk.Label(
    frame1,
    text='Ingresa el ancho del canva',
    fg='black',
    bg='white',
).pack(pady=5)

entryAncho = Entry(
    frame1,
    fg='black',
    bg='#d3d3d3',
    textvariable=ancho_var,
).pack(pady=5)

tk.Label(
    frame1,
    text='Ingresa el alto del canva',
    fg='black',
    bg='white',
).pack(pady=5)

entryAlto = Entry(
    frame1,
    fg='black',
    bg='#d3d3d3',
    textvariable=alto_var,
).pack(pady=10)


tk.Button(
    frame1,
    text='Crear Canva',
    font=('Courier', 10),
    bg='#F2545B',
    fg='white',
    command=saludar,
).pack()

tk.Label(
    frame2,
    text='Canva',
    fg='white',
    bg='#F2545B',
    font=('Arial', 17)
).pack(pady=10)

tk.Button(
    frame1,
    text='Pintar Poligno',
    font=('Courier',10),
    bg='#F2545B',
    fg='white',
    command=pintar,
).pack(expand=True)


frame1.pack(side=LEFT, expand=True, fill=BOTH)
frame2.pack(side=LEFT, expand=True, fill=BOTH)
app.mainloop()
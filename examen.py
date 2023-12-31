import PIL
from PIL import ImageTk
import math
from tkinter import colorchooser
import graflib as gl
import numpy as np
import tkinter as tk
from tkinter import *

# Crear una ventana de Tkinter
app = tk.Tk()

# Configuración de la interfaz
app.geometry('1000x500')
app.title('Sombreado de un Poligono')

# Variables para el tamaño del lienzo
ancho_var = tk.StringVar()
alto_var = tk.StringVar()

# Variables de condicion
canva_creado = False
poligono_creado = False

# Coordenadas de los vértices del polígono
vertices = []
#vertices = [(-200, -200),(175, 25), (25, 175), (-100, 100), (-150, 50)]

# Creación de Frames
frame1 = tk.Frame(app, bg='white')
frame2 = tk.Frame(app, bg='#006d77')

# Función del botón "Crear Canva"
def dibujarFigura():

    global canva_creado

    if not canva_creado:
        tk.Label(frame2, fg='white', bg='#006d77').pack()

        ancho = int(ancho_var.get())
        alto = int(alto_var.get())

        # Definir un lienzo
        canvas = PIL.Image.new('RGB', (ancho, alto), (255, 255, 255))

        tkpic = ImageTk.PhotoImage(canvas)
        label = tk.Label(frame2, image=tkpic)
        label.image = tkpic  # Guardar una referencia a la imagen para evitar que se elimine
        label.pack()
        app.geometry(f"{ancho + 800}x{alto + 500}")

        def callback(event):
                color = (0, 0, 0)
                gl.pointAround(canvas, event.x, event.y, (ancho, alto), color)
                tkpic = ImageTk.PhotoImage(canvas)
                label.config(image=tkpic)
                label.image = tkpic  # Save reference to image
                vertices.append((event.x, event.y))

        label.bind("<Button-1>", callback)

        def crearPoligono():
            
            global poligono_creado
            
            if not poligono_creado:
                relleno = colorchooser.askcolor(title="Choose color")
                color = tuple(int(c) for c in relleno[0])
                print(color)

                gl.drawPolygon(gl.matrixToCartessian(vertices, ancho, alto), (0, 0, 0), canvas)
                gl.drawGradientPolygon(gl.matrixToCartessian(vertices, ancho, alto), color, canvas)

                tkpic = ImageTk.PhotoImage(canvas)
                label.config(image=tkpic)
                label.image = tkpic  # Save reference to image
                label.pack()

                def callback(event):
                    centroid = (event.x, event.y)
                    gl.drawGradientPolygon(gl.matrixToCartessian(vertices, ancho, alto), color, canvas, centroid)
                    tkpic = ImageTk.PhotoImage(canvas)
                    label.config(image=tkpic)
                    label.image = tkpic  # Save reference to image

                label.bind("<Button-1>", callback)
                poligono_creado = True
    
        tk.Label(
            frame1,
            text='Ahora puedes dibujar los puntos de tu poligono en el canva!',
            fg='black',
            bg='white',
        ).pack(pady=10)
        
        tk.Button(
            frame1,
            text='Crear Poligono',
            font=('Courier', 10),
            bg='#006d77',
            fg='white',
            command=crearPoligono,
        ).pack()

        canva_creado = True

    
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
    bg='#006d77',
    fg='white',
    command=dibujarFigura,
).pack(pady=10)

tk.Label(
    frame2,
    text='Canva',
    fg='white',
    bg='#006d77',
    font=('Arial', 17)
).pack(pady=10)


frame1.pack(side=LEFT, expand=True, fill=BOTH)
frame2.pack(side=LEFT, expand=True, fill=BOTH)
app.mainloop()
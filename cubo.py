from PIL import Image
import graflib as gl

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
purple = (128, 0, 128)
cyan = (0, 255, 255)

vertices = [
    [4, 4, 4], # Punto A
    [3, 4, 4], # Punto B
    [3, 3, 4], # Punto C
    [4, 3, 4], # Punto D
    [4, 4, 3], # Punto E
    [3, 4, 3], # Punto F
    [3, 3, 3], # Punto G
    [4, 3, 3]  # Punto H
]

triangulos = [
    [0, 1, 2, red],
    [0, 2, 3, red],
    [4, 0, 3, green],
    [4, 3, 7, green],
    [5, 4, 7, blue],
    [5, 7, 6, blue],
    [1, 5, 6, yellow],
    [1, 6, 2, yellow],
    [4, 5, 1, purple],
    [4, 1, 0, purple],
    [2, 6, 7, cyan],
    [2, 7, 3, cyan]
]

def renderObject(vertices, triangulos, canvas):
    projected = []
    for V in vertices:
        projected.append(gl.projectVertex(V))

    for T in triangulos:
        renderTriangle(T, projected, canvas)

def renderTriangle(triangulo, projected, canvas):   
    print(projected)
    gl.drawWireframeTriangle(
        projected[triangulo[0]],
        projected[triangulo[1]],
        projected[triangulo[2]],
        triangulo[3], canvas
    )

# Tamaño de la imagen
width = 501
height = 501

# Definir un lienzo
canvas = Image.new('RGB', (width, height), (255, 255, 255))

# Color de la linea
color = (0,0,0)

# Dibujar el contorno
renderObject(vertices, triangulos, canvas)

canvas.show()
from PIL import Image, ImageDraw
import math
import graflib as gl

def drawWireframePolygon(vertices, color, canvas):
    num_vertices = len(vertices)
    for i in range(num_vertices):
        P0 = vertices[i]
        P1 = vertices[(i + 1) % num_vertices]
        gl.drawLine(P0, P1, color, canvas)

def drawFilledPolygon(vertices, color, canvas):
    # Encontrar los límites del polígono en el plano cartesiano

    # Función lambda que toma un vertice y devuelve la coordenada "x" de ese vértice
    min_x = min(vertices, key=lambda vertex: vertex[0])[0]
    max_x = max(vertices, key=lambda vertex: vertex[0])[0]

    # Función lambda que toma un vertice y devuelve la coordenada "y" de ese vértice
    min_y = min(vertices, key=lambda vertex: vertex[1])[1]
    max_y = max(vertices, key=lambda vertex: vertex[1])[1]

    # Iterar a través de todos los píxeles dentro de los límites
    for y in range(min_y, max_y + 1):
        intersections = []
        for i in range(len(vertices)):
            P0 = vertices[i]
            P1 = vertices[(i + 1) % len(vertices)]
            if P0[1] <= y < P1[1] or P1[1] <= y < P0[1]:
                x = round(P0[0] + (P1[0] - P0[0]) * (y - P0[1]) / (P1[1] - P0[1]))
                intersections.append(x)

        # Ordenar las intersecciones por coordenada x
        intersections.sort()

        # Rellenar los píxeles entre las intersecciones de forma horizontal
        for i in range(0, len(intersections), 2):
            for x in range(intersections[i], intersections[i + 1] + 1):
                gl.drawPoint(x, y, color, canvas)

#Tamaño de la imagen
width = 501
height = 501

#Definir un lienzo
canvas = Image.new('RGB', (width,height), (255,255,255))

# Coordenadas de los vértices del polígono
vertices = [(-200, -200), (-50, 80), (170, 170), (50,-80)]

color = (199, 125, 255)

# Dibujar el polígono
drawWireframePolygon(vertices, color, canvas)

# Rellenar polígono
drawFilledPolygon(vertices, color, canvas)

canvas.show()

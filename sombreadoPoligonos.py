from PIL import Image
import math
import graflib as gl
import numpy as np

# Tamaño de la imagen
width = 501
height = 501

# Definir un lienzo
canvas = Image.new('RGB', (width, height), (255, 255, 255))

def drawShadedPolygon(P0, P1, P2, color, canvas):
    # Sort the points so that y0 <= y1 <= y2
    h0 = 1
    h1 = 0
    h2 = 0
    c = puntoc
    if P1[1] < P0[1]:
        P1, P0 = gl.swap(P1, P0)
    if P2[1] < P0[1]:
        P2, P0 = gl.swap(P2, P0)
    if P2[1] < P1[1]:
        P2, P1 = gl.swap(P2, P1)

    if c==P0:
        h1 = 0
        h0 = 1
        h2 = 0
    if c==P1:
        h1 = 1
        h0 = 0
        h2 = 0
    if c==P2:
        h1 = 0
        h0 = 0
        h2 = 1

    x0 = P0[0]
    y0 = P0[1]
    x1 = P1[0]
    y1 = P1[1]
    x2 = P2[0]
    y2 = P2[1]

    # Compute the x coordinates and h values of the triangle edges
    x01 = gl.interpolate(y0, x0, y1, x1)
    h01 = gl.interpolate(y0, h0, y1, h1)

    x12 = gl.interpolate(y1, x1, y2, x2)
    h12 = gl.interpolate(y1, h1, y2, h2)

    x02 = gl.interpolate(y0, x0, y2, x2)
    h02 = gl.interpolate(y0, h0, y2, h2)

    # Concatenate the short sides
    x01.pop(-1)
    x012 = x01 + x12

    h01.pop(-1)
    h012 = h01 + h12

    # Determine which is left and which is right
    m = math.floor(len(x012) / 2)
    if x02[m] < x012[m]:
        x_left = x02
        h_left = h02

        x_right = x012
        h_right = h012
    else:
        x_left = x012
        h_left = h012

        x_right = x02
        h_right = h02

    # Draw the horizontal segments
    for y in range(y0, y2 - 1):
        xl = round(x_left[y - y0])
        hl = h_left[y - y0]

        xr = round(x_right[y - y0])
        hr = h_right[y - y0]

        h_segment = gl.interpolate(xl, hl, xr, hr)

        for x in range(xl, xr):
            sh_color0 = round(color[0] * h_segment[x - xl])
            sh_color1 = round(color[1] * h_segment[x - xl])
            sh_color2 = round(color[2] * h_segment[x - xl])
            shaded_color = (sh_color0, sh_color1, sh_color2)
            gl.drawPoint(int(x), int(y), shaded_color, canvas)

# Puntos iniciales
vertices = [(-200, -200),(175,25), (25,175), (-100,100), (-150,50)]
# color de la linea
color = (255, 100, 255)

print(vertices)
k = len(vertices)
cx = int(np.sum([punto[0] for punto in vertices])/k)
print (cx)
cy = int(np.sum([punto[1] for punto in vertices])/k)
print (cy)
i = 0
puntoc = (cx,cy)

while i < k-1:
    print(puntoc, vertices[i], vertices[i+1])
    #gl.drawWireframeTriangle(puntoc,puntos[i],puntos[i+1],color,canvas)
    drawShadedPolygon(puntoc, vertices[i], vertices[i + 1], color, canvas)
    i = i + 1
#gl.drawWireframeTriangle(puntoc,puntos[i],puntos[0],color, canvas)
drawShadedPolygon(puntoc, vertices[i], vertices[0], color, canvas)

canvas.show()
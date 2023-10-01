from PIL import Image,ImageDraw
import math
import graflib as gl

def drawWireframeTriangle (P0, P1, P2, color, canvas):
    gl.drawLine(P0, P1, color, canvas)
    gl.drawLine(P1, P2, color, canvas)
    gl.drawLine(P2, P0, color, canvas)

def drawFilledTriangle (P0, P1, P2, color, canvas):
    # Sort the points so that y0 <= y1 <= y2
    x0=P0[0]
    y0=P0[1]
    x1=P1[0]
    y1=P1[1]
    x2=P2[0]
    y2=P2[1]
    
    if y1 < y0:
        P1, P0 = gl.swap(P1,P0)
        x0=P0[0]
        y0=P0[1]
        x1=P1[0]
        y1=P1[1]
    if y2 < y0:
        P2, P0 = gl.swap(P2,P0)
        x2=P2[0]
        y2=P2[1]
        x0=P0[0]
        y0=P0[1]
    if y2 < y1:
        P2, P1 = gl.swap(P2,P1)
        x1=P1[0]
        y1=P1[1]
        x2=P2[0]
        y2=P2[1]
    
    # Compute the x coordinates of the triangle edges
    x01 = gl.interpolate(y0, x0, y1, x1)
    x12 = gl.interpolate(y1, x1, y2, x2)
    x02 = gl.interpolate(y0, x0, y2, x2)

    #Concatenate the short sides
    #remove_last(x01)
    x01.pop(-1)
    x012 = x01 + x12

    #Determine which is left and which is right
    m = math.floor(len(x012) / 2)
    if x02[m] < x012[m]:
        x_left = x02
        x_right = x012
    else:
        x_left = x012
        x_right = x02
    
    # Draw the horizontal segments
    for y in range(y0,y2+1):
        a=round(x_left[y - y0])
        b=round(x_right[y - y0])
        for x in range(a,b):
            gl.drawPoint(x,y,color,canvas)


#Tamaño de la imagen
width=501
height=501

#Definir un lienzo
canvas = Image.new('RGB', (width,height), (255,255,255))

#Puntos iniciales
P0=(-200,-200)
P1=(-50,80)
P2=(170,170)
#color de la linea
color=(0,0,0)

#dibujar el contorno
drawWireframeTriangle(P0,P1,P2,color,canvas)

#iluminar el polígono
color=(255,100,255)
drawFilledTriangle(P0,P1,P2,color,canvas) 

canvas.show()
from PIL import Image,ImageDraw
import numpy as np
import math
import graflib as gl

def projectVertex(v):
    d = 50
    vx = v[0]
    vy = v[1]
    vz = v[2]
    px = vx * d /vz
    py = vy * d / vz

    return viewportToCanvas(px, py)
 
P1 =( 0      , -r      , 1     ) * 1000
P6 =( 0      , r       , h1+h2+1) * 1000
P2 =( r*cos18, -r*sin18, 1     )* 1000
P7 =( -P2[0] , -P2[1]  , P6[2]+1 ) * 1000
P3 =( r*cos54, r*sin54 , 1     ) * 1000
P8 =( -P3[0] , -P3[1]  , P6[2]+1 ) * 1000
P4 =( -P3[0] ,  P3[1]  , 1     ) * 1000
P9 =( -P4[0] , -P4[1]  , P6[2]+1 ) * 1000
P5 =( -P2[0] ,  P2[1]  , 1     ) * 1000
P10=(  P2[0] , -P2[1]  , P6[2]+1 ) * 1000
P11=( 0      , -rr     , h1+1    ) * 1000
P12=( P1[0]  , -P11[1] , h2+1    ) * 1000
P13=(rr*cos54, -rr*sin54, h2+1    ) * 1000
P14=( -P13[0], -P13[1] , h1+1    ) * 1000
P15=(rr*cos18, -rr*sin18, h1+1    ) * 1000
P16=( -P15[0], -P15[1] , h2+1    ) * 1000
P17=( P15[0] , -P15[1] , h2+1    ) * 1000
P18=( -P17[0], -P17[1] , h1+1    ) * 1000
P19=( P10[0] , -P13[1] , h1+1    ) * 1000
P20=( -P19[0], -P19[1] , h2+1   )* 1000

def drawFace(face, color, canvas):
    gl.drawLine(projectVertex(face[-1]), projectVertex(face[0]), color, canvas)
    for i in range(0, len(cara1)-1):
        gl.drawLine(projectVertex(face[i]), projectVertex(face[i+1]), color, canvas)

# Definicion de caras
face1 = (P1, P2, P3, P4, P5)
face2 = (P1, P11, P20, P18, P5)
face3 = (P1, P11, P13, P15, P2)
face4 = (P2, P15, P17, P19, P3)
face5 = (P3, P19, P12, P14, P4)
face6 = (P4, P14, P16, P18, P5)
face7 = (P8, P9, P10, P6, P7)
face8 = (P8, P9, P13, P11, P20)
face9 = (P9, P13, P15, P17, P10)
face10 = (P10, P17, P19, P12, P6)
face11 = (P6, P12, P14, P16, P7)
face12 = (P7, P16, P18, P20, P8)

# Separarlas entre caras frontales y caras traseras
backside = (face1, face2, face3, face4, face5, face6)
frontside = (face7, face8, face9, face10, face11, face12)

# Trasar cada conjunto de caras con un color distintos
for face in backside:
    drawFace(face, BLUE, canvas)

for face in frontside:
    drawFace(face, RED, canvas)
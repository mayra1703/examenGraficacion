from PIL import Image
import numpy as np
import math
import graflib as gl

def scaleP3D(p,fs):
    P=np.array([p[0],p[1],p[2],1])
    #Matriz de escala
    mS=np.array([[fs,0,0,0],
                 [0,fs,0,0],
                 [0,0,fs,0],
                 [0,0,0,1]])
    return np.matmul(mS,P.transpose())
    
def rotateP3Dz(p,alpha):
    P=np.array([p[0],p[1],p[2],1])
    #Matriz de escala
    mR=np.array([[np.cos(alpha),-np.sin(alpha), 0, 0],
                 [np.sin(alpha), np.cos(alpha), 0, 0],
                 [            0,             0, 1, 0],
                 [            0,             0, 0, 1]])
    return np.matmul(mR,P.transpose())
    
def rotateP3Dx(p,alpha):
    P=np.array([p[0],p[1],p[2],1])
    #Matriz de escala
    mR=np.array([[ 1,             0,             0, 0],
                 [ 0, np.cos(alpha),-np.sin(alpha), 0],
                 [ 0, np.sin(alpha), np.cos(alpha), 0],
                 [ 0,             0,             0, 1]])
    return np.matmul(mR,P.transpose())

def rotateP3Dy(p,alpha):
    P=np.array([p[0],p[1],p[2],1])
    #Matriz de escala
    mR=np.array([[np.cos(alpha),             0,np.sin(alpha), 0],
                 [            0,             1,            0, 0],
                 [np.sin(alpha), np.cos(alpha),            0, 0],
                 [            0,             0,            0, 1]])
    return np.matmul(mR,P.transpose())
    
def translateP3D(p,pt):
    P=np.array([p[0],p[1],p[2],1])
    #Matriz de escala
    mT=np.array([[1,0,0,pt[0]],
                 [0,1,0,pt[1]],
                 [0,0,1,pt[2]],
                 [0,0,0,    1]])
    return np.matmul(mT,P.transpose())


class Cubo():
    """Modela un cubo genérico"""
    
    def __init__(self):
        """Inicializa los atributos del cubo"""
        self.name = "cubo"
        # The eight vertices
        self.vertices = [(1, 1, 1),(-1, 1, 1),(-1, -1, 1),(1, -1, 1),
                  (1, 1, -1),(-1, 1, -1),(-1, -1, -1),(1, -1, -1)]
       
        #Colors
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        yellow = (255,255,0)
        purple = (128,0,128)
        cyan = (0,255,255)
        # Triangles
        self.triangles = [[0,1,2,red],
                          [0,2,3,red],
                          [4,0,3,green],
                          [4,3,7,green],
                          [5,4,7,blue],
                          [5,7,6,blue],
                          [1,5,6,yellow],
                          [1,6,2,yellow],
                          [4,5,1,purple],
                          [4,1,0,purple],
                          [2,6,7,cyan],
                          [2,7,3,cyan]]
                          
    def translation(self,position):
        self.vertices=[translateP3D(vertex,position) for vertex in self.vertices]
        
    def rotateX(self,ax):
        print(ax)
        self.vertices=[rotateP3Dx(vertex,ax) for vertex in self.vertices]
        print(self.vertices)
        
    def rotateY(self,ax):
        self.vertices=[rotateP3Dy(vertex,ax) for vertex in self.vertices]
        
    def rotateZ(self,ax):
        self.vertices=[rotateP3Dz(vertex,ax) for vertex in self.vertices]
        
    def scale(self,fs):
        self.vertices=[scaleP3D(vertex,fs) for vertex in self.vertices]
        
        
        

# Tamaño de la imagen
width = 801
height = 801

# Definir un lienzo
canvas = Image.new('RGB', (width,height), (255,255,255))

# Puntos iniciales
cubo1=Cubo()
print(cubo1.vertices)

cubo1.scale(100)
cubo1.rotateZ(math.pi/4)
#cubo1.rotateY(math.pi/4)
cubo1.translation((1.25,2,100))

cubo2=Cubo()
cubo2.scale(80)
#cubo2.rotateZ(math.pi/4)
#cubo1.rotateY(math.pi/4)
cubo2.translation((-1.25,-2,100))
#print(cubo2.vertices)


gl.renderObject(cubo1.vertices,cubo1.triangles,canvas)
gl.renderObject(cubo2.vertices,cubo2.triangles,canvas)
canvas.show()
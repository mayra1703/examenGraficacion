import numpy as np
import graflib as gl
from PIL import Image

# Función que toma un conjunto de puntos tridimensionales y realiza una traslación tridimensional
def translateP3D(points,pt):
	new_points = np.array([points[0],points[1],points[2],1])
	matrix = np.array([[1,0,0,pt[0]],
				 [0,1,0,pt[1]],
				 [0,0,1,pt[2]],
				 [0,0,0,    1]])
	return np.matmul(matrix,new_points.transpose())

# Clase Cubo
class Cubo():
	def __init__(self, position):
		self.name = "cubo"
		self.position = position
		vertex_array = [
			(1, 1, 1), 
			(-1, 1, 1), 
			(-1, -1, 1),
			(1, -1, 1),
			(1, 1, -1),
			(-1, 1, -1),
			(-1, -1, -1),
			(1, -1, -1)]

		# Se calculan y almacenan los vértices del cubo en la propiedad				 
		self.vertex = [translateP3D(vertex,position) for vertex in vertex_array]
	   
		# Colores para las caras del cubo
		red = (255,0,0)
		green = (0,255,0)
		blue = (0,0,255)
		yellow = (255,255,0)
		purple = (128,0,128)
		cyan = (0,255,255)
		
		# Array de triángulos con color
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

	def render(self, canvas):
		projected = []

		for vertex in self.vertex:
			# Función para proyectar los vértices del cubo
			projected.append(gl.projectVertex(vertex))

		for triangle in self.triangles:
			# Función para renderizar cada triángulo en el canvas
			gl.renderTriangle(triangle, projected, canvas)
			

# Tamaño del canvas
width = 501
height = 501

# Definir un lienzo
canvas = Image.new('RGB', (width,height), (255,255,255))

# Posiciones iniciales
cubo1 = Cubo((4,5,5))
cubo2 = Cubo((-4,4,4))
print(cubo1.vertex)

# Método render para renderizar los cubos
cubo1.render(canvas)
cubo2.render(canvas)

canvas.show()

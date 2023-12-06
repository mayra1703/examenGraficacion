from PIL import Image, ImageDraw


class Cubo:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def dibujar(self, imagen):
        draw = ImageDraw.Draw(imagen)
        x0 = self.x
        y0 = self.y
        x1 = x0 + self.size
        y1 = y0 + self.size

        draw.rectangle([x0, y0, x1, y1], fill=self.color)

class Escena:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def dibujar(self, nombre_archivo):
        imagen = Image.new('RGB', (self.width, self.height), color='white')
        
        for objeto in self.objetos:
            objeto.dibujar(imagen)
        
        imagen.save(nombre_archivo)
        imagen.show()

# Ejemplo de uso:
if __name__ == "__main__":
    escena = Escena(600, 600)
    
    cubo1 = Cubo(50, 50, 100, 'blue')
    cubo2 = Cubo(200, 100, 80, 'red')
    cubo3 = Cubo(300, 250, 120, 'green')

    escena.agregar_objeto(cubo1)
    escena.agregar_objeto(cubo2)
    escena.agregar_objeto(cubo3)

    escena.dibujar("escena_con_cubos.png")
import tkinter as tk
from PIL import Image, ImageTk
from cube import Cubo
import math

class RootApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Rotación 3D")
        # self.master.resizable(1,0)
        self.master.geometry("950x500")

        self.canvas = tk.Canvas(self, width=600, height=600, bg="white")
        self.canvas.pack(side="top", fill="both", expand=True)

        self.cubo = Cubo()
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        self.x_slider = tk.Scale(self, label="Rotación X", from_=-180, to=180, orient="horizontal", command=self.rotate_x)
        self.x_slider.set(0)
        self.x_slider.pack()

        self.y_slider = tk.Scale(self, label="Rotación Y", from_=-180, to=180, orient="horizontal", command=self.rotate_y)
        self.y_slider.set(0)
        self.y_slider.pack()

        self.z_slider = tk.Scale(self, label="Rotación Z", from_=-180, to=180, orient="horizontal", command=self.rotate_z)
        self.z_slider.set(0)
        self.z_slider.pack()

        self.draw_cube()

    def rotate_x(self, value):
        self.angle_x = math.radians(int(value))
        self.draw_cube()

    def rotate_y(self, value):
        self.angle_y = math.radians(int(value))
        self.draw_cube()

    def rotate_z(self, value):
        self.angle_z = math.radians(int(value))
        self.draw_cube()

    def draw_cube(self):
        self.canvas.delete("all")

        # Crear una copia del cubo para no deformar el original
        vertices = [tuple(self.cubo.vertices[i]) for i in range(len(self.cubo.vertices))]
        triangles = [list(self.cubo.triangles[i]) for i in range(len(self.cubo.triangles))]
        rotated_cube = Cubo(vertices, triangles)

        # Aplicar rotaciones en los ejes X, Y y Z
        rotated_cube.rotateX(self.angle_x)
        rotated_cube.rotateY(self.angle_y)
        rotated_cube.rotateZ(self.angle_z)

        # Dibujar la figura en el lienzo
        self.draw_object(rotated_cube.vertices, rotated_cube.triangles)

    def draw_object(self, vertices, triangles):
        for triangle in triangles:
            points = []
            for vertex_index in triangle[:-1]:
                x, y = vertices[vertex_index][:2]
                points.extend([x * 100 + 300, y * 100 + 300])  # Escala y traslada las coordenadas
            color = '#%02x%02x%02x' % triangle[-1]  # Convert tuple to hexadecimal color
            self.canvas.create_polygon(points, outline="black", fill=color)

if __name__ == "__main__":
    app = RootApp()
    app.mainloop()


# Простейший GUI
# Демонстрирует создание окна
from tkinter import *

# создание базового окна
root = Tk()

# изменение окна
root.title("Простейший GUI")
root.geometry("200x100")

# старт событийного цикла
root.mainloop()
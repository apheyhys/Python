# Меню ресторана
# Создает чек заказа с общей стоимостью блюд
from tkinter import *

class Application(Frame):
    """GUI-приложение, создающее рассказ на основе пользовательского ввода."""
    def __init__(self, master):
        """Инициализирует рамку."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.the_number = random.randint(1, 100)
        self.tries = 1
# Сумасшедший сказочник
# Создает рассказ на основе пользовательского ввода
from tkinter import *
import random

class Application(Frame):
    """GUI-приложение, с помощью которого пользователь отгадывает число."""
    def __init__(self, master):
        """Инициализирует рамку."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.the_number = random.randint(1, 100)
        self.tries = 1

    def create_widgets(self):
        """Элементы управления"""
        # метка с текстом-инструкцией
        Label(self,
              text = "Добро пожаловать в игру 'Отгадай число'!"
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self,
              text = "Я загадал натуральное число из диапазона от 1 до 100."
              ).grid(row=1, column=0, columnspan=2, sticky=W)
        Label(self,
              text = "Постарайтесь отгадать его за минимальное число попыток."
              ).grid(row=2, column=0, columnspan=2, sticky=W)
        Label(self,
              text = "Ваше предложение:"
              ).grid(row=3, column=0, sticky=W)
        self.number_ent = Entry(self)
        self.number_ent.grid(row=3, column=1, sticky=W)
        # кнопка отсылки данных
        Button(self,
               text = "Получить ответ",
               command = self.tell_story
               ).grid(row=3, column=2, sticky=W)
        self.story_txt = Text(self, width=55, height=2, wrap=WORD)
        self.story_txt.grid(row=5, column=0, columnspan=4)

    def tell_story(self):
        # начальные значения
        the_number = self.the_number
        number_ent = int(self.number_ent.get()) # переводим строку в число
        max = 100
        min = 1
        # проверяем введенное число на соответствие диапозону
        if number_ent > max or number_ent < min:
            number_out = "Число выходит за пределы диапазона от 1 до 100!"
        else:
            if number_ent > the_number:
                number_out = "Меньше..."
                self.tries += 1
            elif number_ent < the_number:
                number_out = "Больше..."
                self.tries += 1
            else:
                number_out = "Вам удалось отгадасть число! Это в самом деле число " + str(the_number) + "!"
                number_out += " Вы затратили на отгадывание всего лишь " + str(self.tries) + " попыток!"
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, number_out)


# основная часть
root = Tk()
root.title("Отгадай число!")
app = Application(root)
root.mainloop()
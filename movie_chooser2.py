# Киноман - 2
# Демонстрирует применение переключателей
from tkinter import *

class Application(Frame):
    """GUI-приложение, позволяющее выбрать один жанр кино."""
    def __init__(self, master):
        """Инициализирует рамку."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает элементы, с помощью которых пользователь будет выбирать."""
        # метка описание
        Label(self, text="Укажите ваши любимые жанры кино").grid(row=0, column=0, sticky=W)
        # метка-инструкция
        Label(self, text="Выберите ровно один:").grid(row=1, column=0, sticky=W)
        # переменная для хранения сведений о единственном любимом жанре
        self.favorite = StringVar()
        self.favorite.set(None)
        # положение "Комедия" переключателя
        Radiobutton(
                    self,
                    text = "Комедия",
                    variable = self.favorite,
                    value = "комедия.",
                    command = self.update_text
                    ).grid(row=2, column=0, sticky=W)
        # положение "Драма" переключателя
        Radiobutton(
                    self, text = "Драма",
                    variable = self.favorite,
                    value = "драма.",
                    command = self.update_text
                    ).grid(row=3, column=0, sticky=W)
        # положение "Фильм о любви" переключателя
        Radiobutton(self,
                    text = "Фильм о любви",
                    variable = self.favorite,
                    value = "кино о любви.",
                    command = self.update_text
                    ).grid(row=4, column=0, sticky=W)
        # текстовая область с результатами
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """Обновляет текстовую область, вписывает в нее любимый жанр."""
        message = "Ваш любимый киножанр - "
        message += self.favorite.get()
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)
        
# основная часть
root = Tk()
root.title("Киноман-2")
app = Application(root)
root.mainloop()
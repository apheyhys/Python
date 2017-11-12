# Киноман
# Демонстрирует применение флажков
from tkinter import *

class Application(Frame):
    """GUI-приложение, позволяющее выбрать любимые жанры кино."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Создает элементы, с помощью которых пользователь будет выбирать."""
        # метка описание
        Label(self, text="Укажите ваши любимые жанры кино").grid(row=0, column=0, sticky=W)
        # метка-инструкция
        Label(self, text="Выберите все, что вам по вкусу:").grid(row=1, column=0, sticky=W)
        # флажок "Комедия"
        self.likes_comedy = BooleanVar()
        Checkbutton(self, text="Комедия", variable = self.likes_comedy, command = self.update_text).grid(row=2, column=0, sticky=W)
        # флажок "Драма"
        self.likes_drama = BooleanVar()
        Checkbutton(self, text="Драма", variable=self.likes_drama, command=self.update_text).grid(row=3, column=0, sticky=W)
        # флажок "Фильм о любви"
        self.likes_romance = BooleanVar()
        Checkbutton(self, text="Фильм о любви", variable=self.likes_romance, command=self.update_text).grid(row=4, column=0, sticky=W)
        # текстовая область с результатами
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """Обновляет тектовый элемент по мере того, как пользователь выбирает свои любимые киножанры."""
        likes = ""
        if self.likes_comedy.get():
            likes += "Вам нравятся комедии.\n"
        if self.likes_drama.get():
            likes += "Вас привлекает жанр драмы.\n"
        if self.likes_romance.get():
            likes += "Вам по вкусу кино о любви."
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

# основная часть
root = Tk()
root.title("Киноман")
app = Application(root)
root.mainloop()
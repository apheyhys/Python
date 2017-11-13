# Меню ресторана
# Создает чек заказа с общей стоимостью блюд
from tkinter import *

class Application(Frame):
    """GUI-приложение, создающее счет на основе меню."""
    def __init__(self, master):
        """Инициализирует рамку."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Элементы управления"""
        self.item1 = "Солянка мясная (250гр.) - 60 руб. "
        self.item2 = "Куриный крем-суп (250гр.) - 50 руб. руб. "
        self.item3 = "Запеканка картофельная с мясом (150гр.) - 75 руб. "
        self.item4 = "Бигус (150гр.) - 85 руб. "
        self.item5 = "Котлеты по-киевски (150гр.) - 120 руб. "
        self.item6 = "Спагетти (150гр.) - 40 руб. "
        self.item7 = "Картофель по-деревенски (150гр.) - 45 руб. "
        self.item8 = "Кофе (200мл.) - 30 руб. "
        self.item9 = "Чай черный (200мл.) - 20 руб. "
        # список для подстановки количества блюд
        counts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # метка с текстом-инструкцией
        Label(self,
              text = "Добро пожаловать в ресторан Сытный!"
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        # меню
        Label(self,
              text="Супы:"
              ).grid(row=1, column=0, sticky=W)
        Label(self,
              text=self.item1
              ).grid(row=2, column=0, sticky=W)
        self.count1 = IntVar()
        self.count1.set(1)
        OptionMenu(self, self.count1, *counts).grid(row=2, column=1, sticky=W)
        self.item1_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item1_choise
                    ).grid(row=2, column=2, sticky=W)
        Label(self,
              text=self.item2
              ).grid(row=3, column=0, sticky=W)
        self.count2 = IntVar()
        self.count2.set(1)
        OptionMenu(self, self.count2, *counts).grid(row=3, column=1, sticky=W)
        self.item2_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item2_choise
                    ).grid(row=3, column=2, sticky=W)
        Label(self,
              text="Мясо:"
              ).grid(row=4, column=0, sticky=W)
        Label(self,
              text=self.item3
              ).grid(row=5, column=0, sticky=W)
        self.count3 = IntVar()
        self.count3.set(1)
        OptionMenu(self, self.count3, *counts).grid(row=5, column=1, sticky=W)
        self.item3_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item3_choise
                    ).grid(row=5, column=2, sticky=W)
        Label(self,
              text=self.item4
              ).grid(row=6, column=0, sticky=W)
        self.count4 = IntVar()
        self.count4.set(1)
        OptionMenu(self, self.count4, *counts).grid(row=6, column=1, sticky=W)
        self.item4_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item4_choise
                    ).grid(row=6, column=2, sticky=W)
        Label(self,
              text=self.item5
              ).grid(row=7, column=0, sticky=W)
        self.count5 = IntVar()
        self.count5.set(1)
        OptionMenu(self, self.count5, *counts).grid(row=7, column=1, sticky=W)
        self.item5_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item5_choise
                    ).grid(row=7, column=2, sticky=W)
        Label(self,
              text="Гарниры:"
              ).grid(row=8, column=0, sticky=W)
        Label(self,
              text=self.item6
              ).grid(row=9, column=0, sticky=W)
        self.count6 = IntVar()
        self.count6.set(1)
        OptionMenu(self, self.count6, *counts).grid(row=9, column=1, sticky=W)
        self.item6_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item6_choise
                    ).grid(row=9, column=2, sticky=W)
        Label(self,
              text=self.item7
              ).grid(row=10, column=0, sticky=W)
        self.count7 = IntVar()
        self.count7.set(1)
        OptionMenu(self, self.count7, *counts).grid(row=10, column=1, sticky=W)
        self.item7_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item7_choise
                    ).grid(row=10, column=2, sticky=W)
        Label(self,
              text="Напитки:"
              ).grid(row=11, column=0, sticky=W)
        Label(self,
              text=self.item8
              ).grid(row=12, column=0, sticky=W)
        self.count8 = IntVar()
        self.count8.set(1)
        OptionMenu(self, self.count8, *counts).grid(row=12, column=1, sticky=W)
        self.item8_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item8_choise
                    ).grid(row=12, column=2, sticky=W)
        Label(self,
              text=self.item9
              ).grid(row=13, column=0, sticky=W)
        self.count9 = IntVar()
        self.count9.set(1)
        OptionMenu(self, self.count9, *counts).grid(row=13, column=1, sticky=W)
        self.item9_choise = BooleanVar()
        Checkbutton(self,
                    text="",
                    variable=self.item9_choise
                    ).grid(row=13, column=2, sticky=W)
        # кнопка отсылки данных
        Button(self,
               text="Получить счет",
               command=self.score
               ).grid(row=14, column=0, sticky=W)
        self.score_txt = Text(self, width=60, height=10, wrap=WORD)
        self.score_txt.grid(row=15, column=0, columnspan=3)


    def score(self):
        """Заполняем счет на основе пользовательского ввода"""
        count1 = self.count1.get()
        count2 = self.count2.get()
        count3 = self.count3.get()
        count4 = self.count4.get()
        count5 = self.count5.get()
        count6 = self.count6.get()
        count7 = self.count7.get()
        count8 = self.count8.get()
        count9 = self.count9.get()
        t_item1 = 0
        t_item2 = 0
        t_item3 = 0
        t_item4 = 0
        t_item5 = 0
        t_item6 = 0
        t_item7 = 0
        t_item8 = 0
        t_item9 = 0
        total = 0
        menu = "Ваш счет:"
        if self.item1_choise.get():
            total += count1 * 60
            t_item1 = count1 * 60
            menu += "\n" + self.item1 + str(count1) + " шт. " + str(t_item1) + "руб."
        if self.item2_choise.get():
            total += count2 * 50
            t_item2 = count2 * 50
            menu += "\n" + self.item2 + str(count2) + " шт. " + str(t_item2) + "руб."
        if self.item3_choise.get():
            total += count3 * 75
            t_item3 = count3 * 75
            menu += "\n" + self.item3 + str(count3) + " шт. " + str(t_item3) + "руб."
        if self.item4_choise.get():
            total += count4 * 85
            t_item4 = count4 * 85
            menu += "\n" + self.item4 + str(count4) + " шт. " + str(t_item4) + "руб."
        if self.item5_choise.get():
            total += count5 * 120
            t_item5 = count5 * 120
            menu += "\n" + self.item5 + str(count5) + " шт. " + str(t_item5) + "руб."
        if self.item6_choise.get():
            total += count6 * 40
            t_item6 = count6 * 40
            menu += "\n" + self.item6 + str(count6) + " шт. " + str(t_item6) + "руб."
        if self.item7_choise.get():
            total += count7 * 45
            t_item7 = count7 * 45
            menu += "\n" + self.item7 + str(count7) + " шт. " + str(t_item7) + "руб."
        if self.item8_choise.get():
            total += count8 * 30
            t_item8 = count8 * 30
            menu += "\n" + self.item8 + str(count8) + " шт. " + str(t_item8) + "руб."
        if self.item9_choise.get():
            total += count9 * 20
            t_item9 = count9 * 20
            menu += "\n" + self.item9 + str(count9) + " шт. " + str(t_item9) + "руб."
        menu += "\nИтого: " + str(total) + "руб."
        menu += "\nСпасибо! Ждем вас снова!"
        self.score_txt.delete(0.0, END)
        self.score_txt.insert(0.0, menu)

# основная часть
root = Tk()
root.title("Меню")
app = Application(root)
root.mainloop()
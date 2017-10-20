# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться
import random

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name):
        hunger = random.randint(0, 8)
        boredom = random.randint(0, 8)
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        stroka = "Параметры зверюшки:\n\n"
        stroka += "имя:" + self.name + "\n" + "уровень голода:" + str(self.hunger) + "\n" "уровень уныния:" + str(self.boredom) + "\n"
        return stroka

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11<= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print("Меня зовут", self.name, ", и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()

    def eat(self, portion):
        self.hunger -= portion
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, hours_of_play):
        self.boredom -= hours_of_play
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    print("Добро пожаловать на зооферму!\n")
    # создаем 3 разные зверюшки
    crit_name1 = input("Как вы назовете свою первую зверюшку? ")
    crit1 = Critter(crit_name1)
    crit_name2 = input("Как вы назовете свою вторую зверюшку? ")
    crit2 = Critter(crit_name2)
    crit_name3 = input("Как вы назовете свою третью зверюшку? ")
    crit3 = Critter(crit_name3)
    choice = None
    while choice != "0":
        print(
            """
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствии зверюшек
            2 - Покормить зверюшек
            3 - Поиграть со зверюшками
            """
        )
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверюшками
        elif choice == "1":
            crit1.talk()
            crit2.talk()
            crit3.talk()
        # кормление зверюшки
        elif choice == "2":
            while True:
                portion = int(input("Введите количество порций еды, которые вы хотите дать зверюшкам (от 1 до 4):"))
                if portion < 1 or portion > 4:
                    print("Вы ввели неправильное количество порций. Число должно быть от 1 до 4")
                else:
                    print("Мррр... Спасибо!")
                    crit1.eat(portion)
                    crit2.eat(portion)
                    crit3.eat(portion)
                    break
        # игра со зверюшкой
        elif choice == "3":
            while True:
                hours_of_play = int(
                    input("Введите количество часов, в которые вы хотите поиграть со зверюшками (от 1 до 4):"))
                if hours_of_play < 1 or hours_of_play > 4:
                    print("Вы ввели неправильное количество часов. Число должно быть от 1 до 4")
                    continue
                else:
                    print("Уиии!")
                    crit1.play(hours_of_play)
                    crit2.play(hours_of_play)
                    crit3.play(hours_of_play)
                    break
        # секретный ход
        elif choice == "666":
            print(crit1)
            print(crit2)
            print(crit3)
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

main()
input("\nНажмите Enter, чтобы выйти.")


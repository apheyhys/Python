# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться
class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

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

    def eat(self):
        while True:
            portion = int(input("Введите количество порций еды, которые вы хотите дать зверюшки (от 1 до 4):"))
            if portion < 1 or portion > 4:
                print("Вы ввели неправильное количество порций. Число должно быть от 1 до 4")
            else:
                print("Мррр... Спасибо!")
                self.hunger -= portion
                if self.hunger < 0:
                    self.hunger = 0
                print(self.hunger)
                self.__pass_time()
                break

    def play(self):
        while True:
            hours_of_play = int(input("Введите количество часов, в которые вы хотите поиграть со зверюшкой (от 1 до 4):"))
            if hours_of_play < 1 or hours_of_play > 4:
                print("Вы ввели неправильное количество часов. Число должно быть от 1 до 4")
                continue
            else:
                print("Уиии!")
                self.boredom -= hours_of_play
                if self.boredom < 0:
                    self.boredom = 0
                print(self.boredom)
                self.__pass_time()
                break

def main():
    crit_name = input("Как вы назовете свою зверюшку? ")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print(
            """
            Моя зверюшка
            0 - Выйти
            1 - Узнать о самочувствии зверюшки
            2 - Покормить зверюшку
            3 - Поиграть со зверюшкой
            """
        )
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        # кормление зверюшки
        elif choice == "2":
            crit.eat()
        # игра со зверюшкой
        elif choice == "3":
            crit.play()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)

main()
input("\nНажмите Enter, чтобы выйти.")


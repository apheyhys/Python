# Простая приключенческая игра, персонаж перемещается по 3 мирам
import adventure_environment

class AT_Game(object):
    def __init__(self, name):
        self.name = name
        other_position = 1
        self.other_position = other_position
        adventure_environment.ask_move(other_position)

    @property
    def location(self):
        if self.other_position in range(1, 9):
            loc = "Левая локация"
        elif self.other_position in range(11, 19):
            loc = "Центральная локация"
        elif self.other_position in range(21, 30):
            loc = "Правая локация"
        else:
            loc = "Переход"
        return loc

    def static_position(self):
        while 1:
            if self.other_position == 1 or self.other_position == 11 or self.other_position == 21:
                new_move = str(input("Введите направление движения, куда вы хотите пойти: вниз(d) или вправо(r): "))
                if new_move == "d":
                    if self.other_position == 1:
                        self.new_position = adventure_environment.ask_move(move=4)
                    if self.other_position == 11:
                        self.new_position = adventure_environment.ask_move(move=14)
                    if self.other_position == 21:
                        self.new_position = adventure_environment.ask_move(move=24)
                elif new_move == "r":
                    if self.other_position == 1:
                        self.new_position = adventure_environment.ask_move(move=2)
                    if self.other_position == 11:
                        self.new_position = adventure_environment.ask_move(move=12)
                    if self.other_position == 21:
                        self.new_position = adventure_environment.ask_move(move=22)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 2 or self.other_position == 12 or self.other_position == 22:
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(input("Введите направление движения, куда вы хотите пойти: вниз(d) или вправо(r) или влево(l): "))
                if new_move == "d":
                    if self.other_position == 2:
                        self.new_position = adventure_environment.ask_move(move=5)
                    if self.other_position == 12:
                        self.new_position = adventure_environment.ask_move(move=15)
                    if self.other_position == 22:
                        self.new_position = adventure_environment.ask_move(move=25)
                elif new_move == "r":
                    if self.other_position == 2:
                        self.new_position = adventure_environment.ask_move(move=3)
                    if self.other_position == 12:
                        self.new_position = adventure_environment.ask_move(move=13)
                    if self.other_position == 22:
                        self.new_position = adventure_environment.ask_move(move=23)
                elif new_move == "l":
                    if self.other_position == 2:
                        self.new_position = adventure_environment.ask_move(move=1)
                    if self.other_position == 12:
                        self.new_position = adventure_environment.ask_move(move=11)
                    if self.other_position == 22:
                        self.new_position = adventure_environment.ask_move(move=21)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 3 or self.other_position == 13 or self.other_position == 23:
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(
                    input("Введите направление движения, куда вы хотите пойти: вниз(d) или влево(l): "))
                if new_move == "d":
                    if self.other_position == 3:
                        self.new_position = adventure_environment.ask_move(move=6)
                    if self.other_position == 13:
                        self.new_position = adventure_environment.ask_move(move=16)
                    if self.other_position == 23:
                        self.new_position = adventure_environment.ask_move(move=26)
                elif new_move == "l":
                    if self.other_position == 3:
                        self.new_position = adventure_environment.ask_move(move=2)
                    if self.other_position == 13:
                        self.new_position = adventure_environment.ask_move(move=12)
                    if self.other_position == 23:
                        self.new_position = adventure_environment.ask_move(move=22)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 4 or self.other_position == 14 or self.other_position == 24:
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(input("Введите направление движения, куда вы хотите пойти: вниз(d) или вправо(r) или вверх(u): "))
                if new_move == "d":
                    if self.other_position == 4:
                        self.new_position = adventure_environment.ask_move(move=7)
                    if self.other_position == 14:
                        self.new_position = adventure_environment.ask_move(move=17)
                    if self.other_position == 24:
                        self.new_position = adventure_environment.ask_move(move=27)
                elif new_move == "r":
                    if self.other_position == 4:
                        self.new_position = adventure_environment.ask_move(move=5)
                    if self.other_position == 14:
                        self.new_position = adventure_environment.ask_move(move=15)
                    if self.other_position == 24:
                        self.new_position = adventure_environment.ask_move(move=25)
                elif new_move == "u":
                    if self.other_position == 4:
                        self.new_position = adventure_environment.ask_move(move=1)
                    if self.other_position == 14:
                        self.new_position = adventure_environment.ask_move(move=11)
                    if self.other_position == 24:
                        self.new_position = adventure_environment.ask_move(move=21)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 5 or self.other_position == 6 or self.other_position == 14 or self.other_position == 15 or self.other_position == 16 or self.other_position == 24 or self.other_position == 25:
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(input("Введите направление движения, куда вы хотите пойти: вниз(d) или вправо(r) или вверх(u): "))
                if new_move == "r":
                    if self.other_position == 5:
                        self.new_position = adventure_environment.ask_move(move=6)
                    if self.other_position == 6:
                        self.new_position = adventure_environment.ask_move(move=10)
                    if self.other_position == 14:
                        self.new_position = adventure_environment.ask_move(move=15)
                    if self.other_position == 15:
                        self.new_position = adventure_environment.ask_move(move=16)
                    if self.other_position == 16:
                        self.new_position = adventure_environment.ask_move(move=20)
                    if self.other_position == 24:
                        self.new_position = adventure_environment.ask_move(move=25)
                    if self.other_position == 25:
                        self.new_position = adventure_environment.ask_move(move=26)
                elif new_move == "d":
                    if self.other_position == 5:
                        self.new_position = adventure_environment.ask_move(move=8)
                    if self.other_position == 6:
                        self.new_position = adventure_environment.ask_move(move=9)
                    if self.other_position == 14:
                        self.new_position = adventure_environment.ask_move(move=17)
                    if self.other_position == 15:
                        self.new_position = adventure_environment.ask_move(move=18)
                    if self.other_position == 16:
                        self.new_position = adventure_environment.ask_move(move=19)
                    if self.other_position == 24:
                        self.new_position = adventure_environment.ask_move(move=27)
                    if self.other_position == 25:
                        self.new_position = adventure_environment.ask_move(move=28)
                elif new_move == "l":
                    if self.other_position == 5:
                        self.new_position = adventure_environment.ask_move(move=4)
                    if self.other_position == 6:
                        self.new_position = adventure_environment.ask_move(move=5)
                    if self.other_position == 14:
                        self.new_position = adventure_environment.ask_move(move=10)
                    if self.other_position == 15:
                        self.new_position = adventure_environment.ask_move(move=14)
                    if self.other_position == 16:
                        self.new_position = adventure_environment.ask_move(move=15)
                    if self.other_position == 24:
                        self.new_position = adventure_environment.ask_move(move=20)
                    if self.other_position == 25:
                        self.new_position = adventure_environment.ask_move(move=24)
                elif new_move == "u":
                    if self.other_position == 5:
                        self.new_position = adventure_environment.ask_move(move=2)
                    if self.other_position == 6:
                        self.new_position = adventure_environment.ask_move(move=3)
                    if self.other_position == 14:
                        self.new_position = adventure_environment.ask_move(move=11)
                    if self.other_position == 15:
                        self.new_position = adventure_environment.ask_move(move=12)
                    if self.other_position == 16:
                        self.new_position = adventure_environment.ask_move(move=13)
                    if self.other_position == 24:
                        self.new_position = adventure_environment.ask_move(move=21)
                    if self.other_position == 25:
                        self.new_position = adventure_environment.ask_move(move=22)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 7 or self.other_position == 17 or self.other_position == 27:
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(
                    input("Введите направление движения, куда вы хотите пойти: вверх(u) или вправо(r): "))
                if new_move == "u":
                    if self.other_position == 7:
                        self.new_position = adventure_environment.ask_move(move=4)
                    if self.other_position == 17:
                        self.new_position = adventure_environment.ask_move(move=14)
                    if self.other_position == 27:
                        self.new_position = adventure_environment.ask_move(move=24)
                elif new_move == "r":
                    if self.other_position == 7:
                        self.new_position = adventure_environment.ask_move(move=8)
                    if self.other_position == 17:
                        self.new_position = adventure_environment.ask_move(move=18)
                    if self.other_position == 27:
                        self.new_position = adventure_environment.ask_move(move=28)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 8 or self.other_position == 18 or self.other_position == 28:
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(input("Введите направление движения, куда вы хотите пойти: вверх(u) или вправо(r) или влево(l): "))
                if new_move == "u":
                    if self.other_position == 8:
                        self.new_position = adventure_environment.ask_move(move=5)
                    if self.other_position == 18:
                        self.new_position = adventure_environment.ask_move(move=15)
                    if self.other_position == 28:
                        self.new_position = adventure_environment.ask_move(move=25)
                elif new_move == "r":
                    if self.other_position == 8:
                        self.new_position = adventure_environment.ask_move(move=9)
                    if self.other_position == 18:
                        self.new_position = adventure_environment.ask_move(move=19)
                    if self.other_position == 28:
                        self.new_position = adventure_environment.ask_move(move=29)
                elif new_move == "l":
                    if self.other_position == 8:
                        self.new_position = adventure_environment.ask_move(move=7)
                    if self.other_position == 18:
                        self.new_position = adventure_environment.ask_move(move=17)
                    if self.other_position == 28:
                        self.new_position = adventure_environment.ask_move(move=27)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 9 or self.other_position == 19 or self.other_position == 29:
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(
                    input("Введите направление движения, куда вы хотите пойти: вверх(u) или влево(l): "))
                if new_move == "u":
                    if self.other_position == 9:
                        self.new_position = adventure_environment.ask_move(move=6)
                    if self.other_position == 19:
                        self.new_position = adventure_environment.ask_move(move=16)
                    if self.other_position == 29:
                        self.new_position = adventure_environment.ask_move(move=26)
                elif new_move == "l":
                    if self.other_position == 9:
                        self.new_position = adventure_environment.ask_move(move=8)
                    if self.other_position == 19:
                        self.new_position = adventure_environment.ask_move(move=18)
                    if self.other_position == 29:
                        self.new_position = adventure_environment.ask_move(move=28)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position
            if self.other_position == 10 or self.other_position == 20 :
                print("Герой по имени ", self.name, "находится в следующей локации - ", self.location)
                new_move = str(
                    input("Введите направление движения, куда вы хотите пойти: вправо(r) или влево(l): "))
                if new_move == "r":
                    if self.other_position == 10:
                        self.new_position = adventure_environment.ask_move(move=14)
                    if self.other_position == 20:
                        self.new_position = adventure_environment.ask_move(move=24)
                elif new_move == "l":
                    if self.other_position == 10:
                        self.new_position = adventure_environment.ask_move(move=6)
                    if self.other_position == 20:
                        self.new_position = adventure_environment.ask_move(move=16)
                else:
                    print("В этом направлении нельзя идти, выберете другое")
                self.other_position = self.new_position



def main():
    print("\t\tДобро пожаловать в простую приключенческую игру!\n")
    name = input("Введите имя игрока: ")
    game = AT_Game(name)
    game.static_position()


main()
input("\n\nНажмите Enter, чтобы выйти.")
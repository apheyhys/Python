# Имитация телевизора
# Программа имитирует работу телевизора

class TVimit(object):
    """Телевизор"""

    def __init__(self, channel, volume):
        self.volume = volume
        self.channel = channel

    def information(self):
        print("Текущие параметры телевизора:")
        print("\tНомер канала:", self.channel)
        print("\tУстановленный уровень звука:", self.volume)

    def reduce_volume(self):
        if self.volume == 0:
            print("На данный момент установлен минимальный уровень звука")
        else:
            self.volume -= 1
        self.information()

    def increase_volume(self):
        if self.volume > 14:
            print("На данный момент установлен максимальный уровень звука")
        else:
            self.volume += 1
        self.information()

    def change_channel(self):
        while True:
            channel = int(input("Введите номер канала: "))
            if channel < 1 or channel > 15:
                print("Такого канала не существует, выберете другой.")
                continue
            else:
                self.channel = channel
                break
        self.information()


def main():
    print("Добро пожаловать в приложение 'Телевизор'\n")
    channel = 0
    trying = TVimit(channel, volume=0)
    choice = None
    print()
    trying.change_channel()
    while choice != "0":
        print(
            """
            Телевизор
            0 - Выйти
            1 - Увеличить уровень звука
            2 - Уменьшить уровень звука
            3 - Изменить номер канала
            """
        )
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # Увеличить уровень звука
        elif choice == "1":
            trying.increase_volume()
        # Уменьшить уровень звука
        elif choice == "2":
            trying.reduce_volume()
        # Изменить номер канала
        elif choice == "3":
            trying.change_channel()
        # непонятный пользовательский ввод
        else:
            print("Извините, в меню нет пункта", choice)


main()
input("\nНажмите Enter, чтобы выйти.")

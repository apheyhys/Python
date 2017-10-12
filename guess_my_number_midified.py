#Отгадай число
#
#Копьютер выбирает случайное число в диапазоне от 1 до 100
#Игрок пытается отгадать это число, и компьютер говорит,
#предложение больше/меньше, чем заданное число,
#или попало в точку
import random

# глобальные константы
the_number = random.randint(1, 100)
multiplicity = 1


# функция для вывода инструкции
def display_instruct():
    print("\tДобро пожаловать в игру 'Отгадай число'!")
    print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
    print("Постарайтесь отгадать его за минимальное число попыток.\n")

# функция для получения числа из диапазона
def ask_number(question, low, high, multiplicity):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = input(question)
        if response == "":
            continue
        response = float(response)
        if response%multiplicity > 0:
            continue
        response = int(response)
    return response


def winner(the_number, tries):
    print("Вам удалось отгадасть число! Это в самом деле", the_number)
    print("Вы затратили на отгадывание всего лишь ", tries, " попыток!\n")

def main():
    guess = None
    tries = 0
    display_instruct()
    while guess != the_number:
        guess = ask_number("Ваше предположение: ", 0, 101, multiplicity)
        if guess > the_number:
            print("Меньше...")
        elif guess < the_number:
            print("Больше...")
        tries += 1
    winner(the_number, tries)


# запуск программы
main()
input("\n\nНажмите Enter, чтобы выйти.")
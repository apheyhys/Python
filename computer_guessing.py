#Программа пытается отгадать загадонное число
print("Добрый день! Я отгадаю любое число, которое вы загадали в диапазоне от 1 до 100")
tries = 1
number = 50
low = 1
high = 100
guess = 0
while True:
    print("Это число ", number, "?")
    guess = (input("Больше, меньше, угадал?\n"))
    if guess == "Больше" or guess == "больше":
        low = number
        number = number - (low-high)//2
    elif guess == "Меньше" or guess == "меньше":
        high = number
        number = number + (low-high)//2
    elif guess == "Угадал" or guess == "угадал":
        break
    else:
        print("Введите команду еще раз. Я не понял.")
    tries +=1
print("Мне удалось отгадать число! Это число ", number)
print("Для этого мне потребовалось ", tries, "попыток")
print("\n\nВведите Enter, для того чтобы выйти")
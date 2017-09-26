# Компьютер загадывает слово, которое должен угадать человек
# Компьютер сообщает количество букв в слове, и дает пять попыток узнать, есть ли какая-то буква в слове,
# причем программа может отвечать только Да или Нет.
import random
# создадим последовательность слов, из которых компьютер будет выбирать
WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)

print("""
    Компьютер загадал слово. Попробуйте его отгадать. 
    Компьютер сообщает количество букв в слове, и дает пять попыток узнать, есть ли какая то буква в слове,
    причем программа может отвечать только Да или Нет.
          """)
# счетчик количества букв в слове
count = len(word)
print("В загаданном компьютером слове ", count, "букв")
hint = 1
guess = 0
while guess != word:
    guess = input("\nПопробуйте отгадать слово, либо введите одну любую букву. Компьютер проверит ее наличие в слове: ")
    count_guess = len(guess)
    print(count_guess)
    if count_guess == 1:
        if hint != 6:
            if guess in word:
                if hint != 4:
                    print("\nДа, такая буква есть в слове. У вас осталось ", 5-hint, "подсказки")
                elif hint == 5:
                    print("\nДа, такая буква есть в слове. У вас осталось ", 5-hint, "подсказок")
                else:
                    print("\nДа, такая буква есть в слове. У вас осталась ", 5-hint, "подсказка")
            else:
                if hint != 4:
                    print("\nНет, такой буквы нет в слове. У вас осталось ", 5-hint, "подсказки")
                elif hint == 5:
                    print("\nНет, такой буквы нет в слове. У вас осталось ", 5-hint, "подсказок")
                else:
                    print("\nНет, такой буквы нет в слове. У вас осталась ", 5-hint, "подсказка")
        else:
            print("\nК сожалению вы использовали все 5 подсказок и не угадали")
            print("Компьютер загадал слово: ", word)
            break
        hint += 1
    elif guess == word:
        break
    else:
        if guess == "":
            print("\nВы ничего не ввели")
        else:
            print("\nВы не угадали")

if guess == word:
    if hint == 1 or hint == 6:
        print("\nВы угадали слово, использовав ", hint - 1, "подсказок. Компьютер загадал слово: ", word)
    elif hint == 2:
        print("\nВы угадали слово, использовав ", hint - 1, "подсказку. Компьютер загадал слово: ", word)
    else:
        print("\nВы угадали слово, использовав ", hint - 1, "подсказки. Компьютер загадал слово: ", word)
print("\nСпасибо за игру")



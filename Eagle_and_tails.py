#Программа 100 раз подбрасывает монетку и показывает сколько раз выпал орел, а сколько раз решка
import random
number_of_shots = 0
eagle = 0
tails = 0
while number_of_shots != 100:
    throw = random.randint(1, 2)
    if throw == 1:
        eagle += 1
        number_of_shots += 1
    else:
        tails += 1
        number_of_shots += 1

print("После 100 бросков выпал", eagle, "орел и ", tails, "решка")
input("\n\nНажмите Enter, чтобы выйти")

#Программа выдающая 5 различных пирожков с сюрпризом
import random
number_of_pie = random.randint(1, 5)
if number_of_pie == 1:
    print("Вам достался пирожок с капустой")
elif number_of_pie == 2:
    print("Вам достался пирожок с картошкой")
elif number_of_pie == 3:
    print("Вам достался пирожок с вишней")
elif number_of_pie == 4:
    print("Вам достался пирожок с сыром и ветчиной")
else:
    print("Вам достался пирожок с ничем")
input("\n\nНажмите Enter, чтобы выйти.")
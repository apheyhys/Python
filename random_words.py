# программа печатает список слов с определением в случайном порядке
# используются словари
import random
WORDS = ["Мещанство",
         "Приоритет",
         "Паноктикум",
         "Шапокляк",
         "Апокриф"]
newshuffle = []
while len(newshuffle) != len(WORDS):
    j = random.choice(WORDS)
    if j in newshuffle:
        continue
    else:
        newshuffle.append(j)
        print(j)



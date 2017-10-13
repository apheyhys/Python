# Викторина
# Игра на выбор правильного варианта ответа.
# вопросы которой читаются из текстового файла
import sys
import pickle

def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл", file_name, ". Работа программы будет завершена.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        explanation = next_line(the_file)
        nominal = int(next_line(the_file))
    else:
        correct = ""
        explanation = ""
        nominal = ""
    return category, question, answers, correct, explanation, nominal


def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")


def record_tabble(finally_nominal, players_name):
    print("\n\t\tТаблица рекордов:\n")
    f = open("textfiles/trivia_record.dat", "ab")
    name_record = (finally_nominal, players_name)
    pickle.dump(name_record, f)
    f.close()
    f = open("textfiles/trivia_record.dat", "rb")
    scores = []
    while f:
        try:
            scores.append(pickle.load(f))
        except:
            break
    scores.sort(reverse=True)
    scores = scores[:5]
    for x in scores:
        print("\t", x[1], "-", x[0])
    f.close()

def main():
    trivia_file = open("textfiles/trivia_new.txt", "r", encoding='utf-8')
    title = next_line(trivia_file)
    players_name = input("\nВведите свое имя: ")
    welcome(title)
    score = 0
    # извлечение первого блока
    category, question, answers, correct, explanation, nominal = next_block(trivia_file)
    finally_nominal = 0
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # получение ответа
        answer = input("Ваш ответ: ")
        # проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            print("\nДа, за этот вопрос вы заработали", nominal, "баллов")
            finally_nominal += nominal
        else:
            print("\nНет!", end=" ")
        print(explanation)
        # переход к следующему вопросу
        category, question, answers, correct, explanation, nominal = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос!\n")
    print("Ваш итоговый счет: ", finally_nominal)
    record_tabble(finally_nominal, players_name)


main()
input("\n\nНажмите Enter, чтобы выйти.")

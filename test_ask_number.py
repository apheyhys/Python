# тестирование функции с новым пораметром - кратность
multiplicity = 1
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


test = ask_number("Твой ход. Это должно быть целое число. Выбери одно из полей (0 - 8): ", 0, 9, multiplicity)
print(test)
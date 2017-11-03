# Блек-джек
# От 1 до 7 игроков против дилера
import cards, games

class BJ_Card(cards.Card):
    """Карта для игры в Блек-джек."""

    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(cards.Deck):
    """Колода для игры в 'Блек-джек'."""

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """Рука: набор карт у одного игрока."""

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
        score = 100 # в начале игры каждому игроку дается по 100 баллов
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    def big_question(self): # если на счету игрока 0 баллов, то возвращаем 0
        if self.score == 0:
            print("На счету игрока", self.name, "закончились деньги")
            answer = 0
            self.answer = answer
            return self.answer

    def question_rate(self): # спрашиваем ставку каждого игрока в новой игре
        print("В банке игрока", self.name, "-", self.score, "баллов")
        grate = games.ask_number("Введите вашу ставку: ", low=1, high=self.score + 1)
        self.grate = grate
        return self.grate

    @property
    def total(self):
        # если у одной из карт value равно None, то и все свойство равно None
        for card in self.cards:
            if not card.value:
                return None
        # суммируем очки, считая каждый туз за 1 очко
        t = 0
        for card in self.cards:
            t += card.value
        # определяем, есть ли туз на руках у игрока
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        # если на руках есть туз и сумма очков не превышает 11, будем считать туз за 11 очков
        if contains_ace and t <= 11:
            # прибавить нужно лишь 10, потому что единица уже вошла в общую сумму
            t += 10
        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """Игрок в 'Блек-джек'."""

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", будете брать еще карты? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, "перебрал.")
        self.lose()

    def lose(self):
        print(self.name, "проиграл.")
        self.score -= self.grate # если проиграл, то отнимаем баллы
        print("На счету игрока", self.name, "-", self.score, "баллов\n")

    def win(self):
        print(self.name, "выиграл.")
        self.score += self.grate # если выиграл, то прибавляем
        print("На счету игрока", self.name, "-", self.score, "баллов\n")

    def push(self):
        print(self.name, "сыграл с компьютером вничью.") # при ничьей отставляем банк игрока неизменным
        print("На счету игрока", self.name, "-", self.score, "баллов\n")



class BJ_Dealer(BJ_Hand):
    """Дилер в игре 'Блек-джек'."""

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрал.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """Игра в Блек-джек."""

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property # игроки в игре
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # сдача всем по 2 карты
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card() # первая из карт, сданных дилеру, переворачивается рубашкой вверх
        self.temporary_rate = []
        for player in self.players:
            if player.big_question() == 0: # если закончились деньги, то удаляем игрока
                self.players.remove(player)
        if len(self.players) != 0: # если игроков не осталось, то игра заканчивается
            for player in self.players:
                self.temporary_rate.append(player.question_rate())
                print(player)
            print(self.dealer)
            # сдача дополнительных карт игрокам
            for player in self.players:
                self.__additional_cards(player)
            self.dealer.flip_first_card() # первая карта дилера раскрывается
            if not self.still_playing:
                # все игроки перебрали, покажем только 'руку' дилера
                print(self.dealer)
            else:
                # сдача дополнительных карт дилеру
                print(self.dealer)
                self.__additional_cards(self.dealer)
                if self.dealer.is_busted():
                # выигрывают все, кто еще остался в игре
                    for player in self.still_playing:
                        player.win()
                else:
                # сравниваем суммы очков у дилера и у игроков, оставшихся в игре
                    for player in self.still_playing:
                        if player.total > self.dealer.total:
                            player.win()
                        elif player.total < self.dealer.total:
                            player.lose()
                        else:
                            player.push()
        else:
            print("Больше игроков нет, игра закончена!!!")
        # удаление всех карт
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("\t\tДобро пожаловать за игровой стол Блек-джека!\n")
    print("\t\tНа начало игры у каждого игрока по 100 баллов\n")
    names = []
    number = games.ask_number("Сколько всего игроков? (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nХотите сыграть еще раз? ")

main()
input("\n\nНажмите Enter, чтобы выйти.")
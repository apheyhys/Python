# Игра война
# От 2 до 7 игроков
# Игроки тянут по одной карты, а выигрывает тот, у кого номинал
# карты оказался наибольшим
import cards, games

class WR_Card(cards.Card):
    """Карта для игры в 'Войну'."""

    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = WR_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v


class WR_Deck(cards.Deck):
    """Колода для игры в 'Войну'."""

    def populate(self):
        for suit in WR_Card.SUITS:
            for rank in WR_Card.RANKS:
                self.cards.append(WR_Card(rank, suit))


class WR_Hand(cards.Hand):
    """Рука: набор карт у одного игрока."""

    def __init__(self, name):
        super(WR_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(WR_Hand, self).__str__()
        if self.total:
            rep += "номинал карты - " + str(self.total)
        return rep

    @property
    def total(self):
        t = 0
        for card in self.cards:
            t += card.value
        return t

    def is_busted(self):
        return self.total


class WR_Player(WR_Hand):
    """Игрок в 'Блек-джек'."""
    def lose(self):
        print(self.name, "проиграл.")


    def win(self):
        print(self.name, "выиграл.")


class WR_Game(object):
    """Игра в Блек-джек."""

    def __init__(self, names):
        self.players = []
        for name in names:
            player = WR_Player(name)
            self.players.append(player)
        self.deck = WR_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        # сдача всем по 1 карте
        self.deck.deal(self.players, per_hand=1)
        self.table_records = []
        for player in self.players:
            print(player)
            self.table_records.append(player.is_busted())
        self.table_records.sort(reverse=True) # сортируем обратным порядком
        for player in self.players:
            # если у игрока номинал карты равен максимальному номиналу, то он выиграл
            if player.total == self.table_records[0]:
                player.win()
            # если у игрока номинал карты меньше максимального номинала, то он проиграл
            elif player.total < self.table_records[0]:
                player.lose()
        # удаление всех карт
        for player in self.players:
            player.clear()


def main():
    print("\t\tДобро пожаловать за игровой стол гры 'Война'!\n")
    print("\t\tВыиграет тот, у кого будет карта с наибольшим номиналом!\n")
    names = []
    number = games.ask_number("Сколько всего игроков? (2 - 7): ", low=2, high=8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name)
        print()
    game = WR_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nХотите сыграть еще раз? ")

main()
input("\n\nНажмите Enter, чтобы выйти.")
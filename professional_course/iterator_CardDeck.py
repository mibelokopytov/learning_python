class CardDeck():
    def __init__(self):
        suit = ('пик', 'треф', 'бубен', 'червей')
        number = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
        self.deck = iter(f'{i} {j}' for j in suit for i in number)
    def __iter__(self):
        return self

    def __next__(self):
        return next(self.deck)
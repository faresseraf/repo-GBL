#! python
'''LOTO'''
import random

class Karta:
    bochka = [x for x in range(1, 91)]
    def __init__(self, user=None):
        self.user = user

    def __str__(self):
        print(self.user)
        print('-' * 8, 'ВАША КАРТОЧКА', '-' * 8)
        print(self.user, '\n', '-' * 26)
        # print()
        print('-' * 26)
        pass

    def karta_game(self):
        rows_card = []
        num_card = [x for x in range(1, 91)]
        for i in range(3):
            row_karta = []
            for x in range(5):
                row_karta.append(num_card.pop(random.randint(0, len(num_card)-1)))
            row_karta.sort()
            # rows_card.append(list(row_karta))
            rows_card += row_karta
        # карточка готова
        return rows_card
user = Karta('Joker')
print(user)
# print(user.user)
user_ka = user.karta_game()
print(user_ka)

meschok = [x for x in range(1, 91)]
for t in range(35):
    egg = meschok.pop(random.randint(0, len(meschok)-1))
    # print(egg, end=' ')
    if egg in user_ka:
        user_ka[user_ka.index(egg)] = '-'
print()
print(user_ka)

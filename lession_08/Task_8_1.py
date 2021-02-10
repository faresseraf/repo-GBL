#! python
'''LOTO'''
import random

class Karta_game:
# """создание карточки игрока"""
    def __init__(self, user):
        self.user = user
        self.digit = [x for x in range(1, 21)]
        self.rows_card = []
        for i in range(3):
            row_karta = []
            for x in range(5):
                row_karta.append(self.digit.pop(random.randint(0, len(self.digit) - 1)))
            row_karta.sort()
            self.rows_card += row_karta

    # def __iter__(self):
    #     return self.rows_card

    def __str__(self):
        return ('\n' + ("-" * 5) + 'КАРТОЧКА ' + self.user
                + ("-" * 5) + '\n'
                + str(self.rows_card[:5]) + '\n'
                + str(self.rows_card[5:10]) + '\n'
                + str(self.rows_card[10:14]) + '\n'
                + ("-" * 26))



class Game:
# """игра"""
    def __init__(self, user1, user2):
        self.meschok = [x for x in range(1, 21)]
        self.u1 = user1
        self.u2 = user2

        while True:
            egg = self.meschok.pop(random.randint(0, len(self.meschok) - 1))
            print(self.u1)
            print(self.u2)
            print('выпал бочонок: ', egg, end=' ')
            change = input('Это число есть в ваше карте? введите y/n \n')
            if egg in self.u1:
                if 'y' == change:
                    self.u1[self.u1.index(egg)] = '-'
                elif 'n' == change:
                    print('да нету - проигрыш!')
                    break
            elif 'n' == change:
                continue

            if egg in self.u2:
                self.u2[self.u2.index(0)] = '-'






user = Karta_game('Joker')
comp = Karta_game("Computer")
user.
# first_game = Game(user, comp)
# print(first_game)

# Игра "Угадай число"

from random import randint

# class Game():
#     def __init__():
#         pass

def guess_number(self, number, bets, attempts, capital):
    self.number = number
    self.bets = bets
    self.attempts = attempts
    self.capital = capital
    attempts = 5
    capital = 2000

    print(f'Игра "Угадай число" ')

    while attempts ==0:
        print(f'Количество попыток: {self.attempts}')
        print(f'Ваш капитал: {self.capital}')
        chance = randint(0, 13)
        number = int(input("Отгадайте число от 0 до 12: "))
        bets = int(input("Ваши ставки: "))
        if number > capital:
            print(f'Ваши ставки превышают ваш капитал: {self.capital}')
        elif number <= capital:
            if chance == number:
                print(f' Вы выиграли: {self.bets*2}')
                capital = self.capital + bets

            elif chance != number:
                bets = 0
                print(f'Ответ неверный, вы потеряли свои ставки: {self.bets}')
                capital = self.capital - bets
            else:
                print(f'Неправильное число')

            self.attempts -= 1




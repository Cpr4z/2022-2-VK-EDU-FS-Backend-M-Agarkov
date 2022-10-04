"""Создание игры крестики-нолики с консольным вводом пользователем"""

import random
import pygame


class TicTacGame:
    """Реализация класса игры крестики-нолики"""
    size_block = 75
    margin = 15

    def __init__(self, amount: int, mode: str, who_starts: str):
        self.amount = amount
        self.end_of_game = False
        self.num_of_turn = 0
        self.dashbosrd = None
        self.mode = mode
        self.who_starts = who_starts
        self.turn = None
        self.board = []
        self.current_row = None
        self.current_col = None

    def draw(self, row, col):
        """Прорисовывает подаваемую на вход фигуру(либо крестик, либо нолик)"""
        green = (0, 255, 0)
        red = (255, 0, 0)
        if self.turn == 'x':
            pygame.draw.line(
                            self.dashbosrd, green,
                            (TicTacGame.margin * (col+1) + col * TicTacGame.size_block,
                             TicTacGame.margin * (row + 1) + row * TicTacGame.size_block),
                            (TicTacGame.margin * (col + 1) + (col + 1) * TicTacGame.size_block,
                             (TicTacGame.margin * (row + 1) + TicTacGame.size_block * (row + 1))), 5)

            pygame.draw.line(
                            self.dashbosrd, green,
                            (TicTacGame.margin * (col + 1) + col * TicTacGame.size_block,
                             TicTacGame.margin * (row + 1) + (row + 1) * TicTacGame.size_block),
                            (TicTacGame.margin * (col + 1) + (col + 1) * TicTacGame.size_block,
                             TicTacGame.margin * (row + 1) + TicTacGame.size_block * row), 5)
            self.board[self.current_row][self.current_col] = 'x'
            self.turn = 'o'
            self.num_of_turn += 1
            for i in self.board:
                print(i)
            print('\n')
            pygame.display.update()
        elif self.turn == 'o':
            self.board[self.current_row][self.current_col] = 'o'
            pygame.draw.circle(
                               self.dashbosrd, red, (TicTacGame.margin * (col + 1) +
                               col * TicTacGame.size_block + 0.5 * TicTacGame.size_block,
                               TicTacGame.margin * (row + 1) + row * TicTacGame.size_block +
                               0.5 * TicTacGame.size_block), TicTacGame.size_block * 0.5 - 3, 5)
            self.turn = 'x'
            for i in self.board:
                print(i)
            print('\n')
            self.num_of_turn += 1
            pygame.display.update()
        self.check_winner()
        if self.end_of_game:
            return

    def human_mode(self):
        """Логика режима человек - компьютер"""
        if self.end_of_game:
            return

        if self.who_starts == 'x':
            self.turn = 'x'
        else:
            self.turn = 'o'
        self.validate_input()
        if self.end_of_game:
            return

    def computer_mode(self):
        """Логика режима компьютер-компьютер"""
        if self.end_of_game:
            return
        if self.who_starts == 'x':
            self.turn = 'x'
        else:
            self.turn = 'o'
        self.computer_input()
        if self.end_of_game:
            return

    def computer_input(self):
        """Генерация компьютером случайных координат клеток"""
        self.current_row, self.current_col = random.randint(0, 2), random.randint(0, 2)
        if self.board[self.current_row][self.current_col] != 0:
            while self.board[self.current_row][self.current_col] != 0:
                self.current_row, self.current_col = random.randint(0, 2), random.randint(0, 2)
        print(self.current_row, self.current_col)
        self.draw(self.current_row, self.current_col)
        if self.end_of_game:
            return

    def validate_input(self):
        """Осуществляем ввод корректных координат полей"""
        try:
            self.current_row, self.current_col = \
                map(int, input("Введите координаты клетки:").split())
            if self.board[self.current_row][self.current_col] != 0:
                while self.board[self.current_row][self.current_col] != 0:
                    self.current_row, self.current_col = \
                        map(int, input("Введите координаты свободной клетки:").split())
        except ValueError:
            print('Повторите ввод')
        else:
            self.draw(self.current_row, self.current_col)
            if self.end_of_game:
                return

    def start_game(self):
        """Инициализируем доску в зависимости от того,
         какой ширины поле и какой режим игры"""
        try:
            if self.amount not in range(3, 6):
                raise ValueError('Размер поля должен быть в диапозоне от 3 до 5')
        finally:
            pass
        try:
            if self.who_starts not in ('x', 'o'):
                raise ValueError('Введите того, кто начинает игру')
        finally:
            pass
        try:
            if self.mode not in ('computer', 'human'):
                raise ValueError('Введите корректный режим игры')
        finally:
            pass

        width = height = TicTacGame.size_block * self.amount + (self.amount + 1) * TicTacGame.margin
        size_window = (width, height)
        self.dashbosrd = pygame.display.set_mode(size_window)
        pygame.display.set_caption("Крестики-нолики")
        white = (255, 255, 255)
        self.board = [[0] * self.amount for i in range(self.amount)]
        print(self.board)
        while not self.end_of_game:
            for row in range(self.amount):
                for col in range(self.amount):
                    x_coordinate = col * TicTacGame.size_block + (col + 1) * TicTacGame.margin
                    y_coordinate = row * TicTacGame.size_block + (row + 1) * TicTacGame.margin
                    pygame.draw.rect(self.dashbosrd, white, (x_coordinate, y_coordinate,
                                     TicTacGame.size_block, TicTacGame.size_block))
            pygame.display.update()
            if self.mode == 'human':
                self.human_mode()
                if self.end_of_game:
                    return
            elif self.mode == 'computer':
                self.computer_mode()
            else:
                while self.mode not in ('human', 'computer'):
                    self.mode = input('Введите корректный режим игры:')

    def make_choice(self, mas):
        """Функция проверяет наличие побеждной комбинации в подаваемом списке"""
        if mas.count('x') == 3:
            print('Крестики выиграли!')
            self.end_of_game = True
            return
        elif mas.count('o') == 3:
            print('Нолики выгирали!')
            self.end_of_game = True
            return
        return

    def check_winner(self):
        """Проверяем, кто из игроков выиграл"""
        if self.end_of_game:
            return
        if self.num_of_turn == self.amount**2:
            print('Ничья!!!')
            self.end_of_game = True
            return
        for i in self.board:
            self.make_choice(i)
            if self.end_of_game:
                return

        for x_coord in range(self.amount):
            list_of_col = []
            for y_coord in range(self.amount):
                list_of_col.append(self.board[y_coord][x_coord])
                self.make_choice(list_of_col)
                if self.end_of_game:
                    return
            # ищем победителя по диагонали
        list_of_diagonal = []
        for x_coord in range(self.amount):
            for y_coord in range(self.amount):
                if x_coord == y_coord:
                    list_of_diagonal.append(self.board[x_coord][y_coord])
                else:
                    continue
        self.make_choice(list_of_diagonal)
        if self.end_of_game:
            return
        list_of_diagonal.clear()
        for x_coord in range(self.amount - 1, -1, -1):
            for y_coord in range(self.amount - 1, -1, -1):
                if x_coord + y_coord == self.amount - 1:
                    list_of_diagonal.append(self.board[x_coord][y_coord])
        self.make_choice(list_of_diagonal)
        if self.end_of_game:
            return
        list_of_diagonal.clear()
        if self.mode == 'human':
            self.validate_input()
        else:
            self.computer_input()


if __name__ == '__main__':
    game = TicTacGame(amount=3, mode='computer', who_starts='x')
    game.start_game()

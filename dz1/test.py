"""Тесты для игры крестики-нолики"""

import unittest
from unittest import main
from main import TicTacGame


class TicTacGameTest(unittest.TestCase):
    """Класс тестирующий ошибки ввода пользователя"""

    def setUp(self):
        self.game = TicTacGame(38, 'human', 'x')

    def test_amount(self):
        """Проверка на то, что размер поля допустим"""
        with self.assertRaises(ValueError) as error:
            self.game.start_game()
        self.assertEqual('Размер поля должен быть в диапозоне от 3 до 5', error.exception.args[0])

    def test_who_starts(self):
        """Проверка на то, что на вход подается корректный символ, который начинает"""
        self.game.amount = 3
        self.game.who_starts = 'fsfsfs'
        with self.assertRaises(ValueError) as mistake:
            self.game.start_game()
        self.assertEqual('Введите того, кто начинает игру', mistake.exception.args[0])

    def test_mode(self):
        """Проверка того, что на вход подается корректный режим игры"""
        self.game.amount = 3
        self.game.who_starts = 'x'
        self.game.mode = 'fsfsfs'
        with self.assertRaises(ValueError) as fault:
            self.game.start_game()
        self.assertEqual('Введите корректный режим игры', fault.exception.args[0])


if __name__ == 'main':
    main()

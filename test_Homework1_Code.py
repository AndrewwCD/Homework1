from unittest import TestCase
from unittest import mock
import Homework1_Code
import random

class Test(TestCase):
    def test_player(self):
        for choice in ['R','P','S','L','V']:
            with mock.patch("builtins.input",return_value = choice):
                assert Homework1_Code.player() == choice

    def test_computer(self):
        for choice in ['R', 'P', 'S', 'L', 'V']:
            with mock.patch("random.choice", return_value = choice) as mock_random:
                computerChoice = Homework1_Code.computer()
                assert computerChoice == choice

    def test_game(self):
        with mock.patch("builtins.input", return_value = "R"):
            assert type(Homework1_Code.game()) is bool


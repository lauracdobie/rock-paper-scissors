import unittest
from app.models.player import Player
from app.models.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Dave", "scissors")
        self.player_2 = Player("Laura", "paper")
        
        self.game = Game(self.player_1, self.player_2)

    def test_game_has_player_1(self):
        self.assertEqual("Dave", self.game.player_1.name)

    def test_game_has_player_2(self):
        self.assertEqual("Laura", self.game.player_2.name)

    def test_game_player_1_has_choice(self):
        self.assertEqual("scissors", self.game.player_1.choice)

    def test_game_player_2_has_choice(self):
        self.assertEqual("paper", self.game.player_2.choice)

    # def test_scissors_beat_paper(self):

        
        
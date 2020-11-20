import unittest
from app.models.player import Player
from app.models.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Dave", "scissors")
        self.player_2 = Player("Laura", "paper")
        
        self.game = Game("Rock Paper Scissors")

    def test_game_has_name(self):
        self.assertEqual("Rock Paper Scissors", self.game.name)

    # def test_scissors_beat_paper(self):
    #     self.game.rock_paper_scissors(self.player_1, self.player_2):


        
        
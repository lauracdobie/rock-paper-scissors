import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_has_name(self):
        player_1 = Player("player 1", "rock")

        self.assertEqual("player 1", player_1.name)

    def test_player_has_choice(self):
        player_1 = Player("player 1", "rock")

        self.assertEqual("rock", player_1.choice)


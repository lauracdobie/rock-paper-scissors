import unittest
from app.models.player import Player

class TestPlayer(unittest.TestCase):

    def test_player_has_name(self):
        player1 = Player("player 1", "rock")

        self.assertEqual("player 1", player1.name)

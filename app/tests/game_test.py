import unittest
from app.models.player import Player
from app.models.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_1 = Player("Dave", "scissors")
        self.player_2 = Player("Laura", "paper")
        self.player_3 = Player("Chiara", "rock")
        self.player_4 = Player("Wayne", "rock")
        
        self.game1 = Game(self.player_1, self.player_2)
        self.game2 = Game(self.player_1, self.player_3)
        self.game3 = Game(self.player_2, self.player_3)
        self.game4 = Game(self.player_3, self.player_4)

    def test_game_has_player_1(self):
        self.assertEqual("Dave", self.game1.player_1.name)

    def test_game_has_player_2(self):
        self.assertEqual("Laura", self.game1.player_2.name)

    def test_scissors_beat_paper(self):
        winner = self.game1.play_rock_paper_scissors()

        self.assertEqual("Dave", winner.name)

    def test_rock_beats_scissors(self):
        winner = self.game2.play_rock_paper_scissors()

        self.assertEqual("Chiara", winner.name)

    def test_paper_beats_rock(self):
        winner = self.game3.play_rock_paper_scissors()

        self.assertEqual("Laura", winner.name)

    def test_same_choice_returns_none(self):
        winner = self.game4.play_rock_paper_scissors()

        self.assertIsNone(winner)



        
        
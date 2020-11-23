from app.models.player import Player
from random import choice

class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_rock_paper_scissors(self):
        if self.player_1.choice == "paper" and self.player_2.choice == "rock":
            return self.player_1
        elif self.player_2.choice == "paper" and self.player_1.choice == "rock":
            return self.player_2

        elif self.player_1.choice == "scissors" and self.player_2.choice == "paper":
            return self.player_1
        elif self.player_2.choice == "scissors" and self.player_1.choice == "paper":
            return self.player_2

        elif self.player_1.choice == "rock" and self.player_2.choice == "scissors":
            return self.player_1
            
        elif self.player_2.choice == "rock" and self.player_1.choice == "scissors":
            return self.player_2

        elif self.player_1.choice == self.player_2.choice:
            return None

    def generate_computer_player(self, player_2):
        weapons = ["rock", "paper", "scissors"]
        random_weapon = choice(weapons)
        player_2.choice = random_weapon





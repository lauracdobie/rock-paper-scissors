from app.models.player import Player

class Game():
    def __init__(self, name):
        self.name = name

    # def play_rock_paper_scissors(self, player_1, player_2):
    #     if player_1.choice == "paper" and player_2.choice == "rock":
    #         return player_1
    #     elif player_2.choice == "paper" and player_1.choice == "rock"
    #         return player_2

    #     elif player_1.choice == "scissors" and player_2.choice == "paper":
    #         return player_1
    #     elif player_2.choice == "scissors" and player_1.choice == "paper"
    #         return player_2

    #     elif player_1.choice == "rock" and player_2.choice == "scissors":
    #         return player_1
    #     elif player_2.choice == "rock" and player_1.choice == "scissors"
    #         return player_2

    #     elif player_1.choice == player_2.choice:
    #         return None


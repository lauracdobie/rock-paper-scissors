# from app.models.player import Player

class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    # def rock_paper_scissors(self, player_1, player_2):
    #     "paper" > "rock"
    #     "scissors" > "paper"
    #     "rock" > "scissors"
    #     if self.player_1.choice > self.player_2.choice:
    #         return player_1
    #     elif self.player_2.choice > self.player_1.choice:
    #         return player_2
    #     else:
    #         return None


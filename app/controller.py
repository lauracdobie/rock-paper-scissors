from flask import render_template, request, redirect
from app import app
from app.models.player import Player
from app.models.game import *

@app.route('/')
def test():
    return "Boo!"

# @app.route('/<choice1>/<choice2>')

@app.route('/result')
def get_result():
    player_1 = Player("Owl", "scissors")
    player_2 = Player("Pussycat", "rock")

    current_game = Game(player_1, player_2)

    winner = current_game.play_rock_paper_scissors()

    if winner != None:
        result = f"{winner.name} is the winner!"
    else: 
        result = "It's a draw!"

    return render_template('result.html', choice1=player_1.choice, choice2=player_2.choice, player1name=player_1.name, player2name=player_2.name, title='Result', result=result)
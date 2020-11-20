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
    player_1 = Player("Owl", "rock")
    player_2 = Player("Pussycat", "scissors")

    winner = game.play_rock_paper_scissors(player_1, player_2)

    return render_template('result.html', choice1=player_1.choice, choice2=player_2.choice, title='Result')
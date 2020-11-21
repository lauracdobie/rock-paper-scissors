from flask import render_template, request, redirect
from app import app
from app.models.player import Player
from app.models.game import *
from random import choice

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

@app.route('/<choice1>/<choice2>')
def play_game(choice1, choice2):
    player_1 = Player("Owl", choice1)
    player_2 = Player("Pussycat", choice2)

    current_game = Game(player_1, player_2)

    winner = current_game.play_rock_paper_scissors()

    if winner != None:
        result = f"{winner.name} is the winner!"
    else: 
        result = "It's a draw!"

    return render_template('play.html', choice1=choice1, choice2=choice2, player1name=player_1.name, player2name=player_2.name, title='Result', result=result)

@app.route('/computer')
def play_computer():
    weapons = ["rock", "paper", "scissors"]
    random_weapon = choice(weapons)

    player_1 = Player("Owl", "scissors")
    player_2 = Player("Cyber Pussycat", random_weapon)

    current_game = Game(player_1, player_2)

    winner = current_game.play_rock_paper_scissors()

    if winner != None:
        result = f"{winner.name} is the winner!"
    else: 
        result = "It's a draw!"

    return render_template('play-computer.html', choice1=player_1.choice, choice2=player_2.choice, player1name=player_1.name, player2name=player_2.name, title='Result', result=result)

@app.route('/solo-play')
def solo_play():
    return render_template('single-player.html', title='Play the computer!')        
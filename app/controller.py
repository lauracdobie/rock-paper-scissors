from flask import render_template, request, redirect
from app import app
from app.models.player import Player
from app.models.game import *

@app.route('/')
def test():
    return "Boo!"
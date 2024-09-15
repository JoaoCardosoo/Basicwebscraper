from flask import Blueprint, render_template
import requests


views = Blueprint(__name__, "views")

@views.route('/')
def index():
    return render_template('index.html')

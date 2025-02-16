import sys, os, json
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests import post, get
from prog.user_info.user import User
from prog.api_interaction.querys import search
from flask import Flask, render_template, url_for, redirect, request, jsonify
from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify

app = Flask(__name__)

cursong = search()
cursong.get_random_song()

curUser = User("test", 20)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    curUser
    return render_template('index.html', access_token=os.getenv("ACCESS_TOKEN"))

def index():
    return render_template('index.html') 

@app.route('/likeButton', methods=['POST'])
def like_button():
    print("Help me")
    return jsonify({'message': 'Success'})

@app.route('/skipsong', methods=['POST'])
def skipsong():
    cursong.get_random_song()
    return redirect(url_for('index.html'))

@app.route('/play')
def play():
    pass

app.run(debug=True)
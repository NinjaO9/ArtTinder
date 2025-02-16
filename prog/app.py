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
#cursong.get_random_song()
curUser = User("","")
dummyUser = User("John","Johnsezky25")

if os.getenv("ACCESS_TOKEN") == None:
    print("No access token found.")
    exit()

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    global curUser
    curUser.change_name(request.form['username'])
    curUser.change_password(request.form['password'])
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update_song():
    data = request.get_json()
    #print(cursong.search_song_specific(data.get('title'), data.get('artist')))
    return jsonify({'message': 'Success'})

@app.route('/likeButton', methods=['POST'])
def like_button():
    data = request.get_json()
    curUser.like_song(data.get('title'), data.get('artist'), 'empty')
    dummyUser.like_song(data.get('title'), data.get('artist'), 'empty')
    return jsonify({'message': 'Success'})

@app.route('/SkipButton', methods=['POST'])
def skipsong():
    data = request.get_json()
    dummyUser.like_song(data.get('title'), data.get('artist'), 'empty')
    return jsonify({'message': 'Success'})

@app.route('/match',  methods=['POST'])
def match():
    curUser.display_liked_songs()
    commonSongs = curUser.compare_likes(dummyUser)
    dummyUser.display_liked_songs()
    print(commonSongs) # Proof of concept for being able to find matches between two users.
    return jsonify({'message': 'Success'})

@app.route('/play')
def play():
    pass

app.run(debug=True)
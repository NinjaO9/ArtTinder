import sys, os, json
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests import post, get
from prog.user_info.user import User
from prog.api_interaction.querys import search

def main():
    searchQ = search()
    newuser = User("John", 21)

    song = searchQ.get_random_song()
    newuser.like_song(song['name'], song['artists'][0]['name'], song['album']['name'])
    song = searchQ.get_random_song()
    newuser.like_song(song['name'], song['artists'][0]['name'], song['album']['name'])
    song = searchQ.get_random_song()
    newuser.like_song(song['name'], song['artists'][0]['name'], song['album']['name'])
    song = searchQ.get_random_song()
    newuser.like_song(song['name'], song['artists'][0]['name'], song['album']['name'])

    newuser.display_liked_songs()

    

if __name__ == "__main__":
    main()






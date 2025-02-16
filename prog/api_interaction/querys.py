import os, json
from dotenv import load_dotenv
from requests import post, get
from .artist import artist as dummyUser

load_dotenv()
class search:

    def __init__(self):
        self._token = os.getenv("ACCESS_TOKEN")
        self._url = "https://api.spotify.com/v1/search"
        self._headers = {
            "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}"
        }
        self._kwarg = ""
        self._type = ""
        self._params = {
            "q": f"{self._kwarg}",
            "type": f"{self._type}"
        }
        self._artists = []
        self._artistCount = -1
    
    def get_artist(self, Searched_Artist):  
        if self._artistCount != -1:
            print("No artists have been searched yet.")
            return
        self._kwarg = Searched_Artist
        self._type = "artist"
    
    def search_by_artist(self, Searched_Artist):
        self._kwarg = Searched_Artist
        self._type = "artist"
        self._params.update(q= self._kwarg, type= self._type)
        response = get(url=self._url, headers=self._headers, params=self._params).json()['artists']['items'][0]
        self._artists.append(dummyUser(response['name'], response['genres'][0]))
        return response

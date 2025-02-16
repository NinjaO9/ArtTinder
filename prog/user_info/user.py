from .liked import LikedMusic

class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._likedMusic = LikedMusic()

    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, Number of liked songs: {self._likedMusic.get_length()}"
    def change_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def change_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def like_song(self, title, artist, genre):
        self._likedMusic.add_song(title, artist, genre)

    def unlike_song(self, title):
        self._likedMusic.remove_song(title)

    def display_liked_songs(self): 
        self._likedMusic.display_songs()

    


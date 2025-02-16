
class artist:
    def __init__(self, name, genre, followers, picture):
        self._name = name
        self._genre = genre
        self._followers = followers
        self._picture = picture

    def __str__(self):
        return f"Name: {self._name}, Genre: {self._genre}"

    def get_name(self):
        return self._name

    def get_genre(self):
        return self._genre

    def change_name(self, name):
        self._name = name

    def change_genre(self, genre):
        self._genre = genre

    def display_artist(self):
        print(f"Name: {self._name}, Genre: {self._genre}, Followers: {self._followers}, Image: {self._picture}")
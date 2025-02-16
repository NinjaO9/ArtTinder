from .liked import LikedMusic

class User:

    def __init__(self, name, password):
        self._name = name
        self._password = password
        self._likedMusic = LikedMusic()

    def __str__(self):
        return f"Name: {self._name}, Password: {self._password}, Number of liked songs: {self._likedMusic.get_length()}"
    
    def change_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def change_password(self, password):
        self._password = password

    def get_age(self):
        return self._age

    def like_song(self, title, artist, genre):
        self._likedMusic.add_song(title, artist, genre)

    def unlike_song(self, title):
        self._likedMusic.remove_song(title)

    def display_liked_songs(self): 
        self._likedMusic.display_songs()

    def compare_likes(self, user2):
        Common_songs = []
        temp = user2._likedMusic.head
        current_self = self._likedMusic.head
        while current_self:
            print("djaidwjoajd")
            current_user2 = temp
            while current_user2:
                if current_self.title == current_user2.title:
                    Common_songs.append(current_self.title)
                    break  
                current_user2 = current_user2.next
            
            current_self = current_self.next
        
        return Common_songs


    


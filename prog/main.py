import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests import post, get, put, delete
from prog.user_info.user import User

def signup():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return User(name, age)

def main():
    user = signup()
    user.like_song("Song1", "Artist1", "Genre1")
    user.like_song("Song2", "Artist2", "Genre2")
    user.like_song("Song3", "Artist3", "Genre3")
    user.display_liked_songs()
    user.unlike_song("Song2")
    user.display_liked_songs()

    print(user.__str__())


if __name__ == "__main__":
    main()






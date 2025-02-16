import os, sys
# Add the path to the 'user_info' directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../user_info'))

from user_info import User

class ButtonInputs:
    def __init__(self):
        self._user = User()
        self._button = None

    def like_button(self):
        self.user.like_song() # add song to liked songs

    def dislike_button(self):
        pass # get next song
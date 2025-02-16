
class Song:
    def __init__(self, title, artist, genre):
        self.prev = None
        self.title = title
        self.artist = artist
        self.genre = genre
        self.next = None

class LikedMusic:

    def __init__(self):
        self.head = None
        self._length = 0

    def add_song(self, title, artist, genre):
        new_song = Song(title, artist, genre)
        if self.head is None:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
            new_song.prev = current
        self._length += 1

    def remove_song(self, title):
        current = self.head
        while current:
            if current.title == title:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                break
            current = current.next
        self._length -= 1

    def display_songs(self):
        current = self.head
        while current:
            print(f"{current.title} by {current.artist} - {current.genre}")
            current = current.next

    def get_length(self):
        return self._length
    
    

    

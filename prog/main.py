import sys, os, json
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests import post, get
from prog.user_info.user import User

def main():
    artistID = "0TnOYISbd1XYRBk9myaseg"
    #url = f"https://api.spotify.com/v1/artists/{artistID}"
    url = f"https://api.spotify.com/v1/search"
    Searched_Artist = input("Enter the name of the artist you want to search: ")
    headers={
        "Authorization": f"Bearer {os.getenv("ACCESS_TOKEN")}"
    }
    params = {
        "q": f"{Searched_Artist}",
        "type" : "artist"
    }
    

    response = get(url=url, headers=headers, params=params).json()

    print(response['artists']['items'])
    

if __name__ == "__main__":
    main()






import sys, os, json
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests import post, get
from prog.user_info.user import User
from prog.api_interaction.querys import search

def main():
    searchQ = search()
    Searched_Artist = input("Enter the name of the artist you want to search: ")
    
    print(searchQ.search_by_artist(Searched_Artist=Searched_Artist))
    

if __name__ == "__main__":
    main()






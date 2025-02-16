import sys, os, json
from dotenv import load_dotenv
from flask import Flask, render_template
load_dotenv()

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from requests import post, get
from prog.user_info.user import User
from prog.api_interaction.querys import search







def main():
    searchQ = search()
    Searched_Artist = input("Enter the name of the artist you want to search: ")
    searchQ.search_by_artist(Searched_Artist=Searched_Artist)

    searchQ._artists[0].display_artist()
    




app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello bruh'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == "__main__":
    app.run(debug=True)






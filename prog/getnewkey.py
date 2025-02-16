from dotenv import load_dotenv
from requests import post
import os

# Not a part of the proper program, rather this is a way to refresh our key, should it expire.

load_dotenv()

data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET")
    }

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
response = post(url="https://accounts.spotify.com/api/token", headers=headers, data=data)

print(response.json())
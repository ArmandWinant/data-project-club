import json
import requests
import os
from pathlib import Path

class SpotifyAPIClient:
    def __init__(self, credentials_file):
        credentials_dir = os.path.join(Path.home(), f"Desktop/Projects/data-project-club/2_spotify_wrapped", credentials_file)
        self.get_credentials(credentials_dir)
        
    def get_credentials(self, file_dir):
        try:
            with open(file_dir, "r") as file:
                self.credentials = json.load(file)
        except FileNotFoundError:
            print(f"Could not find credenials file: {file_dir}")
            
    def get_access_token(self):
        url = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self.credentials['client-id'],
            "client_secret": self.credentials['client-secret']
        }
        
        r = requests.post(url, data=data, headers=headers)
        
        if r.status_code == 200:
            r_json = r.json()
            return r_json
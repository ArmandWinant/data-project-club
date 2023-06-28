import warnings
warnings.filterwarnings('ignore') # setting ignore as a parameter

from src.auth_utils import login
from pathlib import Path
import os
import json
import requests

class Extractor:
    def __init__(self):
        self.project_dir = os.path.join(Path.home(), f"Desktop/Projects/data-project-club/2_spotify_wrapped")
        self.get_credentials()
    
    def get_credentials(self):
        credentials_file = os.path.join(self.project_dir, "secrets/spotify_credentials.json")
        try:
            with open(credentials_file, "r") as file:
                self.credentials = json.load(file)
        except FileNotFoundError:
            print(f"Could not find credenials file: {file_dir}")
            
    def get_access_token(self):
        config = self.credentials.copy()
        
        config["auth_uri"] = "https://accounts.spotify.com/authorize"
        config["token_uri"] = "https://accounts.spotify.com/api/token"
        config["scopes"] = ["user-top-read", "user-read-private"]
                
        access_token = login(config)
        
        self.headers = {"Authorization": f"Bearer {access_token}"}
    
    def get_request(self, endpoint):
        r = requests.get(endpoint, headers=self.headers)
        print(r.status_code)
        if r.status_code == 200:
            return r.json()
    
    def get_user_profile(self):
        endpoint = "https://api.spotify.com/v1/me"
        return self.get_request(endpoint)
    
    def get_top_artists(self):
        endpoint = f"https://api.spotify.com/v1/me/top/artists?time_range=medium_term&limit=50&offset=0"
        return self.get_request(endpoint)
    
    def get_top_tracks(self):
        endpoint = f"https://api.spotify.com/v1/me/top/tracks?time_range=medium_term&limit=50&offset=0"
        return self.get_request(endpoint)
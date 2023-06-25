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
            self.access_token = r.json()
    
    def api_request(self, url, *args, **kwargs):
        # TODO: verify that the access token is defined
        try:
            headers = {"Authorization": f"{self.access_token['token_type']} {self.access_token['access_token']}"}
            artist_data = request.get(url, headers=headers)
        except AttributeError:
            print("SpotifyAPIClient.api_request(): Access Token was not generated (call SpotifyAPIClient.get_access_token())")
            return
        return artist_data
    
#     def get_artist_info(self, artist_id):
#         url = "https://api.spotify.com/v1/artists/6rqlONGmPuP2wJVSfliLBI"
#         headers = {"Authorization": f"{sc.access_token['token_type']} {sc.access_token['access_token']}"}
#         artist_data = requests.get(url, headers=headers)
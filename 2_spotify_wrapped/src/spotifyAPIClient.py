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
            access_token = r.json()
            r.close()
            self.headers = {"Authorization": f"{access_token['token_type']} {access_token['access_token']}"}
    
    def api_request(self, url, *args, **kwargs):
        try:
            r = requests.get(url, headers=self.headers)
            if r.status_code == 200:
                data = r.json()
                r.close()
                return data
        except AttributeError:
            print("SpotifyAPIClient.api_request(): Access Token was not generated (call SpotifyAPIClient.get_access_token())")
            return
        # TODO: throw except when the access token has expired
        return
    
#     def get_artist_info(self, artist_id):
#         url = "https://api.spotify.com/v1/artists/6rqlONGmPuP2wJVSfliLBI"
#         headers = {"Authorization": f"{sc.access_token['token_type']} {sc.access_token['access_token']}"}
#         artist_data = requests.get(url, headers=headers)
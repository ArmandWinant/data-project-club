import json
import requests
import os
from pathlib import Path
import logging

class SpotifyAPIClient:
    def __init__(self, credentials_file):
        self.project_dir = os.path.join(Path.home(), f"Desktop/Projects/data-project-club/2_spotify_wrapped")
        
        credentials_dir = os.path.join(self.project_dir, credentials_file)
        self.get_credentials(credentials_dir)
        
        try:
            tmp_data_dir = os.path.join(self.project_dir, "tmp")
            os.mkdir(tmp_data_dir)
        except FileExistsError as e:
            pass
        
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
            token_info = r.json()
            self.headers = {"Authorization": f"{token_info['token_type']} {token_info['access_token']}"}
            r.close()
    
    def api_request(self, url, headers=None):
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                data = r.json()
                r.close()
                return data
        except AttributeError:
            print("SpotifyAPIClient.api_request(): Access Token was not generated (call SpotifyAPIClient.get_access_token())")
            return
        r.close()
        return
    
    def store_data(self, data, filename):
        file_dir = os.path.join(self.project_dir, f"tmp/{filename}.json")
        
        json_data = json.dumps(data, indent=4)
        
        with open(file_dir, "w") as outfile:
            outfile.write(json_data)
        
        
    def get_user_info(self):
        url = f"https://api.spotify.com/v1/users/31jetuno3fq5jswe3glemlzm3hwu"
        data = self.api_request(url, self.headers)
        
        self.store_data(data, "user_info")
    
    def get_artist_info(self, artist_id="6rqlONGmPuP2wJVSfliLBI"):
        url = f"https://api.spotify.com/v1/artists/{artist_id}"
        data = self.api_request(url, self.headers)
        
        self.store_data(data, "artist_info")
    
    
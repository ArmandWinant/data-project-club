import json
import requests

def get_credentials():
    creds_dict = {}
    with open("credential.json", "r") as file:
        creds_dict = json.load(file)
    
    return creds_dict


def get_access_token():
    credentials = get_credentials()
    
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": credentials['client-id'],
        "client_secret": credentials['client-secret']
    }
    
    r = requests.post(url, data=data, headers=headers)
    
    if r.status_code == 200:
        r_json = r.json()
        token_type = r_json["token_type"]
        access_token = r_json["access_token"]
        
        return access_token, token_type
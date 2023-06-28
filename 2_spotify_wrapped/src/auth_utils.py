import warnings
warnings.filterwarnings('ignore') # setting ignore as a parameter
import pkce
import base64
import requests
import random
import string
from typing import Any
import webbrowser
from oauthlib.oauth2 import WebApplicationClient

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse

class OAuthHttpServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        HTTPServer.__init__(self, *args, **kwargs)
        self.authorization_code = ""


class OAuthHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write("<script type=\"application/javascript\">window.close();</script>".encode("UTF-8"))
        
        parsed = parse.urlparse(self.path)
        qs = parse.parse_qs(parsed.query)
        
        self.server.authorization_code = qs["code"][0]
        
        
def generate_code() -> tuple[str, str]:
    code_verifier = pkce.generate_code_verifier(length=128)
    code_challenge = pkce.get_code_challenge(code_verifier)

    return (code_verifier, code_challenge)

        
def login(config: dict[str, Any]) -> str:
    with OAuthHttpServer(('', config["port"]),OAuthHttpHandler) as httpd:
        client = WebApplicationClient(config["client_id"], response_type='code')
        code_verifier, code_challenge = generate_code()

        auth_uri = client.prepare_request_uri(
            config["auth_uri"],
            scope=config["scopes"],
            redirect_uri=config["redirect_uri"], 
            code_challenge=code_challenge,
            code_challenge_method = "S256")

        webbrowser.open_new(auth_uri)
        httpd.handle_request()
        
        auth_code = httpd.authorization_code

        data = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": config["redirect_uri"],
            "client_id": config["client_id"],
            "code_verifier": code_verifier
        }
        
        response = requests.post(config["token_uri"], data=data, verify=False)
        access_token = response.json()["access_token"]
        
    return access_token
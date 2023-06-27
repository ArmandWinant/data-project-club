from src.spotifyAPIClient import SpotifyAPIClient
from src.dataUploader import DataUploader

class SpotifyDataPipeline:
    def __init__(self, spotify_creds_file, aws_creds_file):
        self.sp_client = SpotifyAPIClient(spotify_creds_file)
        self.aws_client = DataUploader(aws_creds_file)
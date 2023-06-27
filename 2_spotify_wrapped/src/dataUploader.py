import boto3
import logging
import json
import os
from pathlib import Path
from botocore.exceptions import ClientError

class DataUploader:
    def __init__(self, credentials_file):
        credentials_dir = os.path.join(Path.home(), f"Desktop/Projects/data-project-club/2_spotify_wrapped", credentials_file)
        self.get_credentials(credentials_dir)
        
    def get_credentials(self, file_dir):
        try:
            with open(file_dir, "r") as file:
                credentials = json.load(file)
                self.s3_client = boto3.client('s3',
                                              aws_access_key_id=credentials["access-key"],
                                              aws_secret_access_key=credentials["secret-key"])
        except FileNotFoundError as e:
            logging.error(e)
        except ClientError as e:
            logging.error(e)
        
    def close_client(self):
        try:
            self.s3_client.close()
        except AttributeError as e:
            logging.error(e)
        except ClientError as e:
            logging.error(e)
        
    def createBucket(self, bucket_name="dpc-spotify-wrap-data", region="eu-central-1"):
        try:
            location = {"LocationConstraint": region}
            self.s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True
    
    def deleteBucket(self, bucket_name="dpc-spotify-wrap-data"):
        try:
            self.s3_client.delete_bucket(Bucket=bucket_name)
        except ClientError as e:
            logging.error(e)
            return False
import os

from dotenv import load_dotenv

from sftp_connection.connection.mock_sftp_client import MockSFTPClient
from sftp_connection.connection.sftp_client import SFTPClient


class SFTPFunctions:
    def __init__(self):
        load_dotenv()
        self.sftp_client = MockSFTPClient() if int(os.getenv('USE_MOCK')) else SFTPClient()

    def connect(self):
        self.sftp_client.connect()

    def close(self):
        self.sftp_client.close()

    def get(self, remote_path: str, local_path: str):
        self.sftp_client.get(remote_path, local_path)

    def put(self, remote_path: str, local_path: str):
        self.sftp_client.put(remote_path, local_path)

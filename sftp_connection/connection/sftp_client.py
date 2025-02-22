import os

import pysftp
from dotenv import load_dotenv

from sftp_connection.connection.interfaces.sftp_interface import SFTPInterface


class SFTPClient(SFTPInterface):
    def __init__(self):
        load_dotenv()
        self.hostname = os.getenv('SMTP_HOST')
        self.username = os.getenv('SMTP_USER')
        self.password = os.getenv('SMTP_PASSWORD')
        self.port = os.getenv('SMTP_PORT')
        self.connection = None

    def connect(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None  # Para ignorar verificação de chave (uso em testes)
        self.connection = pysftp.Connection(
            host=self.hostname, username=self.username, password=self.password, port=self.port, cnopts=cnopts
        )
        print("✅ Conectado ao SFTP!")

    def put(self, local_path: str, remote_path: str):
        self.connection.put(local_path, remote_path)
        print(f"📤 Arquivo {local_path} enviado para {remote_path}")

    def get(self, remote_path: str, local_path: str):
        self.connection.get(remote_path, local_path)
        print(f"📥 Arquivo {remote_path} baixado para {local_path}")

    def close(self):
        if self.connection:
            self.connection.close()
        print("🔌 Conexão SFTP fechada")

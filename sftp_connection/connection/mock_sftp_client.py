from unittest.mock import MagicMock

from sftp_connection.connection.interfaces.sftp_interface import SFTPInterface


class MockSFTPClient(SFTPInterface):
    def __init__(self):
        self.mock_sftp = MagicMock()
        print("⚡ Usando Mock SFTP")

    def connect(self):
        print("✅ Simulando conexão SFTP")

    def put(self, local_path: str, remote_path: str):
        print(f"📤 Simulando upload de {local_path} para {remote_path}")
        self.mock_sftp.put(local_path, remote_path)

    def get(self, remote_path: str, local_path: str):
        print(f"📥 Simulando download de {remote_path} para {local_path}")
        self.mock_sftp.get(remote_path, local_path)

    def close(self):
        print("🔌 Simulando fechamento da conexão SFTP")

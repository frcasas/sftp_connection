from abc import ABC, abstractmethod

class SFTPInterface(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def put(self, local_path: str, remote_path: str): pass

    @abstractmethod
    def get(self, remote_path: str, local_path: str): pass

    @abstractmethod
    def close(self): pass
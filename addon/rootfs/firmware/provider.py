from abc import ABC, abstractmethod


class FirmwareProvider(ABC):

    @abstractmethod
    def scan(self):
        pass

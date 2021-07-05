from abc import ABC, abstractmethod


class ConfigParser(ABC):
    @abstractmethod
    def parse(self): pass

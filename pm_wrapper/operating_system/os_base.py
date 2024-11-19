from abc import ABC, abstractmethod

from pm_wrapper.config.config import Config

class OperatingSystemBase(ABC):
    def __init__(self, config: Config):
        self.config = config

    @abstractmethod
    def default_package(self) -> str:
        pass

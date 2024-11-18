from abc import ABC, abstractmethod

from pm_wrapper.config.config import UserConfig

class OSBase(ABC):
    def __init__(self, config: UserConfig):
        self.config = config

    @abstractmethod
    def default_package(self) -> str:
        pass

from abc import ABC, abstractmethod
import argparse

class OptionBase(ABC):
    """
    Option base class
    """
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.__value: str | None = None


    @classmethod
    @abstractmethod
    def option_name(cls):
        pass

    def get_value(self):
        return self.__value

    def is_set(self):
        return self.get_value() is not None


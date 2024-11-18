from abc import abstractmethod
import argparse


class CommandBase:
    """
    Command base class.
    """

    COMMAND_NAME: str = ""

    def __init__(
        self,
        parser: argparse.ArgumentParser,
        args: argparse.Namespace
    ):
        self.parser: argparse.ArgumentParser = parser
        self.args: argparse.Namespace = args
        self.errors: list[str] = []

    @classmethod
    def command_name(cls) -> str:
        """
        Returns the command name.
        """
        if cls.COMMAND_NAME == "":
            raise NotImplementedError("COMMAND_NAME is not implemented")
        return cls.COMMAND_NAME

    @abstractmethod
    def parser(
        self,
        main_parser: argparse.ArgumentParser
    ) -> argparse.ArgumentParser:
        """
        Returns the command parser.
        """
        pass

    @abstractmethod
    def check(self):
        """
        Checks the validity of the command parameters.
        If an error is found, it exits with sys.exit(1).
        """
        pass

    def add_error(self, message: str):
        """
        Adds an error message.
        """
        self.errors.append(message)

    def print_error(self):
        """
        Prints an error message and exits with sys.exit(1).
        """
        for error in self.errors:
            print(f"Error: {error}")
        self.parser.print_usage()

    @abstractmethod
    def execute(self):
        """
        Executes the command.
        """
        pass

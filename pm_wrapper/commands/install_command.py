import argparse
import logging

from pm_wrapper.commands.command_base import CommandBase
from pm_wrapper.package_manager.package_manager_base import PackageManagerBase


logger = logging.getLogger(__name__)


class InstallCommand(CommandBase):
    """
    Install command.
    """

    COMMAND_NAME = "install"

    def __init__(self, parser, args):
        super().__init__(parser, args)
        self.subparsers: argparse.ArgumentParser | None = None

    def parser(self, main_parser) -> argparse.ArgumentParser:
        """
        Returns the command parser.
        """
        p = main_parser.add_parser("install", help="Install a package")
        # p.add_argument("-a", "--all", action="store_true", help="All packages")
        p.add_argument("-d", "--dry-run", action="store_true", help="Dry run")
        p.add_argument("-f", "--file", type=str, help="Target bundle file")
        p.add_argument("-h", "--help", action="help", help="Show help")
        p.add_argument("-q", "--quiet", action="store_true", help="Quiet mode")
        p.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
        # p.add_argument("-V", "--version", action="store_true", help="Show version")
        p.add_argument("-y", "--yes", action="store_true", help="Yes to all")

        p.add_argument("-t", "--target", type=str, help="Target package scope")
        p.add_argument("-p", "--package", type=str, help="Target package command")
        p.add_argument("--os", type="store_true", help="Target OS")
        self.subparsers = p
        return p

    def check_parameters(self) -> bool:
        """
        Checks the validity of the command parameters.
        """

        if self.args.all:
            if self.args.package is not None:
                self.add_error("--package cannot be specified when --all is specified")
            if self.args.file is not None:
                self.add_error("--file cannot be specified when --all is specified")
            if self.args.file is not None:
                self.add_error("--file cannot be specified when --all is specified")

        if self.args.file is not None and self.args.package is None:
            self.add_error("--package is required when --file is specified")

        return len(self.errors) == 0

    def execute(self, package_manager: PackageManagerBase, options: dict):
        """
        Executes the command.
        """
        package_manager.install_(self.args.package, self.args.file, self.args.all, self.args.dry_run)
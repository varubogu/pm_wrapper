import os
from pm_wrapper.package_manager.package_manager_base import PackageManagerBase


class BrewCommand(PackageManagerBase):
    """
    Brew command class
    """

    @classmethod
    def list_(cls, is_requested_only: bool = False):
        """
        List installed packages
        """
        command = ["brew", "list"]
        if is_requested_only:
            command.append("--requested-only")
        cls.execute(command)

    @classmethod
    def search_(cls, package_name):
        """
        Search for a package
        """
        command = ["brew", "search", package_name]
        cls.execute(command)

    @classmethod
    def install_(cls, package_name, yes=False):
        """
        Install a package
        """
        command = ["brew", "install"]
        if yes:
            command.append("-y")
        command.append(package_name)
        cls.execute(command)

    @classmethod
    def uninstall_(cls, package_name):
        """
        Uninstall a package
        """
        command = ["brew", "uninstall", package_name]
        cls.execute(command)

    @classmethod
    def update_(cls):
        """
        Update the package manager
        """
        command = ["brew", "upgrade"]
        cls.execute(command)

    @classmethod
    def upgrade_(cls, package_name, yes=False):
        """
        Upgrade a package
        """
        command = ["brew", "upgrade"]
        if yes:
            command.append("-y")
        command.append(package_name)
        cls.execute(command)

    @classmethod
    def import_(cls, bundle_file):
        """
        Import a package from a file
        """
        command = ["brew", "bundle", "install", "--file", bundle_file]
        cls.execute(command)

    @classmethod
    def export_(cls, bundle_file):
        """
        Export a package to a file
        """
        command = ["brew", "bundle", "dump", "--file", bundle_file]
        cls.execute(command)

    @classmethod
    def config_directory(cls) -> str:
        """
        Returns the configuration directory.
        """
        return os.path.join(os.getenv("HOME"), ".config", "brew")

    @classmethod
    def package_file_name(cls) -> str:
        return "Brewfile"

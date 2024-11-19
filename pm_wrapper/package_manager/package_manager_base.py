from abc import ABC
import logging
import subprocess

logger = logging.getLogger(__name__)

class PackageManagerBase(ABC):
    def execute(self, command: list[str]):
        try:
            command_str = '"{}"'.format('" "'.join(command))
            logger.info(f'Executing command: {command_str}')
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"An error occurred while executing the command: {e}")


    def update_(self, command: list[str]):
        """
        Update the package manager
        """
        raise NotImplementedError("PackageManagerBase")

    def upgrade_(self, command: list[str]):
        """
        Upgrade a package
        """
        raise NotImplementedError("PackageManagerBase")

    def install_(self, command: list[str]):
        """
        Install a package
        """
        raise NotImplementedError("PackageManagerBase")

    def uninstall_(self, command: list[str]):
        """
        Uninstall a package
        """
        raise NotImplementedError("PackageManagerBase")

    def search_(self, command: list[str]):
        """
        Search for a package
        """
        raise NotImplementedError("PackageManagerBase")

    def list_(self, command: list[str]):
        """
        List installed packages
        """
        raise NotImplementedError("PackageManagerBase")

    def info_(self, command: list[str]):
        """
        Get information about a package
        """
        raise NotImplementedError("PackageManagerBase")

    def import_(self, command: list[str]):
        """
        Import a package from a file
        """
        raise NotImplementedError("PackageManagerBase")

    def export_(self, command: list[str]):
        """
        Export a package to a file
        """
        raise NotImplementedError("PackageManagerBase")

    def config_(self, command: list[str]):
        """
        Configure the package manager
        """
        raise NotImplementedError("PackageManagerBase")

    def help_(self, command: list[str]):
        """
        Show help
        """
        raise NotImplementedError("PackageManagerBase")

    def version_(self, command: list[str]):
        """
        Show version
        """
        raise NotImplementedError("PackageManagerBase")

    def package_file_name(self) -> str:
        """
        Returns the package file name.
        """
        raise NotImplementedError("PackageManagerBase")

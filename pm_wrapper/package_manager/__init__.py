import pathlib
from typing import Optional
from pm_wrapper.package_manager.package_manager_base import PMCommandBase
from pm_wrapper.package_manager.brew import BrewCommand

__all__ = [
    BrewCommand,
]

def find_pm_command(command_name: str) -> Optional[PMCommandBase]:
    """
    Finds the PM command.
    """
    for command in __all__:
        if command.command_name() == command_name:
            return command
    return None

def find_pm_command_from_package_file(package_file_name: str) -> Optional[PMCommandBase]:
    """
    Finds the PM command from the package file.
    """
    for command in __all__:
        if command.package_file_name() == package_file_name:
            return command
    return None

def find_package_files(pwd: str) -> list[pathlib.Path]:
    """
    Finds the package files.
    """
    results = []
    for command in __all__:
        file_name = command.package_file_name()
        if file_name is not None:
            file_path = pathlib.Path(file_name)
            if file_path.exists():
                results.append(file_path)
    return results

def find_package_files_to_commands(pwd: str) -> list[PMCommandBase]:
    """
    Finds the package files to the commands.
    """
    results: list[PMCommandBase] = []
    for command in __all__:
        file_name = command.package_file_name()
        if file_name is not None:
            file_path = pathlib.Path(file_name)
            if file_path.exists():
                results.append(command)
    return results

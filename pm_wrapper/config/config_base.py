
from abc import ABC
import os
import json

class ConfigBase(ABC):
    """
    Base class for configuration.
    """

    # config file name
    FILE_NAME: str = ""

    def __init__(self, config_dir: str):
        """
        Initialize configuration.
        """
        self.config_dir: str = config_dir

        # config json data
        self.data: dict = {}

    async def load(self):
        """
        Load configuration from file.
        """
        config_file: str = os.path.join(self.config_dir, self.FILE_NAME)
        with open(config_file, "r") as f:
            self.data = json.load(f)

    async def save(self):
        """
        Save configuration to file.
        """
        config_file: str = os.path.join(self.config_dir, self.FILE_NAME)
        with open(config_file, "w") as f:
            json.dump(self.data, f)

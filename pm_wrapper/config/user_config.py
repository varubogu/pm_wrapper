from .config_base import ConfigBase

class UserConfig(ConfigBase):
    """
    Configuration for the user.
    """
    FILE_NAME = "user.json"

    def __init__(self, config_dir: str):
        super().__init__(config_dir)

    @property
    def command_available(self) -> str:
        if "command_available" in self.data:
            return self.data["command_available"]
        return "command -v {{command}} &> /dev/null"

    @command_available.setter
    def command_available(self, value: str):
        self.data["command_available"] = value

    @property
    def default_package(self) -> str:
        if "default_package" in self.data:
            return self.data["default_package"]
        return ""

    @default_package.setter
    def default_package(self, value: str):
        self.data["default_package"] = value

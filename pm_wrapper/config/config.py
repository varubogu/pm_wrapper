from pm_wrapper.config.config_base import ConfigBase

class Config(ConfigBase):
    """
    Configuration for the user.
    """
    FILE_NAME = "config.json"

    def __init__(self, config_dir: str):
        super().__init__(config_dir)

    @property
    def os_default_package(self) -> str:
        if "os_default_package" in self.data:
            return self.data["os_default_package"]
        return ""

    @os_default_package.setter
    def os_default_package(self, value: str):
        self.data["os_default_package"] = value

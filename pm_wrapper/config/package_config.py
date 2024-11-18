from .config_base import ConfigBase
class PackageConfig(ConfigBase):
    """
    Configuration for a package.
    """
    FILE_NAME = "package.json"

    def __init__(self, config_dir: str):
        super().__init__(config_dir)

    def get_value(self, key: str) -> str:
        """
        Get the value of a key.

        Args:
            key (str): The key to get the value of.

        Returns:
            str: The value of the key.
        """
        keys = key.split(".")
        obj = self._target_config(key, keys)
        if obj is None:
            return ""
        return obj[keys[-1]]


    def set_value(self, key: str, value: str):
        """
        Set the value of a key.

        Args:
            key (str): The key to set the value of.
            value (str): The value to set.
        """
        keys = key.split(".")
        obj = self._target_config(key, keys)
        if obj is None:
            return
        obj[keys[-1]] = value

    def _target_config(self, key: str, keys: list[str]) -> any:
        """
        Get the target configuration object.

        Args:
            key (str): The key to get the target configuration object of.
            keys (list[str]): The keys to get the target configuration object of.

        Returns:
            any: The target configuration object.
        """
        current_dict = self.data
        for i in range(len(keys) - 1):
            k = keys[i]
            current_dict = current_dict.get(k)
            if current_dict is None:
                return None
        return current_dict






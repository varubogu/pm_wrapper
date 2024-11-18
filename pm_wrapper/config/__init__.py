import os

from .config import Config

def load_config() -> Config:
    config_dir = config_dir_search()
    return Config(config_dir)

def config_dir_search() -> str:
    """
    Searches for the configuration directory.
    """

    # XDG Base Directory config_dir
    XDG_BASE_CONFIG_DIR = os.getenv("XDG_CONFIG_HOME")
    if not os.path.exists(XDG_BASE_CONFIG_DIR):
        return XDG_BASE_CONFIG_DIR

    HOME_DIR = os.getenv("HOME") or os.getenv("USERPROFILE")
    if HOME_DIR is None:
        raise RuntimeError("HOME or USERPROFILE is not set")
    if not os.path.exists(HOME_DIR):
        raise RuntimeError("HOME or USERPROFILE is not exists")

    # $HOME/.config
    HOME_CONFIG_DIR = os.path.join(HOME_DIR, ".config")
    if not os.path.exists(HOME_CONFIG_DIR):
        return HOME_CONFIG_DIR

    # $HOME/.pm_wrapper/config
    HOME_PM_WRAPPER_DIR = os.path.join(HOME_DIR, ".pm_wrapper", "config")
    if not os.path.exists(HOME_PM_WRAPPER_DIR):
        return HOME_PM_WRAPPER_DIR

    raise RuntimeError("Configuration directory not found")
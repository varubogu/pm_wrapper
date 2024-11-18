from .package_config import PackageConfig

class PackageDetailConfig():
    """
    Configuration for a package detail.
    """

    def __init__(self, parent_config: dict):
        self.parent_config: dict = parent_config


    @property
    def bundle_file(self) -> str:
        if "bundle_file" in self.data:
            return self.data["bundle_file"]
        return ""

    @bundle_file.setter
    def bundle_file(self, value: str):
        self.data["bundle_file"] = value


    @property
    def list_command(self) -> str:
        if "list_command" in self.data:
            return self.data["list_command"]
        return ""

    @list_command.setter
    def list_command(self, value: str):
        self.data["list_command"] = value


    @property
    def search_command(self) -> str:
        if "search_command" in self.data:
            return self.data["search_command"]
        return ""

    @search_command.setter
    def search_command(self, value: str):
        self.data["search_command"] = value


    @property
    def install_command(self) -> str:
        if "install_command" in self.data:
            return self.data["install_command"]
        return ""

    @install_command.setter
    def install_command(self, value: str):
        self.data["install_command"] = value


    @property
    def uninstall_command(self) -> str:
        if "uninstall_command" in self.data:
            return self.data["uninstall_command"]
        return ""

    @uninstall_command.setter
    def uninstall_command(self, value: str):
        self.data["uninstall_command"] = value


    @property
    def update_command(self) -> str:
        if "update_command" in self.data:
            return self.data["update_command"]
        return ""

    @update_command.setter
    def update_command(self, value: str):
        self.data["update_command"] = value


    @property
    def upgrade_command(self) -> str:
        if "upgrade_command" in self.data:
            return self.data["upgrade_command"]
        return ""

    @upgrade_command.setter
    def upgrade_command(self, value: str):
        self.data["upgrade_command"] = value

    @property
    def import_command(self) -> str:
        if "import_command" in self.data:
            return self.data["import_command"]
        return ""

    @import_command.setter
    def import_command(self, value: str):
        self.data["import_command"] = value


    @property
    def export_command(self) -> str:
        if "export_command" in self.data:
            return self.data["export_command"]
        return ""

    @export_command.setter
    def export_command(self, value: str):
        self.data["export_command"] = value

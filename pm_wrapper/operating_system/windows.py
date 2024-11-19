from pm_wrapper.operating_system.os_base import OperatingSystemBase


class Windows(OperatingSystemBase):
    def default_package(self) -> str:
        return "winget"

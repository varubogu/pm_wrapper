from pm_wrapper.operating_system.os_base import OperatingSystemBase


class Darwin(OperatingSystemBase):
    def default_package(self) -> str:
        return "brew"

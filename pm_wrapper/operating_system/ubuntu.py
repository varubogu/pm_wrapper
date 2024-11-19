from pm_wrapper.operating_system.os_base import OperatingSystemBase


class Ubuntu(OperatingSystemBase):
    def default_package(self) -> str:
        return "apt-get"


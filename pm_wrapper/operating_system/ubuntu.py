from pm_wrapper.operating_system.os_base import OSBase


class Ubuntu(OSBase):
    def default_package(self) -> str:
        return "apt-get"


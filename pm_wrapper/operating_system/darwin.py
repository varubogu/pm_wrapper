from pm_wrapper.operating_system.os_base import OSBase


class Darwin(OSBase):
    def default_package(self) -> str:
        return "brew"

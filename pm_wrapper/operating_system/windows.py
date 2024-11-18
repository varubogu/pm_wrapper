from pm_wrapper.operating_system.os_base import OSBase


class Windows(OSBase):
    def default_package(self) -> str:
        return "winget"

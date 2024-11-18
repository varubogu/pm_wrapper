from pm_wrapper.operating_system.os_base import OSBase


class FreeBSD(OSBase):
    """
    FreeBSD
    """

    def default_package(self) -> str:
        return "pkg"

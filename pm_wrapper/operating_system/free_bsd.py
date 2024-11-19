from pm_wrapper.operating_system.os_base import OperatingSystemBase


class FreeBSD(OperatingSystemBase):
    """
    FreeBSD
    """

    def default_package(self) -> str:
        return "pkg"

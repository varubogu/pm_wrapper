from pm_wrapper.operating_system.os_base import OperatingSystemBase


class OpenBSD(OperatingSystemBase):
    """
    OpenBSD
    """

    def default_package(self) -> str:
        return "pkg_add"

from pm_wrapper.operating_system.os_base import OSBase


class OpenBSD(OSBase):
    """
    OpenBSD
    """

    def default_package(self) -> str:
        return "pkg_add"

import os
from pm_wrapper.operating_system.os_base import OSBase
from pm_wrapper.operating_system.darwin import Darwin
from pm_wrapper.operating_system.ubuntu import Ubuntu
from pm_wrapper.operating_system.windows import Windows
from pm_wrapper.operating_system.free_bsd import FreeBSD
from pm_wrapper.operating_system.open_bsd import OpenBSD

__all__ = ["Darwin", "Ubuntu", "Windows", "FreeBSD", "OpenBSD"]

def get_os() -> OSBase:
    """
    Returns the OS.
    """
    os_name = os.uname().sysname
    if os_name == "Darwin":
        return Darwin()
    elif os_name == "Windows":
        return Windows()
    elif os_name == "Linux":
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release", "r") as f:
                os_release = f.read()
                if "Ubuntu" in os_release:
                    return Ubuntu()
    elif os_name == "FreeBSD":
        return FreeBSD()
    elif os_name == "OpenBSD":
        return OpenBSD()
    else:
        raise RuntimeError("Unknown OS: {}".format(os_name))
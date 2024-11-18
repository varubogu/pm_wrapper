from argparse import Namespace

from .all_option import AllOption
from .dry_run_option import DryRunOption
from .file_option import FileOption
from .force_option import ForceOption
from .help_option import HelpOption
from .os_option import OSOption
from .package_manager_option import PackageManagerOption
from .quiet_option import QuietOption
from .target_option import TargetOption
from .verbose_option import VerboseOption
from .version_option import VersionOption
from .yes_option import YesOption

__all__ = [
    AllOption,
    DryRunOption,
    FileOption,
    ForceOption,
    HelpOption,
    OSOption,
    PackageManagerOption,
    QuietOption,
    TargetOption,
    VerboseOption,
    VersionOption,
    YesOption,
]


def make_options(args: Namespace):
    options = []
    for option in __all__:
        if option.option_name() in args:
            options.append(option(args))
    return options

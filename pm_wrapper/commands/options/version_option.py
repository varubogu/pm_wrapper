from argparse import Namespace
from pm_wrapper.commands.options.option_base import OptionBase


class VersionOption(OptionBase):
    """
    Version option class
    """

    def __init__(self, args: Namespace):
        super().__init__(args)

    @classmethod
    def option_name(cls):
        return "version"

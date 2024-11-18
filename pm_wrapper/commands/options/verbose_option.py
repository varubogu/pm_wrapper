from argparse import Namespace
from pm_wrapper.commands.options.option_base import OptionBase


class VerboseOption(OptionBase):
    """
    Verbose option class
    """

    def __init__(self, args: Namespace):
        super().__init__(args)

    @classmethod
    def option_name(cls):
        return "verbose"

from argparse import Namespace
from pm_wrapper.commands.options.option_base import OptionBase


class QuietOption(OptionBase):
    """
    Quiet option class
    """

    def __init__(self, args: Namespace):
        super().__init__(args)

    @classmethod
    def option_name(cls):
        return "quiet"

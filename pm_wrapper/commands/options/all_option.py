from argparse import Namespace
from typing import override
from pm_wrapper.commands.options.option_base import OptionBase


class AllOption(OptionBase):
    """
    All option class
    """

    def __init__(self, args: Namespace):
        super().__init__(args)

    @classmethod
    def option_name(cls):
        return "all"

class UpdateCommand(CommandBase):
    """
    Update command.
    """

    COMMAND_NAME = "update"

    def __init__(self, parser, args):
        super().__init__(parser, args)

    def parser(self, main_parser) -> argparse.ArgumentParser:
        p = main_parser.add_parser("update", help="Update a package")
        p.add_argument("-p", "--package", type=str, help="Target package command")
        p.add_argument("-a", "--all", action="store_true", help="All packages")
        p.add_argument("-d", "--dry-run", action="store_true", help="Dry run")
        return p

    def check_parameters(self) -> bool:
        if self.args.all:
            if self.args.package is not None:
                self.add_error("--package cannot be specified when --all is specified")
            if self.args.file is not None:
                self.add_error("--file cannot be specified when --all is specified")

        if self.args.file is not None and self.args.package is None:
            self.add_error("--package is required when --file is specified")

        return len(self.errors) == 0

    def execute(self):
        print(f"update {self.args.package} {self.args.all} {self.args.dry_run}")

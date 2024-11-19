#!/usr/bin/env python3

import logging
import sys
import os
import argparse

from pm_wrapper import commands
from pm_wrapper.commands.options import make_options
from pm_wrapper import os_
from pm_wrapper.package_manager import find_pm_command, find_package_files_to_commands

logger = logging.getLogger(__name__)


def main():
    try:
        parser = argparse.ArgumentParser(description="Package management tool")

        subparsers = parser.add_subparsers(dest="command", required=True)


        # コマンドのパーサーを追加
        for command in commands.__all__:
            command.parser(subparsers)

        # コマンドのパース実行
        args = parser.parse_args()
        options = make_options(args)

        # サブコマンドを入力値から決定
        execute_command = None
        for command in commands:
            if args.command == command.command_name():
                execute_command = command(parser, args)
                break

        if execute_command is None:
            if args.command:
                # コマンド未入力なら通常のヘルプ
                logger.info("command is None")
                parser.print_help()
                sys.exit(0)
            else:
                # 存在しないコマンド
                logger.error("Unknown command: {}".format(args.command))
                parser.print_usage()
                sys.exit(1)

        if args.help:
            # コマンドのヘルプ
            subparsers.print_help()
            sys.exit(0)

        if not execute_command.check_parameters():
            execute_command.print_error()
            sys.exit(1)

        # パッケージ管理ツール未指定なら
        target_pm = args.package
        if args.package:
            target_pm = find_pm_command(args.package)
        else:

            target_os = os_.get_os()

            home_dir = os.path.expanduser("~")
            pwd = os.getcwd()

            if pwd == home_dir:
                # ホームディレクトリならOSデフォルトのパッケージ管理ツールを使用する
                target_pm = target_os.default_package()
            else:
                # ホームディレクトリ以外ならパッケージ管理ツールのファイルを探す
                pm_commands = find_package_files_to_commands(pwd)
                if len(pm_commands) == 0:
                    # それでもなければOSデフォルトのパッケージ管理ツールを使用する
                    target_pm = target_os.default_package()
                elif len(pm_commands) == 1:
                    target_pm = pm_commands[0]
                else:
                    raise RuntimeError("Multiple package files found")

        if target_pm is None:
            raise RuntimeError("Target package manager not found")

        return execute_command.execute(target_pm, args)

    except Exception as e:
        logger.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()

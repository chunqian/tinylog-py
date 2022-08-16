"""---------------------------------------------------------
    name: tinylog.py
    editor: shenchunqian
    created: 2022-08-16
---------------------------------------------------------"""

import sys

from pprint import PrettyPrinter

__all__ = ["tinylog"]

class Tinylog:
    def __init__(self, nonColor = False) -> None:
        self.nonColor = nonColor

    def debug(self, fmt, *args):
        prefix = "[\033[34mDEBUG\033[0m] "
        if self.nonColor == True:
            prefix = "[DEBUG] "
        self.print(prefix, fmt, *args)

    def warn(self, fmt, *args):
        prefix = "[\033[33mWARN\033[0m] "
        if self.nonColor == True:
            prefix = "[WARN] "
        self.print(prefix, fmt, *args)

    def info(self, fmt, *args):
        prefix = "[\033[36mINFO\033[0m] "
        if self.nonColor == True:
            prefix = "[INFO] "
        self.print(prefix, fmt, *args)

    def error(self, fmt, *args):
        prefix = "[\033[31mERROR\033[0m] "
        if self.nonColor == True:
            prefix = "[ERROR] "
        self.print(prefix, fmt, *args)

    def fatal(self, fmt, *args):
        prefix = "[\033[35mFATAL\033[0m] "
        if self.nonColor == True:
            prefix = "[FATAL] "
        self.print(prefix, fmt, *args)
        sys.exit()


    def print(self, prefix, fmt, *args):
        pretty_printer = PrettyPrinter()
        pretty_str = prefix
        single_tuple = fmt.split("{}")
        count = len(single_tuple)
        if single_tuple[count - 1] != "":
            count -= 1
        for idx, val in enumerate(single_tuple):
            if idx >= count:
                break
            pretty_str += val + pretty_printer.pformat(args[idx])
        print(pretty_str)

tinylog = Tinylog()

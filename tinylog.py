"""---------------------------------------------------------
    name: tinylog.py
    editor: shenchunqian
    created: 2022-08-16
---------------------------------------------------------"""

import sys
import re

from pprint import PrettyPrinter

__all__ = ["tinylog"]

class Tinylog:
    def __init__(self, nonColor = False) -> None:
        self.nonColor = nonColor

    def debug(self, *args):
        prefix = "[\033[34mDEBUG\033[0m] "
        if self.nonColor == True:
            prefix = "[DEBUG] "
        self.print(prefix, *args)

    def warn(self, *args):
        prefix = "[\033[33mWARN\033[0m] "
        if self.nonColor == True:
            prefix = "[WARN] "
        self.print(prefix, *args)

    def info(self, *args):
        prefix = "[\033[36mINFO\033[0m] "
        if self.nonColor == True:
            prefix = "[INFO] "
        self.print(prefix, *args)

    def error(self, *args):
        prefix = "[\033[31mERROR\033[0m] "
        if self.nonColor == True:
            prefix = "[ERROR] "
        self.print(prefix, *args)

    def fatal(self, *args):
        prefix = "[\033[35mFATAL\033[0m] "
        if self.nonColor == True:
            prefix = "[FATAL] "
        self.print(prefix, *args)
        sys.exit()

    def print(self, prefix, *args):
        fmt = ""
        if type(args[0]) != str:
            for idx in range(len(args)):
                fmt += "{}"
        else:
            if re.search("{}", args[0]) == None:
                for idx in range(len(args)):
                    fmt += "{}"
            else:
                fmt = args[0]
                args = args[1:len(args)]

        pretty_printer = PrettyPrinter()
        pretty_str = prefix
        single_tuple = fmt.split("{}")

        args_len = len(args)
        count = len(single_tuple) - 1
        for idx, val in enumerate(single_tuple):
            if idx >= count or idx >= args_len:
                break
            pretty_str += val + pretty_printer.pformat(args[idx])
        if count == 0:
            print(pretty_str + fmt)
        else:
            print(pretty_str)

tinylog = Tinylog()

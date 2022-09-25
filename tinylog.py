"""---------------------------------------------------------
    name: tinylog.py
    editor: shenchunqian
    created: 2022-08-16
---------------------------------------------------------"""

import sys
import re
import traceback

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

    def stack(self):
         traceback.print_stack()

    def expandToFront(self, *args):
        fmt_str = ""
        args_list = [""]
        args_list.extend(args)

        top = len(args)
        for idx in range(top):
            if idx == top - 1:
                fmt_str += "{}"
            else:
                fmt_str += "{}, "
        args_list[0] = fmt_str
        return tuple(args_list)

    def expandToEnd(self, *args):
        count = 0
        if type(args[0]) == str:
            s = args[0].split("{}")
            count = len(s) - 1

        args_list = list(args)
        diff_count = 0
        if len(args_list) - 1 < count:
            diff_count = count - (len(args_list) - 1)
        for idx in range(diff_count):
            args_list.append("not found!")
        return tuple(args_list)

    def print(self, prefix, *args):
        top = len(args)
        if top == 0:
            return
        if type(args[0]) != str:
            args = self.expandToFront(*args)
        else:
            if re.search("{}", args[0]) == None:
                args = self.expandToFront(*args)
            else:
                args = self.expandToEnd(*args)

        fmt = args[0]
        top = len(args)
        pretty_printer = PrettyPrinter()
        pretty_str = prefix
        format_tuple = fmt.split("{}")

        count = len(format_tuple)
        for idx in range(top):
            if idx >= count:
                break
            if idx > 0:
                pretty_str += pretty_printer.pformat(args[idx]) + format_tuple[idx]
            else:
                pretty_str += format_tuple[idx]
        print(pretty_str)

tinylog = Tinylog()

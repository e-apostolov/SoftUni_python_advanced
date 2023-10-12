import sys

from termcolor import colored, cprint

cprint("Hello World!", "red", attrs=["bold", "underline"], file=sys.stderr)

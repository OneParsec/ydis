#!/usr/bin/python3
# Coded by OneParsec
import sys

if sys.platform == 'linux':
    from core.shell_win import *
else:
    from core.shell import *

shell()

#!/usr/bin/env python

"""settings.py
Methods for common file IO and directory management operations
"""

global DATA_DIR
DATA_DIR = 'data/'


def fileManager(path, mode, output=''):

    with open(path, mode) as file:

        if mode == 'w' and output:
            file.write(output)

        elif mode == 'a' and output:
            file.write('\n' + output)

        elif mode == 'r':
            return file.read()

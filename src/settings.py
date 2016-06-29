#!/usr/bin/env python

from re import compile

"""settings.py
Methods for common file IO and directory management operations
"""

global DATA_DIR
DATA_DIR = 'data/'

filterPat = r'[\{\(\[].*?[\)\]\}/]'
filterRe = compile(filterPat)

moreFilterPat = r'^.*?\('
moreFilterRe = compile(moreFilterPat)

endPat = r'[\)\]\}]'
endRe = compile(endPat)


def fileManager(path, mode, output=''):

    with open(path, mode) as file:

        if mode == 'w' and output:
            file.write(output)

        elif mode == 'a' and output:
            file.write('\n' + output)

        elif mode == 'r':
            return file.read()

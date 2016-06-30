#!/usr/bin/env python

from re import compile

"""settings.py
Methods for common file IO and directory management operations
"""

global DATA_DIR
DATA_DIR = 'data/'

excludePat = r'[\{\(\[].*?[\)\]\}/\\]'
excludeRe = compile(excludePat)

moreFilterPat = r'^.*?\('
moreFilterRe = compile(moreFilterPat)

endPat = r'[\)\]\}\-\'\"\,:]'
endRe = compile(endPat)

whtSpacePat = r'\s+'
whtSpaceRe = compile(whtSpacePat)


def regexify(title):

    return whtSpaceRe.sub(
        ' ', endRe.sub(
            ' ', moreFilterRe.sub(
                '', excludeRe.sub(
                    '', title.lower()
                )
            )
        ).rstrip().lstrip()
    )


def fileManager(path, mode, output=''):

    with open(path, mode) as file:

        if mode == 'w' and output:
            file.write(output)

        elif mode == 'a' and output:
            file.write('\n' + output)

        elif mode == 'r':
            return file.read()

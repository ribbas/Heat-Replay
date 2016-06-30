#!/usr/bin/env python
"""settings.py
Methods for common file IO and directory management operations
"""

from re import compile

DATA_DIR = 'data/'

MXM_DIR = 'mxm/'
MSD_DIR = 'MillionSongSubset/'

RAW_DIR = DATA_DIR + '{file}.txt'

MXM = RAW_DIR.format(file=MXM_DIR + 'mxm_779k_matches')
FILTERED_MXM = RAW_DIR.format(file='mxm_filtered')

CHARTED = RAW_DIR.format(file='charted')
CHARTED_MXM = RAW_DIR.format(file='charted_mxm')
CHARTED_FAIL = RAW_DIR.format(file='charted_failed')

reCompiles = []


def compileTitleRe():

    rePats = [
        r'[\{\(\[].*?[\)\]\}/\\]',
        r'^.*?\(',
        r'[\)\]\}\-\'\"\,:]',
        r'\s+'
    ]

    reCompiles.extend([compile(pat) for pat in rePats])


def regexify(title):

    return reCompiles[3].sub(
        ' ', reCompiles[2].sub(
            ' ', reCompiles[1].sub(
                '', reCompiles[0].sub(
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

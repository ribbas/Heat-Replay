#!/usr/bin/env python
"""settings.py
Global variables and methods for Heat Replay
"""

from re import compile  # also used in the other scripts

# ----------------- Global directories ----------------- #

DATA_DIR = 'data/'  # main dir of all datasets

ARCHIVE_DIR = 'archive/'  # main dir of all archived datasets

MXM_DIR = ARCHIVE_DIR + 'mxm/'  # dir for all mxm datasets
MSD_DIR = ARCHIVE_DIR + 'MillionSongSubset/'  # dir for all MSD datasets

RAW_DIR = DATA_DIR + '{file}.txt'  # format for text dataset

MXM = RAW_DIR.format(
    file=MXM_DIR + 'mxm_779k_matches')  # index of all songs in mxm

MXM_PATH = RAW_DIR.format(file=MXM_DIR + 'mxm_dataset_test')  # test mxm

FILTERED_MXM = RAW_DIR.format(file='mxm_filtered')  # curtailed mxm index

FILTERED_MXM_RAW = RAW_DIR.format(
    file='mxm_filtered_raw')  # curtailed mxm index with track IDs

CHARTED = RAW_DIR.format(file=ARCHIVE_DIR + 'charted')  # songs that charted

CHARTED_MXM = RAW_DIR.format(
    file='charted_mxm')  # intersection of charted and mxm

CHARTED_TIDS = RAW_DIR.format(
    file='charted_tid')  # intersection of charted and mxm

CHARTED_FAIL = RAW_DIR.format(
    file='charted_failed')  # difference of charted and mxm

CURSE_PATH = RAW_DIR.format(
    file='google_twunter_lol')  # raw list of curse words by Google

CURSES = DATA_DIR + 'curses.json'  # indexed curse words

# ----------------- Global variables ----------------- #

sep = '<SEP>'  # delimiter for all datasets

# ----------------- Local variables ----------------- #

__reCompiles = []


# ----------------- Global methods ----------------- #

def compileTitleRe():
    """Generates and compiles regex patterns"""

    rePats = [
        r'[\{\(\[].*?[\)\]\}/\\]',
        r'^.*?\(',
        r'[\)\]\}\-\'\"\,:]',
        r'\s+'
    ]

    __reCompiles.extend([compile(pat) for pat in rePats])


def regexify(title):
    """Applies regular expression methods and trims whitespace to the specified
    format

    title: the string to be regexified
    """

    return __reCompiles[3].sub(  # replace multiple \s with one \s
        ' ', __reCompiles[2].sub(  # replace excess punctuations with one \s
            ' ', __reCompiles[1].sub(  # remove everything before '('
                '', __reCompiles[0].sub(  # remove everything between brackets
                    '', title.lower()  # convert to lower case first
                )
            )
        ).rstrip().lstrip()  # strip whitespace from beginning and end only
    )


def fileManager(path, mode, output=''):
    """Basic IO operations

    path: path of file
    mode: file access mode
    output: string output to write or append to file
    """

    with open(path, mode) as file:

        if mode == 'w' and output:
            file.write(output)

        elif mode == 'a' and output:
            file.write('\n' + output)

        elif mode == 'r':
            return file.read()

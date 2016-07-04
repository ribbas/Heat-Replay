#!/usr/bin/env python
"""settings.py
Global variables and methods for Heat Replay
"""

from re import compile  # also used in the other scripts


# ----------------- Global directories ----------------- #

DATA_DIR = 'data/'  # main dir of all datasets

FILE = '{file}.txt'  # file formats

ARCHIVE_DIR = DATA_DIR + 'archive/'  # main dir of all archived datasets
TRANS_DIR = DATA_DIR + 'transitional/'  # main dir of all transitional datasets
FINAL_DIR = DATA_DIR + 'final/'  # main dir of all final datasets

MXM_DIR = ARCHIVE_DIR + 'mxm/' + FILE  # dir for all mxm datasets
MSD_DIR = ARCHIVE_DIR + 'MillionSongSubset/' + FILE  # dir for all MSD datasets


# ----------------- Global file paths ----------------- #

ARCHIVE = ARCHIVE_DIR + FILE  # main dir of all archived datasets
TRANS = TRANS_DIR + FILE  # main dir of all transitional datasets
FINAL = FINAL_DIR + FILE  # main dir of all final datasets

# --------- Archived datasets --------- #

MXM_INDEX = MXM_DIR.format(
    file='mxm_779k_matches')  # index of all songs in mxm

MXM_PATH = MXM_DIR.format(file='mxm_dataset_test')  # test mxm

CURSE_PATH = ARCHIVE.format(
    file='google_twunter')  # raw list of curse words by Google

CHARTED = ARCHIVE.format(file='charted')  # songs that charted

CHARTED2 = ARCHIVE.format(file='charted2')  # songs that charted

# --------- Transitional datasets --------- #

FILTERED_MXM = TRANS.format(file='mxm_filtered')  # curtailed mxm index

FILTERED_MXM_RAW = TRANS.format(
    file='mxm_filtered_raw')  # curtailed mxm index with track IDs

CHARTED_MXM = TRANS.format(
    file='charted_mxm')  # intersection of charted and mxm

CHARTED_FAIL = TRANS.format(
    file='charted_failed')  # difference of charted and mxm

# --------- Final datasets --------- #

CHARTED_TIDS = FINAL.format(
    file='charted_tid')  # intersection of charted and mxm

CURSES = FINAL_DIR + 'curses.json'  # indexed curse words


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
            '', __reCompiles[1].sub(  # remove everything before '('
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


def sortSet(dataset):

    setName = set()

    with open(dataset) as lyricsFile:

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            setName.add(line)

    setName = ''.join(sorted(list(setName)))

    fileManager(dataset, 'w', setName)

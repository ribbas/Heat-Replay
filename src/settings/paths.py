from os.path import abspath

# ----------------- Global directories ----------------- #

DATA_DIR = abspath('../../data/')  # main dir of all datasets

FILE = '{file}.txt'  # file formats

ARCHIVE_DIR = \
    DATA_DIR + '/archive/'  # main dir of all archived datasets
TRANS_DIR = \
    DATA_DIR + '/transitional/'  # main dir of all transitional datasets
FINAL_DIR = \
    DATA_DIR + '/final/'  # main dir of all final datasets

MXM_DIR = \
    ARCHIVE_DIR + '/mxm/' + FILE  # dir for all mxm datasets

# ----------------- Global file paths ----------------- #

ARCHIVE = ARCHIVE_DIR + FILE  # main dir of all archived datasets
TRANS = TRANS_DIR + FILE  # main dir of all transitional datasets
FINAL = FINAL_DIR + FILE  # main dir of all final datasets

# --------- Archived datasets --------- #

MXM_INDEX = MXM_DIR.format(
    file='mxm_779k_matches')  # index of all songs in mxm

MXM_PATH = MXM_DIR.format(file='mxm_dataset_test')  # test mxm

CURSE_RAW = ARCHIVE.format(
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

BOW = FINAL.format(file='bow')  # bag of words version of the lyrics

URLS_FAILED = FINAL.format(
    file='urls_failed')  # urls for charted songs not in mxm

URLS_EXCESS = FINAL.format(
    file='urls_excess')  # urls for charted songs from 2011 - 2015

CHARTED_TIDS = FINAL.format(
    file='charted_tid')  # intersection of charted and mxm

CURSES = FINAL_DIR + 'curses.json'  # indexed curse words

# ----------------- Global variables ----------------- #

sep = '<SEP>'  # delimiter for all datasets

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
    ARCHIVE_DIR + 'mxm/' + FILE  # dir for all mxm datasets

URL_DIR = \
    TRANS_DIR + 'urls/' + FILE  # dir for all urls for scraping lyrics

LYRICS_DIR = \
    TRANS_DIR + 'lyrics/'  # dir for all scraped lyrics

RANGE1 = LYRICS_DIR + '1961-2010/' + \
    FILE  # dir for all scraped lyrics from 1961-2010

RANGE2 = LYRICS_DIR + '2011-2015/' + \
    FILE  # dir for all scraped lyrics from 2011-2015

# ----------------- Global file paths ----------------- #

ARCHIVE = ARCHIVE_DIR + FILE  # main dir of all archived datasets
TRANS = TRANS_DIR + FILE  # main dir of all transitional datasets
FINAL = FINAL_DIR + FILE  # main dir of all final datasets

# --------- Archived datasets --------- #

MXM_INDEX = MXM_DIR.format(
    file='mxm_779k_matches')  # index of all songs in mxm

MXM_TEST = MXM_DIR.format(file='mxm_dataset_test')  # test mxm

MXM_TRAIN = MXM_DIR.format(file='mxm_dataset_train')  # train mxm

MXM = MXM_DIR.format(file='mxm')  # cleaned mxm file

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

URLS_FAILED = URL_DIR.format(
    file='urls_failed')  # urls for charted songs not in mxm

URLS_EXCESS = URL_DIR.format(
    file='urls_excess')  # urls for charted songs from 2011 - 2015

QUEUE = URL_DIR.format(
    file='queue')  # urls for charted songs from 2011 - 2015

FAIL = URL_DIR.format(
    file='failed')  # urls for charted songs from 2011 - 2015

# --------- Final datasets --------- #

BOW = FINAL.format(file='bow')  # bag of words version of the lyrics

CHARTED_TIDS = FINAL.format(
    file='charted_tid')  # intersection of charted and mxm

CURSES = FINAL_DIR + 'curses.json'  # indexed curse words

# ----------------- Global variables ----------------- #

sep = '<SEP>'  # delimiter for all datasets

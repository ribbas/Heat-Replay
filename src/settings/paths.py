#!/usr/bin/env python

from os.path import abspath, exists

# ----------------- Global directories ----------------- #

DATA_DIR = abspath('../../data/')  # main dir of all datasets

if not exists(DATA_DIR):
    DATA_DIR = abspath('../../../data/')  # main dir of all datasets

FILE = '{file}.txt'  # file formats

ARCHIVE_DIR = DATA_DIR + '/archive/'  # archived datasets
FINAL_DIR = DATA_DIR + '/final/'  # final datasets
TRANS_DIR = DATA_DIR + '/transitional/'  # transitional datasets

# ----------------- Global file paths ----------------- #

FINAL = FINAL_DIR + FILE  # final datasets

# --------- Archived directories --------- #

CHARTED_DIR = ARCHIVE_DIR + 'charted/' + FILE  # charted datasets
CURSES_DIR = ARCHIVE_DIR + 'curses/' + FILE  # Google's list of curse words
MSD_DIR = ARCHIVE_DIR + 'msd/'  # MSD datasets
MSD_RAW_DIR = MSD_DIR + 'msd_raw/'  # raw MSD datasets
MXM_DIR = ARCHIVE_DIR + 'mxm/'  # mxm datasets
MXM_RAW_DIR = MXM_DIR + 'mxm_raw/' + FILE  # raw mxm datasets


# --------- Archived datasets --------- #

CHARTED_RAW = CHARTED_DIR.format(
    file='charted_raw')  # songs that charted from 1961-2010

CHARTED_RAW2 = CHARTED_DIR.format(
    file='charted_raw2')  # songs that charted from 2011-2015

CURSE_RAW = CURSES_DIR.format(
    file='google_twunter')  # Google's list of curse words

MSD_TID = (MSD_DIR + FILE).format(file='MSD_TID')  # tracks IDs from MSD

MSD_TID_YEAR = (MSD_DIR + FILE).format(
    file='msd_tid_year')  # tracks IDs and years from MSD

MSD_FILES = (MSD_DIR + FILE).format(file='msd_files')  # all file paths in MSD

MXM_INDEX = MXM_RAW_DIR.format(
    file='mxm_779k_matches')  # index of all songs in mxm

MXM_TEST = MXM_RAW_DIR.format(file='mxm_dataset_test')  # test mxm

MXM_TRAIN = MXM_RAW_DIR.format(file='mxm_dataset_train')  # train mxm

MXM = MXM_RAW_DIR.format(file='mxm')  # combined train and test set

MXM_TID = (MXM_DIR + FILE).format(file='mxm_tid')  # track IDs from MXM


# --------- Transitional directories --------- #

T_CHARTED_DIR = TRANS_DIR + 'charted/' + FILE  # charted datasets
T_LYRICS_DIR = TRANS_DIR + 'lyrics/'  # scraped lyrics
T_MXM_DIR = TRANS_DIR + 'mxm/' + FILE  # scraped lyrics
URL_DIR = T_LYRICS_DIR + 'urls/' + FILE  # urls for scraping lyrics
RANGE1 = T_LYRICS_DIR + '1961-2010/'  # scraped lyrics from 1961-2010
RANGE2 = T_LYRICS_DIR + '2011-2015/'  # scraped lyrics from 2011-2015

# --------- Transitional datasets --------- #

CHARTED_MXM = T_CHARTED_DIR.format(
    file='charted_mxm')  # intersection of charted and mxm

CHARTED_FAIL = T_CHARTED_DIR.format(
    file='charted_failed')  # difference of charted and mxm

URLS_FAILED = URL_DIR.format(
    file='urls_failed')  # urls for charted songs not in mxm

URLS_EXCESS = URL_DIR.format(
    file='urls_excess')  # urls for charted songs from 2011 - 2015

QUEUE = URL_DIR.format(file='queue')  # urls for range1 charted songs

FAIL = URL_DIR.format(file='failed')  # urls for range2 charted songs

FILTERED_MXM = T_MXM_DIR.format(file='mxm_filtered')  # titles from mxm

FILTERED_MXM_RAW = T_MXM_DIR.format(
    file='mxm_filtered_raw')  # titles and track IDs from mxm

# --------- Final datasets --------- #

BOW = FINAL.format(file='bow')  # bag of words version of the lyrics

CHARTED_TIDS = FINAL.format(
    file='charted_tid')  # intersection of charted and mxm track IDs

MSD_MXM = FINAL.format(file='MSD_mxm')  # intersection of charted and mxm

MORE0 = FINAL.format(file='more0')  # charted songs with lyrics

MORE1 = FINAL.format(file='more1')  # scraped charted songs with lyrics

CURSES = FINAL_DIR + 'curses.json'  # indexed curse words

FINAL_MXM = FINAL.format(file='final0')

# final charted set, mapped with lyrics and year
CHARTED = FINAL.format(file='charted')

# final uncharted set, mapped with lyrics and year
UNCHARTED = FINAL.format(file='uncharted')

FINAL_SET = FINAL_DIR + 'final.csv'  # final dataset

# ----------------- Global variables ----------------- #

sep = '<SEP>'  # delimiter for all datasets

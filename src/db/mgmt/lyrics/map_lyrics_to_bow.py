from os import listdir

from pandas import DataFrame as df

from context import *
from settings.filemgmt import fileManager
from settings.paths import sep
from settings.paths import RANGE1, BOW_RANGE1, BOW
from lyrics_to_bow import lyrics_to_bow


def readLyrics(dir):

    mxmBow = fileManager(BOW, 'r')
    mxmBowSplit = mxmBow.split(',')

    files = listdir(dir)[:2]

    newSet = []
    songLyrics = {}

    for lyrics in files:
        bow = lyrics_to_bow(fileManager(RANGE1 + lyrics, 'r'))
        for word, freq in bow.iteritems():
            if word in mxmBow:
                songLyrics[mxmBowSplit.index(word)] = freq
        newSet.append(songLyrics)
        songLyrics = {}

    print df(newSet)

if __name__ == '__main__':

    readLyrics(RANGE1)

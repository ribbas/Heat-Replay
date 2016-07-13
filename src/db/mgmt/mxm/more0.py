#!/usr/bin/env python

from context import *
from settings.filemgmt import fileManager
from settings.paths import CHARTED_TIDS, MXM, MORE0


def loadSet(fileName):

    setName = []
    charted = fileManager(CHARTED_TIDS, 'r')

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for line in lyricsFile:

            if line.split(',')[0] in charted:
                setName.append(
                    line.split(',')[0] + ',' + ','.join(line.split(',')[2:])
                )

    return setName


def exportSet():

    dataset = loadSet(MXM)

    splitLyrics = [row.split(',') for row in dataset]

    newSet = []

    for rows in splitLyrics:
        newSet.append(','.join(rows))

    return newSet

if __name__ == '__main__':

    newSet = exportSet()
    fileManager(MORE0, 'w', ''.join(newSet))

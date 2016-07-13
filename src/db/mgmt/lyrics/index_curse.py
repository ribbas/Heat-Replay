#!/usr/bin/env python

from collections import OrderedDict
from json import dump

from context import *
from settings.filemgmt import fileManager
from settings.paths import BOW, CURSE_RAW, CURSES


def bagOfCurse():

    curseFile = fileManager(CURSE_RAW, 'r')

    return filter(
        None, [word.partition(':')[0].strip().strip()
               for word in curseFile.split()[1:-1]
               if len(word) > 3 and any(char.isdigit() for char in word)]
    )


def intersectLists():

    curses = set(bagOfCurse())
    bagOfWords = fileManager(BOW, 'r')
    words = set(bagOfWords.split(','))

    return list(curses & words), bagOfWords.split(',')


def mapIndices():

    curses = intersectLists()[0]
    words = intersectLists()[1]

    return {
        curseWord: (words.index(curseWord) + 1) for curseWord in curses
    }


def dumpJSON():

    curseData = OrderedDict(sorted(mapIndices().items()))

    with open(CURSES, 'w') as outputJSON:
        dump(curseData, outputJSON)


if __name__ == '__main__':

    dumpJSON()

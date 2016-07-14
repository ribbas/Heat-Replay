#!/usr/bin/env python

from collections import OrderedDict
from json import dump

from nltk.corpus import stopwords

from context import *
from settings.filemgmt import fileManager
from settings.paths import BOW, CURSE_RAW, CURSES, STOPWORDS


def bagOfCurse():

    curseFile = fileManager(CURSE_RAW, 'r')

    return filter(
        None, [word.partition(':')[0].strip().strip()
               for word in curseFile.split()[1:-1]
               if len(word) > 3 and any(char.isdigit() for char in word)]
    )


def bagOfStopWords():

    return [str(word) for word in stopwords.words('english')]


def intersectLists(bagOfFeats):

    feat = set(bagOfFeats)
    bagOfWords = fileManager(BOW, 'r')
    words = bagOfWords.split(',')

    interesects = list(feat & set(words))

    return {
        intersectWord: (words.index(intersectWord) + 1)
        for intersectWord in interesects
    }


def dumpJSON(newFeats, path):

    newFeats = OrderedDict(sorted(intersectLists(newFeats).items()))

    with open(path, 'w') as outputJSON:
        dump(newFeats, outputJSON)


if __name__ == '__main__':

    curses = bagOfCurse()
    dumpJSON(curses, CURSES)

    stopWords = bagOfStopWords()
    dumpJSON(stopWords, STOPWORDS)

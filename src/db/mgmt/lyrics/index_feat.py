#!/usr/bin/env python

from collections import OrderedDict
from json import dump

from nltk.corpus import stopwords

from context import *
from settings.filemgmt import fileManager
from settings.paths import BOW, CURSE_RAW, CURSES, STOPWORDS, SYLLABLES


bagOfWords = fileManager(BOW, 'r')


def bagOfCurse():

    curseFile = fileManager(CURSE_RAW, 'r')

    return filter(
        None, [word.partition(':')[0].strip().strip()
               for word in curseFile.split()[1:-1]
               if len(word) > 3 and any(char.isdigit() for char in word)]
    )


def bagOfStopWords():

    return [str(word) for word in stopwords.words('english')]


def countSyllables(word):

    vowels = "aeiouy"
    numVowels = 0
    lastWasVowel = False

    for wc in word:
        foundVowel = False

        for v in vowels:
            if v == wc:
                if not lastWasVowel:
                    numVowels += 1  # don't count diphthongs
                foundVowel = lastWasVowel = True
                break
                # If full cycle and no vowel found, set lastWasVowel to false
        if not foundVowel:
            lastWasVowel = False

    # Remove es - it's "usually" silent (?)
    if (len(word) > 2 and word[-2:] == "es") or \
            (len(word) > 1 and word[-1:] == "e"):
        numVowels -= 1

    return numVowels


def bagOfSyllables():

    words = bagOfWords.split(',')

    success = {}

    for i in words:
        success[i] = countSyllables(i)

    return success


def convertToDict(featList):

    return OrderedDict(sorted(intersectLists(featList).items()))


def intersectLists(bagOfFeats):

    feat = set(bagOfFeats)
    # bagOfWords = fileManager(BOW, 'r')
    words = bagOfWords.split(',')

    interesects = list(feat & set(words))

    return {
        intersectWord: (words.index(intersectWord) + 1)
        for intersectWord in interesects
    }


def dumpJSON(newFeats, path):

    with open(path, 'w') as outputJSON:
        dump(newFeats, outputJSON)


if __name__ == '__main__':

    curses = bagOfCurse()
    curses = convertToDict(curses)
    dumpJSON(curses, CURSES)

    syllables = bagOfSyllables()
    dumpJSON(syllables, SYLLABLES)

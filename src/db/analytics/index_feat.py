#!/usr/bin/env python

from collections import OrderedDict
from json import dump

from nltk import pos_tag
from nltk.corpus import stopwords

from context import *
from settings.filemgmt import fileManager
from settings.paths import ADJECTIVES, BOW, CURSE_RAW, CURSES, NOUNS, \
    STOPWORDS, SYLLABLES, VERBS


bagOfWords = fileManager(BOW, 'r').split(',')


def bagOfCurse():

    curseFile = fileManager(CURSE_RAW, 'r')

    return filter(
        None, [word.partition(':')[0].strip().strip()
               for word in curseFile.split()[1:-1]
               if len(word) > 3 and any(char.isdigit() for char in word)]
    )


def bagOfStopWords():

    stopWords = [str(word) for word in stopwords.words('english')]
    stopWords.extend(
        [
            word for word in bagOfWords if word.isdigit() or len(word) < 2
        ]
    )

    return stopWords


def bagOfPOS():

    pos = pos_tag(bagOfWords)

    adj = [word[0] for word in pos if 'JJ' in word[-1]]

    nouns = [word[0] for word in pos if 'NN' in word[-1]]

    verbs = [word[0] for word in pos if 'VB' in word[-1]]

    return adj, nouns, verbs


def countSyllables(word):

    vowels = 'aeiouy'
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

    if (len(word) > 2 and word[-2:] == 'es') or \
            (len(word) > 1 and word[-1:] == 'e'):
        numVowels -= 1

    return numVowels


def bagOfSyllables():

    success = {}

    for word in bagOfWords:
        success[word] = countSyllables(word)

    return success


def convertToDict(featList):

    return OrderedDict(sorted(intersectLists(featList).items()))


def intersectLists(bagOfFeats):

    feat = set(bagOfFeats)

    interesects = list(feat & set(bagOfWords))

    return {
        intersectWord: (bagOfWords.index(intersectWord) + 1)
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

    stopWords = bagOfStopWords()
    stopWords = convertToDict(stopWords)
    dumpJSON(stopWords, STOPWORDS)

    adj, nouns, verbs = bagOfPOS()
    adj = convertToDict(adj)
    nouns = convertToDict(nouns)
    verbs = convertToDict(verbs)
    dumpJSON(adj, ADJECTIVES)
    dumpJSON(nouns, NOUNS)
    dumpJSON(verbs, VERBS)

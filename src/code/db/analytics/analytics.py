#!/usr/bin/env python

"""analytics.py
"""

from random import shuffle
from time import time

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from pandas import concat, DataFrame

from context import *
from settings.filemgmt import loadJSON, fileManager
from settings.paths import CHARTED, FINAL_SET, UNCHARTED
from settings.paths import BOW, CURSES, STOPWORDS, SYLLABLES, ADJECTIVES, \
    NOUNS, VERBS

start = time()

filteredCols = [
    'year',
    'decade',

    'unique_words',
    'density',

    'unique_words_raw',
    'density_raw',

    'nouns',
    'verbs',
    'adjectives',

    'syllables',

    'most_used_term',
    'most_used_freq',

    'explicit',
    'total_curses',

    'reading_score',
    'sentiment',

    'charted'
]

sid = SentimentIntensityAnalyzer()


def loadSet(fileName):

    setName = []

    with open(fileName) as dataFile:
        for line in dataFile:
            setName.append(line.replace('\n', ''))

    return [row.split(',') for row in setName]


def categories(category):

    return set(
        sorted(
            dict(
                loadJSON(category)
            ).values()
        )
    )


def readingScore(density, densityRaw, syllables):

    avSentLen = 0
    upper = 20
    lower = 0

    sentLen = float(densityRaw - density)

    if lower < sentLen < upper:
        avSentLen = densityRaw / float(densityRaw - density)

    else:
        avSentLen = densityRaw / upper

    avSyllables = syllables / float(densityRaw)

    score = 0.39 * (avSentLen) + 11.8 * (avSyllables) - 5.59

    return score


def mostUsed(density, uniqueWords):

    maxIndex = max(density)

    indices = [
        index for index, val in enumerate(density) if val == maxIndex
    ]

    maxVals = []

    for maxes in indices:
        maxVals.append(uniqueWords[maxes] - 1)

    return min(maxVals) + 1


def makeSentence(bow, density, uniqueWords):

    sent = ' '.join(
        [
            (
                (bow[i - 1] + ' ') * density[uniqueWords.index(i)]
            ) for i in uniqueWords
        ]
    ).split()

    shuffle(sent)

    sent = ' '.join(sent)

    return sid.polarity_scores(sent)['compound']


def generateCol(path, analyzedFeats):

    dataset = loadSet(path)
    bow = fileManager(BOW, 'r').split(',')
    syllables = loadJSON(SYLLABLES)

    charted = 1 if path == CHARTED else 0

    curses, stopWords, adj, nouns, verbs = analyzedFeats

    mappedLyrics = {}
    df = []

    for rows in dataset:

        totalCurses = 0
        totalSyllables = 0
        totalAdj = 0
        totalNouns = 0
        totalVerbs = 0

        uniqueWordsRaw = []
        densityRaw = []
        uniqueWords = []
        density = []

        mappedLyrics['year'] = rows[1]
        mappedLyrics['decade'] = rows[1][:-1] + '0'
        mappedLyrics['charted'] = charted

        for cols in rows[2:]:

            term = int(cols.partition(':')[0])
            freq = int(cols.partition(':')[-1])

            try:
                totalSyllables += syllables[bow[term]]

            except Exception:
                continue

            if term not in stopWords:
                uniqueWords.append(term)
                density.append(freq)

            if term in curses:
                totalCurses += freq

            if term in adj:
                totalAdj += freq

            if term in nouns:
                totalNouns += freq

            if term in verbs:
                totalVerbs += freq

            uniqueWordsRaw.append(term)
            densityRaw.append(freq)

        mappedLyrics['total_curses'] = totalCurses

        mappedLyrics['explicit'] = 1 if totalCurses else 0

        mappedLyrics['unique_words'] = len(uniqueWords)

        mappedLyrics['density'] = sum(density)

        mappedLyrics['unique_words_raw'] = len(uniqueWordsRaw)

        mappedLyrics['density_raw'] = sum(densityRaw)

        mostUsedIndex = mostUsed(density, uniqueWords)

        mappedLyrics['most_used_term'] = bow[mostUsedIndex - 1]

        mappedLyrics['most_used_freq'] = density[
            uniqueWords.index(mostUsedIndex)
        ]

        mappedLyrics['syllables'] = totalSyllables

        mappedLyrics['adjectives'] = totalAdj
        mappedLyrics['nouns'] = totalNouns
        mappedLyrics['verbs'] = totalVerbs

        mappedLyrics['sentiment'] = makeSentence(bow, density, uniqueWords)

        mappedLyrics['reading_score'] = readingScore(
            sum(density), sum(densityRaw), totalSyllables
        )

        df.append(mappedLyrics)
        mappedLyrics = {}

    return DataFrame(df)


def dfConfig(path):

    curses = categories(CURSES)
    stopWords = categories(STOPWORDS)
    adj = categories(ADJECTIVES)
    nouns = categories(NOUNS)
    verbs = categories(VERBS)

    features = [curses, stopWords, adj, nouns, verbs]

    df = generateCol(path, features)

    return df[filteredCols].fillna(0)


if __name__ == '__main__':

    charted = dfConfig(CHARTED)
    uncharted = dfConfig(UNCHARTED)

    df = concat([charted, uncharted])
    df.sort_values('year', ascending=True, inplace=True)
    df.to_csv(FINAL_SET, index=False)

    end = time()
    print 'Script took ' + '{0:.3f}'.format((end - start)) + \
        ' seconds to generate data.'

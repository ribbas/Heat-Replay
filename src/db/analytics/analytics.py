#!/usr/bin/env python

"""analytics.py
"""

from nltk import pos_tag
from pandas import concat, DataFrame

from context import *
from settings.filemgmt import loadJSON, fileManager
from settings.paths import BOW, CURSES, CHARTED, FINAL_SET, STOPWORDS, \
    SYLLABLES, UNCHARTED


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

    'curses',
    'total_curses',

    'reading_score',

    'charted'
]


def loadSet(fileName):

    setName = []

    with open(fileName) as dataFile:
        for line in dataFile:
            setName.append(line.replace('\n', ''))

    return [row.split(',') for row in setName]


def categories(category):

    return sorted(dict(loadJSON(category)).values())


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


def generateCol(path, analyzedFeats):

    dataset = loadSet(path)
    bow = fileManager(BOW, 'r').split(',')
    syllables = loadJSON(SYLLABLES)

    charted = 1 if path == CHARTED else 0

    curses = analyzedFeats[0]
    stopWords = analyzedFeats[1]

    mappedLyrics = {}
    df = []

    for rows in dataset:

        totalCurses = 0
        totalSyllables = 0
        uniqueWordsRaw = []
        densityRaw = 0
        unique_words = []
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
                unique_words.append(term)
                density.append(freq)

            if term in curses:
                totalCurses += freq

            uniqueWordsRaw.append(term)
            densityRaw += freq

        mappedLyrics['total_curses'] = totalCurses

        mappedLyrics['curses'] = 1 if totalCurses else 0

        mappedLyrics['unique_words'] = len(unique_words)

        mappedLyrics['density'] = sum(density)

        mappedLyrics['unique_words_raw'] = len(uniqueWordsRaw)

        mappedLyrics['density_raw'] = densityRaw

        maxIndex = max(density)
        indices = [
            index for index, val in enumerate(density) if val == maxIndex
        ]

        maxVals = []
        mostUsed = ''

        for maxes in indices:
            maxVals.append(unique_words[maxes] - 1)

        mostUsed = min(maxVals) + 1

        mappedLyrics['most_used_term'] = bow[mostUsed - 1]

        mappedLyrics['most_used_freq'] = density[unique_words.index(mostUsed)]

        mappedLyrics['syllables'] = totalSyllables

        pos = set(pos_tag([bow[i - 1] for i in unique_words]))
        verbs = len([i for i in pos if i[-1] == 'VB'])
        nouns = len([i for i in pos if i[-1] == 'NN'])
        adj = len([i for i in pos if i[-1] == 'JJ'])

        mappedLyrics['nouns'] = nouns
        mappedLyrics['verbs'] = verbs
        mappedLyrics['adjectives'] = adj

        mappedLyrics['reading_score'] = \
            readingScore(sum(density), densityRaw, totalSyllables)
        df.append(mappedLyrics)
        mappedLyrics = {}

    return DataFrame(df)


def dfConfig(path):

    curses = categories(CURSES)
    stopWords = categories(STOPWORDS)

    features = [curses, stopWords]

    df = generateCol(path, features)

    return df[filteredCols].fillna(0)


if __name__ == '__main__':

    charted = dfConfig(CHARTED)
    uncharted = dfConfig(UNCHARTED)

    df = concat([charted, uncharted])
    df.sort_values('year', ascending=True, inplace=True)
    # print df[['year', 'most_used_term', 'most_used_freq']].head()
    df.to_csv(FINAL_SET, index=False)

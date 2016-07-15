#!/usr/bin/env python

"""analytics.py
"""

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

    'creativity',

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

    try:
        avSentLen = 18 * densityRaw / float(densityRaw - density)
        print avSentLen

    except ZeroDivisionError:
        avSentLen = 18

    avSyllables = syllables / float(densityRaw)

    score = 0.39 * (avSentLen) + 11.8 * (avSyllables) - 15.59

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

        mostUsed = unique_words[density.index(max(density))]

        mappedLyrics['most_used_term'] = bow[mostUsed - 1]

        mappedLyrics['most_used_freq'] = density[unique_words.index(mostUsed)]

        mappedLyrics['creativity'] = \
            float(len(unique_words) / float(sum(density)))

        mappedLyrics['syllables'] = totalSyllables
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
    df.dtypes
    df.to_csv(FINAL_SET, index=False)

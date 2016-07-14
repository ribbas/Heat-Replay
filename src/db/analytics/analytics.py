#!/usr/bin/env python

"""analytics.py
"""

from pandas import concat, DataFrame

from context import *
from settings.filemgmt import loadJSON, fileManager
from settings.paths import BOW, CURSES, CHARTED, FINAL_SET, \
    STOPWORDS, UNCHARTED


filteredCols = [
    'year', 'decade', 'total_curses', 'curses', 'unique_words',
    'density', 'creativity', 'most_used_term', 'most_used_freq', 'charted'
]


def loadSet(fileName):

    setName = []

    with open(fileName) as dataFile:
        for line in dataFile:
            setName.append(line.replace('\n', ''))

    return [row.split(',') for row in setName]


def categories(category):

    return sorted(dict(loadJSON(category)).values())


def generateCol(path, analyzedFeats):

    dataset = loadSet(path)
    bow = fileManager(BOW, 'r').split(',')
    charted = 1 if path == CHARTED else 0

    curses = analyzedFeats[0]
    stopWords = analyzedFeats[1]

    mappedLyrics = {}
    df = []

    for rows in dataset:

        totalCurses = 0
        unique_words = []
        density = []

        mappedLyrics['year'] = rows[1]
        mappedLyrics['decade'] = rows[1][:-1] + '0'
        mappedLyrics['charted'] = charted

        for cols in rows[2:]:

            term = int(cols.partition(':')[0])
            freq = int(cols.partition(':')[-1])

            if term not in stopWords:
                unique_words.append(term)
                density.append(freq)

            if term in curses:
                totalCurses += freq

        mappedLyrics['total_curses'] = totalCurses

        if totalCurses:
            mappedLyrics['curses'] = 1
        else:
            mappedLyrics['curses'] = 0

        mappedLyrics['unique_words'] = len(unique_words)

        mostUsed = density.index(max(density))

        mappedLyrics['most_used_term'] = bow[
            unique_words[mostUsed] - 1]

        mappedLyrics['most_used_freq'] = \
            density[unique_words.index(unique_words[mostUsed])]

        mappedLyrics['density'] = sum(density)

        mappedLyrics['creativity'] = \
            float(len(unique_words) / float(sum(density)))

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

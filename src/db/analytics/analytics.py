#!/usr/bin/env python

"""analytics.py
"""

from pandas import concat, DataFrame

from context import *
from settings.filemgmt import loadJSON
from settings.paths import CURSES, CHARTED, FINAL_SET, UNCHARTED


filteredCols = [
    'year', 'total_curses', 'curses',
    'unique_words', 'density', 'creativity', 'charted'
]


def loadSet(fileName):

    setName = []

    with open(fileName) as dataFile:
        for line in dataFile:
            setName.append(line.replace('\n', ''))

    return [row.split(',') for row in setName]


def categories(category):

    return sorted(dict(loadJSON(category)).values())


def generateCol(path, analyzedSet):

    dataset = loadSet(path)
    charted = 1 if path == CHARTED else 0
    mappedLyrics = {}
    df = []

    for rows in dataset:

        totalCurses = 0
        density = 0

        for cols in rows[2:]:

            term = int(cols.partition(':')[0])
            freq = int(cols.partition(':')[-1])

            mappedLyrics['year'] = rows[1]

            if term in analyzedSet:
                totalCurses += freq
            mappedLyrics['total_curses'] = totalCurses

            if totalCurses:
                mappedLyrics['curses'] = 1
            else:
                mappedLyrics['curses'] = 0

            mappedLyrics['unique_words'] = len(rows[2:])

            density += freq
            mappedLyrics['density'] = density

            mappedLyrics['creativity'] = float(len(rows[2:]) / float(density))

            mappedLyrics['charted'] = charted

        df.append(mappedLyrics)
        mappedLyrics = {}

    return DataFrame(df)


def dfConfig(path):

    curses = categories(CURSES)
    df = generateCol(path, curses)

    df[filteredCols[2:-2]] = df[filteredCols[2:-2]].fillna(0).astype(int)
    return df[filteredCols]


if __name__ == '__main__':

    charted = dfConfig(CHARTED)
    uncharted = dfConfig(UNCHARTED)

    df = concat([charted, uncharted])
    df.sort_values('year', ascending=True, inplace=True)
    df.dtypes
    df.to_csv(FINAL_SET, index=False)

from pandas import DataFrame

from context import *
from settings.filemgmt import loadJSON
from settings.paths import CURSES, MORE0, MORE1, CHARTED, UNCHARTED


def loadSet(fileName):

    setName = []

    with open(fileName) as dataFile:
        for line in dataFile:
            setName.append(line.replace('\n', ''))

    return [row.split(',') for row in setName]


def curses(dataset):

    curses = loadJSON(CURSES)
    cursesVals = dict(curses).values()

    return sorted(cursesVals)


def exportCurses(analyzedSet, dataset, charted):

    mappedLyrics = {}
    df = []

    for rows in dataset:

        totalCurses = 0
        density = 0

        for cols in rows[2:]:

            mappedLyrics['track_id'] = rows[0]
            mappedLyrics['year'] = rows[1]
            if int(cols.partition(':')[0]) in analyzedSet:
                totalCurses += int(cols.partition(':')[-1])
            mappedLyrics['total_curses'] = totalCurses

            if totalCurses:
                mappedLyrics['curses'] = 1
            else:
                mappedLyrics['curses'] = 0

            mappedLyrics['unique_words'] = len(rows[2:])

            density += int(cols.partition(':')[-1])
            mappedLyrics['density'] = density

            mappedLyrics['creativity'] = float(len(rows[2:]) / float(density))

            mappedLyrics['charted'] = charted

        df.append(mappedLyrics)
        mappedLyrics = {}

    return DataFrame(df)


def cursesConfig(path):

    dataset = loadSet(path)

    analyzedSet = curses(dataset)
    cursesDF = exportCurses(analyzedSet, dataset, 1)

    filteredCols = [
        'track_id', 'year', 'total_curses', 'curses',
        'unique_words', 'density', 'creativity', 'charted'
    ]

    exportSet(cursesDF, filteredCols, 'charted.csv')


def exportSet(df, filteredCols, path):

    df[filteredCols[2:-2]] = df[filteredCols[2:-2]].fillna(0).astype(int)
    df[filteredCols].to_csv(path)


if __name__ == '__main__':

    cursesConfig(CHARTED)

from pandas import DataFrame

from context import *
from settings.filemgmt import loadJSON
from settings.paths import CURSES, MORE0, MORE1


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


def exportCurses(analyzedSet, dataset):

    mappedLyrics = {}
    df = []

    for rows in dataset:

        totalCurses = 0
        density = 0

        for cols in rows[1:]:

            mappedLyrics['track_id'] = rows[0]

            if int(cols.partition(':')[0]) in analyzedSet:
                totalCurses += int(cols.partition(':')[-1])
            mappedLyrics['total_curses'] = totalCurses

            mappedLyrics['unique_words'] = len(rows[1:])

            density += int(cols.partition(':')[-1])
            mappedLyrics['density'] = density

            mappedLyrics['creativity'] = float(len(rows[1:]) / float(density))

        df.append(mappedLyrics)
        mappedLyrics = {}

    return DataFrame(df)


def cursesConfig(path):

    dataset = loadSet(path)

    analyzedSet = curses(dataset)
    cursesDF = exportCurses(analyzedSet, dataset)

    filteredCols = [
        'track_id', 'total_curses',
        'unique_words', 'density', 'creativity'
    ]
    exportSet(cursesDF, filteredCols, 'test.csv')


def exportSet(df, filteredCols, path):

    df[filteredCols[1:-1]] = df[filteredCols[1:-1]].fillna(0).astype(int)
    df[filteredCols].to_csv(path)


if __name__ == '__main__':

    cursesConfig(MORE0)

from pandas import DataFrame

from context import *
from settings.filemgmt import fileManager, loadJSON
from settings.paths import CHARTED_TIDS, CURSES, MXM


def loadSet(fileName):

    setName = []
    charted = fileManager(CHARTED_TIDS, 'r')

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for line in lyricsFile:

            if line.split(',')[0] in charted:
                setName.append(line)

    dif = [line.replace('\n', '') for line in setName]
    print len(list(set(charted.split('\n')) - set(dif)))
    return setName


def readSet():

    dataset = loadSet(MXM)

    curses = loadJSON(CURSES)

    cursesVals = dict(curses).values()

    maxRow = max(cursesVals) + 1

    splitLyrics = [row.split(',') for row in dataset]

    mappedLyrics = {}
    df = []

    for rows in splitLyrics:

        for cols in rows[2:maxRow]:
            mappedLyrics['track_id'] = rows[0]
            mappedLyrics[int(cols.partition(':')[0])] = \
                int(cols.partition(':')[-1])

        df.append(mappedLyrics)
        mappedLyrics = {}

    return df, cursesVals


def exportSet():

    df = DataFrame(readSet()[0])
    cursesVals = readSet()[1]
    filteredCols = [cols for cols in cursesVals if cols in list(df)]

    df[filteredCols] = df[filteredCols].fillna(0)
    df[filteredCols].to_csv('test.csv')


if __name__ == '__main__':

    exportSet()

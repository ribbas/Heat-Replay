from json import load
from pandas import DataFrame
from settings import *

TEST_PATH = 'test.txt'


def loadJSON():
    """Loads in curse indices"""

    with open(CURSES) as inputJSON:
        return load(inputJSON)


def readSet():

    dataset = fileManager(TEST_PATH, 'r')

    curses = loadJSON()

    cursesVals = dict(curses).values()

    maxRow = max(cursesVals) + 1

    splitLyrics = [row.split(',') for row in dataset.split('\n')]

    mappedLyrics = {}
    df = []

    for rows in splitLyrics:

        for cols in rows[2:maxRow]:
            mappedLyrics['track_id'] = rows[0]
            mappedLyrics['mxm track id'] = rows[1]
            mappedLyrics[int(cols.partition(':')[0])] = \
                int(cols.partition(':')[-1])

        df.append(mappedLyrics)
        mappedLyrics = {}

    return df, cursesVals


def exportSet():

    df = DataFrame(readSet()[0])
    cursesVals = readSet()[1]
    filteredCols = [cols for cols in cursesVals if cols in list(df)]

    print df[filteredCols]

exportSet()

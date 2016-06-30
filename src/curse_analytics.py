from json import load

from pandas import DataFrame

from settings import *

JSON_PATH = 'curses.json'
DATASET_PATH = 'test.txt'


def loadJSON():

    with open(JSON_PATH) as inputJSON:
        inputJSON = load(inputJSON)

    return inputJSON


def readSet():

    dataset = fileManager(DATASET_PATH, 'r')

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

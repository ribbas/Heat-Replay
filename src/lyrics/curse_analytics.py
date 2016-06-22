from json import load
from sys import path

from pandas import DataFrame

path.insert(0, '../dir_factory')
from dirMethods import fileManager


JSON_PATH = 'curses.json'
DATASET_PATH = 'test.txt'


def loadJSON():

    with open(JSON_PATH) as inputJSON:
        inputJSON = load(inputJSON)

    return inputJSON


def readSet():

    dataset = fileManager(DATASET_PATH, 'r')

    df = DataFrame(row.split(',') for row in dataset.split('\n'))

    print df

readSet()

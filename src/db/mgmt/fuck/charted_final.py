from context import *
from settings.filemgmt import fileManager
from settings.paths import CHARTED


def loadSet(fileName):

    setName = ''

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for line in lyricsFile:
            setName += line

    return setName


if __name__ == '__main__':

    set1 = loadSet('more0_f.txt').split('\n')
    set2 = loadSet('more0_failed.txt').split('\n')
    set3 = loadSet('more1_f.txt').split('\n')

    chartedSet = set1 + set2 + set3

    fileManager(CHARTED, 'w', '\n'.join(sorted(chartedSet)))

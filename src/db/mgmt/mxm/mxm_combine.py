from context import *
from settings.filemgmt import fileManager
from settings.paths import MXM_TEST, MXM_TRAIN, MXM


def loadSet(fileName):

    setName = []
    startLine = 17

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            if lineNum > startLine:
                setName.append(line)

    return setName

if __name__ == '__main__':

    finalSet = []
    finalSet.extend(loadSet(MXM_TEST))
    finalSet.extend(loadSet(MXM_TRAIN))

    finalSet = ''.join(sorted(set(finalSet)))

    fileManager(MXM, 'w', finalSet)

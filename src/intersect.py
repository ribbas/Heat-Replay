from settings import *


def loadSet(fileName):

    setName = set()

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            if lineNum:
                setName.add(line)

    return setName

if __name__ == '__main__':

    fileManager(
        CHARTED_MXM, 'w',
        ''.join(sorted(list(loadSet(CHARTED) & loadSet(FILTERED_MXM))))
    )

    fileManager(
        CHARTED_FAIL, 'w',
        ''.join(sorted(list(loadSet(CHARTED) - loadSet(FILTERED_MXM))))
    )

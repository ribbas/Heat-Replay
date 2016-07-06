from json import dump

from context import settings
from settings.filemgmt import fileManager
from settings.paths import BOW, CURSE_RAW, CURSES, MXM_PATH


def bagOfWords():

    with open(MXM_PATH) as lyricsFile:

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            # index 17 is the bag of words
            if lineNum == 17:
                rawBagOfWords = line[1:]
                fileManager(BOW, 'w', rawBagOfWords)
                break

    return rawBagOfWords.split(',')


def bagOfCurse():

    curseFile = fileManager(CURSE_RAW, 'r')

    return filter(
        None, [word.partition(':')[0].strip().strip()
               for word in curseFile.split()[1:-1]
               if len(word) > 3 and any(char.isdigit() for char in word)]
    )


def intersectLists():

    curses = set(bagOfCurse())
    words = set(bagOfWords())

    return list(curses & words)


def mapIndices():

    curses = intersectLists()
    words = bagOfWords()

    return {
        curseWord: (words.index(curseWord) + 1) for curseWord in curses
    }


def dumpJSON():

    curseData = mapIndices()

    with open(CURSES, 'w') as outputJSON:
        dump(curseData, outputJSON)


if __name__ == '__main__':

    dumpJSON()

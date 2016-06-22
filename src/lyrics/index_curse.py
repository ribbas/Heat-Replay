from json import dump
from sys import path

path.insert(0, '../dir_factory')
from dirMethods import fileManager

RAW_DIR = 'raw_files/{file}.txt'
# test instead of train because of size
MXM_PATH = RAW_DIR.format(file='mxm_dataset_test')
CURSE_PATH = RAW_DIR.format(file='google_twunter_lol')
CURSES = 'curses.json'


def bagOfWords():

    with open(MXM_PATH) as lyricsFile:

        # to avoid the entire file from being read into memory
        # (enumerate(x) uses x.next)
        for lineNum, line in enumerate(lyricsFile):

            # index 17 is the bag of words
            if lineNum == 17:
                rawBagOfWords = line
                break

    return rawBagOfWords.split(',')


def bagOfCurse():

    curseFile = fileManager(CURSE_PATH, 'r')

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
        curseWord: words.index(curseWord) for curseWord in curses
    }


def dumpJSON():

    curseData = mapIndices()

    with open(CURSES, 'w') as outputJSON:
        dump(curseData, outputJSON)


if __name__ == '__main__':
    dumpJSON()

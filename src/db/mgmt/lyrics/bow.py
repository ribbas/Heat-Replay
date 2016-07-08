from context import settings
from settings.filemgmt import fileManager
from settings.paths import BOW, MXM_TEST


def bagOfWords():

    with open(MXM_TEST) as lyricsFile:

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            # index 17 is the bag of words
            if lineNum == 17:
                rawBagOfWords = line[1:]
                break

    return rawBagOfWords

if __name__ == '__main__':

    rawBagOfWords = bagOfWords()
    fileManager(BOW, 'w', rawBagOfWords)

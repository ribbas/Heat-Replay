#!/usr/bin/env python
"""bow.py
Extracts the raw bag of words used in the musiXmatch dataset
"""

from context import *
from settings.filemgmt import fileManager
from settings.paths import BOW, MXM_TEST


def bagOfWords():
    """returns the line containing the bag of words"""

    with open(MXM_TEST) as lyricsFile:

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            # index 17 is the bag of words
            if lineNum == 17:
                rawBagOfWords = line[1:]
                break

    return rawBagOfWords

if __name__ == '__main__':

    fileManager(BOW, 'w', bagOfWords())

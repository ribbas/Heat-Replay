from context import *
from settings.filemgmt import fileManager
from settings.paths import MXM, MXM_TID, sep


def newFrame():

    newFrame = []

    with open(MXM) as lyricsFile:

        rawNewFrame = ''
        start = 0

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            if lineNum >= start:
                rawNewFrame += line

    for row in rawNewFrame.split('\n'):

        try:

            newFrame.append(row.split(',')[0])

        except Exception:
            continue

    return '\n'.join(sorted(set(filter(None, newFrame))))

fileManager(MXM_ALL, 'w', newFrame())

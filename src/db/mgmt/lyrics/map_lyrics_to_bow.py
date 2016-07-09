from os import listdir, remove

from context import *
from settings.filemgmt import fileManager
from settings.paths import RANGE1, BOW, sep
from lyrics_to_bow import lyrics_to_bow


def readLyrics(dir):

    mxmBow = fileManager(BOW, 'r').split(',')

    files = sorted(listdir(dir))

    newSet = []
    songLyrics = []

    for lyrics in files:
        bow = lyrics_to_bow(fileManager(RANGE1 + lyrics, 'r'))
        try:
            for word, freq in bow.iteritems():
                try:
                    songLyrics.append(
                        str(mxmBow.index(word) + 1) + ':' + str(freq)
                    )

                except ValueError:
                    continue
            newSet.append(
                [lyrics[:-4].replace('-lyrics-', sep)] +
                sorted(
                    songLyrics, key=lambda s: int(s.partition(':')[0])
                )
            )
            songLyrics = []

        except AttributeError:
            remove(RANGE1 + lyrics)

    newSet = '\n'.join(sorted([','.join(line) for line in newSet]))
    fileManager('more.txt', 'w', newSet)

if __name__ == '__main__':

    readLyrics(RANGE1)

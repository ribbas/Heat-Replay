#!/usr/bin/env python

from os import listdir

from context import *
from settings.filemgmt import fileManager
from settings.paths import BOW, MORE1, RANGE1, sep
from lyrics_to_bow import lyrics_to_bow


def readLyrics(dir):

    mxmBow = fileManager(BOW, 'r').split(',')

    files = sorted(listdir(dir))

    newSet = []
    songLyrics = []
    bow = '{word}:{freq}'

    for lyrics in files:
        bow = lyrics_to_bow(fileManager(RANGE1 + lyrics, 'r'))

        try:

            for word, freq in bow.iteritems():

                try:

                    songLyrics.append(
                        bow.format(
                            word=str(mxmBow.index(word) + 1),
                            freq=str(freq)
                        )
                    )

                except ValueError:
                    continue

            newSet.append(
                [
                    sep.join(
                        lyrics[:-4].split('-lyrics-')[::-1]
                    ).replace('-', '')
                ] +
                sorted(
                    songLyrics, key=lambda s: int(s.partition(':')[0])
                )
            )
            songLyrics = []

        except AttributeError:
            print "Failed to index", lyrics
            continue

    return '\n'.join(sorted([','.join(line) for line in newSet]))

if __name__ == '__main__':

    newSet = readLyrics(RANGE1)
    fileManager(MORE1, 'w', newSet)

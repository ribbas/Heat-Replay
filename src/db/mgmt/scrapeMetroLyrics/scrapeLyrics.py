#!/usr/bin/env python

from random import randrange
from time import sleep

from context import *
from settings.filemgmt import fileManager
from settings.paths import FAIL, QUEUE, RANGE1
from lyrics import Lyrics


class ScrapeLyrics:

    def __init__(self, path):

        self.path = path

    def __saveProgress(self, queue, success, failed):

        newQueue = sorted(queue - success - failed)

        fileManager(FAIL, 'a', output='\n'.join(sorted(failed)))
        fileManager(QUEUE, 'w', output='\n'.join(newQueue))

        if len(newQueue):
            exit('\n' + str(len(newQueue)) +
                 ' songs left.\nSaving progress.')

        exit('Queue is empty, scraping completed!')

    def scrape(self):

        rawFile = fileManager(self.path, 'r').split('\n')
        success = set()
        failed = set()

        for line in rawFile:

            try:
                sleep(randrange(0, 2))
                song = Lyrics(line)
                song.scrape()
                lyrics = song.lyrics

                if lyrics:
                    fileManager(
                        RANGE1.format(file=song.name), 'w', song.lyrics
                    )
                    success.add(line)

                else:
                    failed.add(line)

            except KeyboardInterrupt:
                break

            except Exception as e:
                print e
                continue

        self.__saveProgress(set(rawFile), success, failed)

if __name__ == '__main__':

    obj = ScrapeLyrics(QUEUE)
    obj.scrape()

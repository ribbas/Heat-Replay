#!/usr/bin/env python
"""filemgmt.py
Global variables and methods for Heat Replay
"""

from json import load


def fileManager(path, mode, output=''):
    """Basic IO operations

    path: path of file
    mode: file access mode
    output: string output to write or append to file
    """

    with open(path, mode) as file:

        if mode == 'w' and output:
            file.write(output)

        elif mode == 'a' and output:
            file.write('\n' + output)

        elif mode == 'r':
            data = ''
            for line in file:
                data += line
            return data


def loadJSON(fileName):
    """Loads in curse indices"""

    with open(fileName) as inputJSON:
        return load(inputJSON)


def sortSet(dataset):

    setName = set()

    with open(dataset) as lyricsFile:

        # to avoid the entire file from being read into memory
        for line in lyricsFile:
            setName.add(line)

    setName = ''.join(sorted(list(setName)))

    fileManager(dataset, 'w', setName)

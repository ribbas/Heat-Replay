from string import ascii_lowercase

from settings import *


def newFrame(colStart, colEnd):

    newFrame = []

    with open(MXM) as lyricsFile:

        rawNewFrame = ''
        start = fileManager(FILE_LINE_NUM, 'r')

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            if lineNum >= int(start):
                rawNewFrame += line

    for row in rawNewFrame.split('\n'):

        rowSplit = '<SEP>'.join(
            regexify(col) for col in row.split('<SEP>')[colStart:colEnd]
        )

        try:
            if rowSplit.decode('ascii') and \
                    rowSplit[0] in ascii_lowercase:
                newFrame.extend([rowSplit])

        except Exception:
            continue

    return '\n'.join(sorted(set(filter(None, newFrame))))

fileManager(FILTERED_MXM, 'w', newFrame(4, 6))

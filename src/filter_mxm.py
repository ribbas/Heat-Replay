from string import ascii_lowercase

from settings import *


def newFrame(colStart, colEnd):

    newFrame = []
    compileTitleRe()

    with open(MXM) as lyricsFile:

        rawNewFrame = ''
        start = 18

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            if lineNum >= int(start):
                rawNewFrame += line

    for row in rawNewFrame.split('\n'):

        rowSplit = '<SEP>'.join(
            [row.split('<SEP>')[0]] +
            [regexify(col) for col in row.split('<SEP>')[colStart:colEnd]]
        )

        try:
            if rowSplit.decode('ascii') and \
                    rowSplit.split('<SEP>')[1][0] in ascii_lowercase:
                newFrame.extend([rowSplit])

        except Exception:
            continue

    return '\n'.join(sorted(set(filter(None, newFrame))))

fileManager(FILTERED_MXM, 'w', newFrame(4, 6))

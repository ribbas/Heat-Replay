from string import ascii_lowercase

from settings import *


def newFrame(colStart, colEnd, raw=False):

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

        try:

            rowSplit = sep.join(
                [row.split(sep)[0]] +
                [regexify(col)
                 for col in row.split(sep)[colStart:colEnd]]
            ) if raw else sep.join(
                [regexify(col)
                 for col in row.split(sep)[colStart:colEnd]]
            )

            artist = rowSplit.split(sep)[1][0] \
                if raw else rowSplit.split(sep)[0][0]

            if rowSplit.decode('ascii') and artist in ascii_lowercase:
                newFrame.extend([rowSplit])

        except Exception:
            continue

    return '\n'.join(sorted(set(filter(None, newFrame))))

fileManager(FILTERED_MXM_RAW, 'w', newFrame(4, 6, True))

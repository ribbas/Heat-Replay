from string import ascii_lowercase

from settings import *

RAW_DIR = DATA_DIR + '{file}.txt'
MXM_PATH = RAW_DIR.format(file='mxm/mxm_779k_matches')
FILE_LINE_NUM = RAW_DIR.format(file='line')
FILTERED_MXM = RAW_DIR.format(file='mxm_filtered')


def newFrame(colStart, colEnd):

    newFrame = []

    with open(MXM_PATH) as lyricsFile:

        rawNewFrame = ''
        start = fileManager(FILE_LINE_NUM, 'r')

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            try:

                if lineNum >= int(start):
                    rawNewFrame += line

            except KeyboardInterrupt:
                fileManager(FILE_LINE_NUM, 'w', str(lineNum))
                break

    for row in rawNewFrame.split('\n'):

        rowSplit = '<SEP>'.join(
            endRe.sub(
                '', moreFilterRe.sub(
                    '', filterRe.sub(
                        '', col.lower()
                    )
                )
            ).rstrip()
            for col in row.split('<SEP>')[colStart:colEnd]
        )

        try:
            if rowSplit[0].decode('ascii') and \
                    rowSplit[0][0] in ascii_lowercase:
                newFrame.extend([rowSplit])

        except Exception:
            continue

    return '\n'.join(sorted(set(filter(None, newFrame))))

fileManager(FILTERED_MXM, 'w', newFrame(4, 6))

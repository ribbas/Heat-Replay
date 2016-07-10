from context import *
from settings.filemgmt import fileManager
from settings.paths import CHARTED_RAW, FILTERED_MXM_RAW, CHARTED_TIDS, sep
from settings.regexify import *


def loadSet(fileName):

    setName = ''

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for line in lyricsFile:
            setName += line

    return setName


if __name__ == '__main__':

    compileTitleRe()

    charted_tids = loadSet(CHARTED_TIDS).split('\n')
    charted_title_year = loadSet(CHARTED_RAW).split('\n')

    mxm = [row.split(sep) for row in loadSet(FILTERED_MXM_RAW).split('\n')]

    fuck = []

    for i in mxm:
        if i[0] in charted_tids:
            fuck.append(sep.join(i))

    fileManager('charted_tid_year', 'w', '\n'.join(fuck))
    #     if i in
    #     if i in mxm:
    #         print mxm.index(i)

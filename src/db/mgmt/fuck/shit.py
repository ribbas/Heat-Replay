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


def idk():

    compileTitleRe()

    charted_tids = loadSet(CHARTED_TIDS).split('\n')

    mxm = [row.split(sep) for row in loadSet(FILTERED_MXM_RAW).split('\n')]

    fuck = []

    for i in mxm:
        if i[0] in charted_tids:
            fuck.append(sep.join(i))

    fileManager('charted_tid_title.txt', 'w', '\n'.join(fuck))


def normalize(mode, row):

    if not mode:
        return sep.join(row.split(sep)[1:]).replace(' ', '')
    else:
        return sep.join(row.split(sep)[:-1]).replace('-', '')

if __name__ == '__main__':

    charted_title_year = loadSet(CHARTED_RAW).split('\n')
    charted_title_tid = loadSet('charted_tid_title.txt').split('\n')

    yo = [normalize(1, i) for i in charted_title_year]

    pls = []

    for i in charted_title_tid:
        if normalize(0, i) in yo:
            row = \
                normalize(0, i) + sep + \
                i.partition(sep)[0] + sep + \
                charted_title_year[yo.index(normalize(0, i))].split(sep)[-1]
            pls.append(row)

    fileManager('charted_tid_year_title.txt', 'w', '\n'.join(pls))

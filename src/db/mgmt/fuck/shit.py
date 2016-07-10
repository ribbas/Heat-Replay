from context import *
from settings.filemgmt import fileManager
from settings.paths import CHARTED_RAW, FILTERED_MXM_RAW, CHARTED_TIDS, sep
from settings.paths import MORE0, MORE1
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


def idgaf():

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

    fileManager('charted_tid_year_title.txt', 'w', '\n'.join(sorted(pls)))


def more0():

    more0 = loadSet(MORE0).split('\n')
    charted_title_tid_year = loadSet('charted_tid_year_title.txt').split('\n')

    yo = [i.split(sep)[2] for i in charted_title_tid_year]

    final = []
    failed = []

    for i in more0:
        if i.split(',')[0] in yo:
            extras = charted_title_tid_year[
                yo.index(i.split(',')[0])
            ].split(sep)
            newRow = sep.join(extras[:2]) + ',' + \
                extras[-1] + ',' + ','.join(i.split(',')[1:])
            final.append(newRow)
        else:
            failed.append(i)

    fileManager('more0_f.txt', 'w', '\n'.join(sorted(final)))
    fileManager('more0_failed.txt', 'w', '\n'.join(sorted(failed)))

if __name__ == '__main__':

    raw = loadSet(CHARTED_RAW).split('\n')
    charted_raw = [i.replace('-', '') for i in raw]
    yo = [normalize(1, i) for i in raw]

    more1 = loadSet(MORE1).split('\n')

    final = []
    failed = []

    for i in more1:
        if i.split(',')[0] in yo:
            extras = charted_raw[
                yo.index(i.split(',')[0])
            ].split(sep)
            newRow = sep.join(extras[:2]) + ',' + extras[-1] + \
                ',' + ','.join(i.split(',')[1:])
            final.append(newRow)
        else:
            failed.append(i)

    fileManager('more1_f.txt', 'w', '\n'.join(sorted(final)))
    fileManager('more1_failed.txt', 'w', '\n'.join(sorted(failed)))

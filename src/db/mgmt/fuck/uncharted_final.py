from context import *
from settings.filemgmt import fileManager
from settings.paths import MSD_MXM, MSD_TID_YEAR, CHARTED_TIDS, \
    MXM, UNCHARTED, sep


def loadSet(fileName):

    setName = ''

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for line in lyricsFile:
            setName += line

    return setName


if __name__ == '__main__':

    charted_tid = loadSet(CHARTED_TIDS).split('\n')
    msd_mxm = loadSet(MSD_MXM).split('\n')
    msd_tid_year = loadSet(MSD_TID_YEAR).split('\n')
    mxm = loadSet(MXM).split('\n')

    filtered = [i.split(sep)[0] for i in msd_tid_year]
    filtered1 = [i.split(',')[0] for i in mxm]

    yo = []

    for i in msd_mxm:
        if i in filtered and i in filtered1 and i not in charted_tid:
            tid_year = msd_tid_year[filtered.index(i)]
            bow = mxm[filtered1.index(i)]
            newRow = ','.join(tid_year.split(sep)) + ',' + \
                ','.join(bow.split(',')[2:])
            yo.append(newRow)

    fileManager(UNCHARTED, 'w', '\n'.join(sorted(yo)))

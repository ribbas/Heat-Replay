from context import *
from settings.filemgmt import fileManager
from settings.paths import MXM, MSD_TID_YEAR, MSD_MXM, UNCHARTED, sep


def loadSet(fileName):

    setName = set()

    with open(fileName) as file:

        # to avoid the entire file from being read into memory
        for line in file:
            setName.add(line)

    return setName


if __name__ == '__main__':

    mxm = set([line.partition(',')[0] for line in loadSet(MXM)])
    msd = set([line.split(sep)[0] for line in loadSet(MSD_TID_YEAR)])
    intersects = sorted(list(mxm & msd))

    intersects = [
        line for line in loadSet(MXM) if line.partition(',')[0] in intersects
    ]

    fileManager(MSD_MXM, 'w', '\n'.join(intersects))

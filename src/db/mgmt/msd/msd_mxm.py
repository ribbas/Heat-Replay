from context import settings
from settings.filemgmt import fileManager
from settings.paths import MXM_ALL, MSD_, MSD_MXM, sep


def loadSet(fileName):

    setName = set()

    with open(fileName) as file:

        # to avoid the entire file from being read into memory
        for line in file:
            setName.add(line)

    return setName


if __name__ == '__main__':

    mxm = set([line.partition('\n')[0] for line in loadSet(MXM_ALL)])
    msd = set([line.split(sep)[0] for line in loadSet(MSD_)])

    fileManager(MSD_MXM, 'w', '\n'.join(sorted(list(mxm & msd))))

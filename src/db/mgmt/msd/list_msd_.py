from os import listdir

from context import settings
from settings.filemgmt import fileManager
from settings.paths import MSD_TID, MSD_DIR, MSD_FILES

if __name__ == '__main__':

    hdf5Files = [
        MSD_DIR + h5 for h5 in listdir(MSD_DIR)
        if h5.partition('.')[-1] == 'h5' and h5.startswith('T')
    ]

    hdf5 = [
        h5.split('/')[-1].partition('.')[0] for h5 in hdf5Files
    ]

    fileManager(MSD_FILES, 'w', '\n'.join(hdf5Files))
    fileManager(MSD_TID, 'w', '\n'.join(hdf5))

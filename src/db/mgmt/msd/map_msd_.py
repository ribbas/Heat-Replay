from context import *
from settings.filemgmt import fileManager
from settings.paths import MSD_TID_YEAR, MSD_FILES, sep
from hdf5_getters import open_h5_file_read, get_year

if __name__ == '__main__':

    hdf5Files = fileManager(MSD_FILES, 'r').split('\n')

    msdData = []

    for file in hdf5Files:
        h5 = open_h5_file_read(file)
        year = get_year(h5)
        if year > 1960:
            msdData.append(
                str(file.split('/')[-1].partition('.')[0]) +
                sep + str(year)
            )
        h5.close()

    fileManager(MSD_TID_YEAR, 'w', '\n'.join(msdData))

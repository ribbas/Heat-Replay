from context import settings
from settings.filemgmt import fileManager
from settings.paths import MSD_, MSD_FILES, MSD_RAW, sep
from hdf5_getters import open_h5_file_read, get_year

if __name__ == '__main__':

    hdf5Files = fileManager(MSD_FILES, 'r').split('\n')

    msdData = []

    for file in hdf5Files:
        h5 = open_h5_file_read(file)
        year = get_year(h5)
        if year:
            msdData.append(
                str(file.split('/')[-1].partition('.')[0]) +
                sep + str(year)
            )
        h5.close()

    fileManager(MSD_, 'w', '\n'.join(msdData))

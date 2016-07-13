#!/usr/bin/env python

"""
Thierry Bertin-Mahieux (2010) Columbia University
tb2332@columbia.edu

Code to quickly see the content of an HDF5 file.

This is part of the Million Song Dataset project from
LabROSA (Columbia University) and The Echo Nest.


Copyright 2010, Thierry Bertin-Mahieux

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import hdf5_getters


if __name__ == '__main__':
    """ MAIN """

    # get params
    hdf5path = 'TRBAADN128F426B7A4.h5'
    songidx = 0

    # sanity check
    if not os.path.isfile(hdf5path):
        print 'ERROR: file', hdf5path, 'does not exist.'
        sys.exit(0)
    h5 = hdf5_getters.open_h5_file_read(hdf5path)
    numSongs = hdf5_getters.get_num_songs(h5)
    if songidx >= numSongs:
        print 'ERROR: file contains only', numSongs
        h5.close()
        sys.exit(0)

    # print them
    try:
        res = hdf5_getters.get_year(h5, songidx)
    except Exception, e:
        print e
    print res

    h5.close()

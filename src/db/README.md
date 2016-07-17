# Source code for generating the datasets for Heat Replay

## Structure of the directory
```
db
├── analytics; manages higher level dataset manipulations
│   ├── analytics.py; generates the final dataset using all the other datasets
│   └── index_feat.py; indexes features against the bag of words
│
└── mgmt; manages low level dataset manipulations
    ├── DataWaves; scrapes lyrics from MetroLyrics
    │   ├── lyrics.py
    │   └── scrapeLyrics.py
    ├── final; merges and manages the datasets leading up to the final dataset
    │   ├── charted_final.py
    │   ├── concat.py
    │   └── uncharted_final.py
    ├── HotSingles; scrapes list of charted songs from Wikipedia
    │   └── hot_singles.py
    ├── lyrics; handles the low level lyrical indexing and analysis
    │   ├── bow.py
    │   ├── lyrics_to_bow.py
    │   ├── more1.py
    │   └── sep_to_url.py
    ├── msd; manages the MillionSongDataset files
    │   ├── display_song.py
    │   ├── hdf5_getters.py
    │   ├── list_msd_.py
    │   ├── map_msd_.py
    │   └── msd_mxm.py
    └── mxm; manages the musiXmatch files
        ├── intersect.py
        ├── more0.py
        ├── mxm_combine.py
        ├── mxm_filter.py
        └── mxm_main.py

8 directories, 22 files
```
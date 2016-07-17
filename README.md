# Heat Replay <img src="https://github.com/kug3lblitz/Heat-Replay/blob/master/static/logo.png" width=10px>

a data science project that will attempt to determine if the lyrical content of a song can predict 
if it will hit the Billboard Year-End Hot 100 singles. The project will intersect several datasets to create a final
dataframe that will consist of songs that charted and those that did not chart, with each comprising exactly 50% of 
the set, along with the bag of words version of their lyrics and the analyses on them, such as sentiment analysis, 
frequency of obscene words, frequency of words pertaining to certain themes, total number of unique words, etc. and 
the year they charted. The dataframe will also include the last column 'charted', a binary variable that corresponds
to the chart status of the song.

## Drafted structure of features

1. Track information
  1.  Year (int)

2.  Lyrical content
  1.  Frequency of curse words (int)
  2.  Most frequent word (string)
  3.  Density of words (int)
  4.  Number of unique words (int)
  5.  Sentiment analysis (float) (if time allows)

3.  Chart
  1.  Yes (b’1)
  2.  No (b’0)


## Structure of repository
```
src
├── data
│   ├── archive
│   │   ├── charted
│   │   │   ├── charted_raw2.txt
│   │   │   └── charted_raw.txt
│   │   ├── curses
│   │   │   └── google_twunter.txt
│   │   ├── msd
│   │   │   ├── msd_files.txt
│   │   │   ├── msd_tid.txt
│   │   │   └── msd_tid_year.txt
│   │   └── mxm
│   │       ├── mxm_raw
│   │       │   ├── mxm_779k_matches.txt
│   │       │   ├── mxm_dataset_test.txt
│   │       │   ├── mxm_dataset_train.txt
│   │       │   └── mxm.txt
│   │       └── mxm_tid.txt
│   ├── final
│   │   ├── adj.json
│   │   ├── bow.txt
│   │   ├── charted_tid.txt
│   │   ├── charted.txt
│   │   ├── curses.json
│   │   ├── final.csv
│   │   ├── more0.txt
│   │   ├── more1.txt
│   │   ├── MSD_mxm.txt
│   │   ├── nouns.json
│   │   ├── stopwords.json
│   │   ├── syllables.json
│   │   ├── uncharted.txt
│   │   └── verbs.json
│   ├── README.md
│   └── transitional
│       ├── charted
│       │   ├── charted_failed.txt
│       │   └── charted_mxm.txt
│       └── mxm
│           ├── mxm_filtered_raw.txt
│           └── mxm_filtered.txt
├── db
│   ├── analytics
│   │   ├── analytics.py
│   │   ├── context.py
│   │   └── index_feat.py
│   └── mgmt
│       ├── DataWaves
│       │   ├── context.py
│       │   ├── lyrics.py
│       │   └── scrapeLyrics.py
│       ├── final
│       │   ├── charted_final.py
│       │   ├── charted_tid_title.txt
│       │   ├── charted_tid_year_title.txt
│       │   ├── concat.py
│       │   ├── context.py
│       │   ├── more0_failed.txt
│       │   ├── more0_f.txt
│       │   ├── more1_failed.txt
│       │   ├── more1_f.txt
│       │   ├── uncharted_final.py
│       │   └── uncharted_f.txt
│       ├── HotSingles
│       │   ├── context.py
│       │   └── hot_singles.py
│       ├── msd
│       │   ├── context.py
│       │   ├── display_song.py
│       │   ├── hdf5_getters.py
│       │   ├── list_msd_.py
│       │   ├── map_msd_.py
│       │   └── msd_mxm.py
│       └── mxm
│           ├── context.py
│           ├── intersect.py
│           ├── more0.py
│           ├── mxm_combine.py
│           ├── mxm_filter.py
│           └── mxm_main.py
├── models
└── settings
    ├── filemgmt.py
    ├── paths.py
    └── regexify.py

22 directories, 65 files
```
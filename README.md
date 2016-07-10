# Heat Replay
General Assembly: Data Science project to predict if a song will hit the Billboard Year-End Hot 100 singles

### Research question
Can acoustic attributes (loudness, energy, danceability, and tempo), song structure (duration, end of fade in, and start of fade out) and lyrical content (frequency of obscene words, most frequent word, and density of words) predict if the song will reach the Billboard Year-End Hot 100 singles?

### Drafted structure of features

1. Track information
  1.  Year (int)
  2.  Title (string)
  3.  Artist (string)

2.	Acoustic attributes
  1.	Loudness (float)
  2.	Energy (float)
  3.	Danceability (float)
  4.	Tempo (float)

3.	Song structure
  1.	Duration (time)
  2.	End of fade in (time)
  3.	Start of fade out (time)

4.	Lyrical content
  1.	Frequency of curse words (int)
  2.	Most frequent word (string)
  3.	Density of words (int)

5.	Chart
  1.	Yes (b’1)
  2.	No (b’0)

### [Sources for datasets](https://github.com/kug3lblitz/Heat-Replay/tree/master/src/data)
*	Million Song Dataset (MSD)
*	EchoNest, MSD, for acoustic attributes
*	musiXmatch, MSD, for lyrical bag of words
*	Wikipedia Year-End Hot 100 scraped pages, for list of songs in the chart (5800 songs)

### Structure of repository:
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
│   │   ├── bow.txt
│   │   ├── charted_tid.txt
│   │   ├── curses.json
│   │   ├── more0.txt
│   │   ├── more1.txt
│   │   └── MSD_mxm.txt
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
│   │   ├── context.py
│   │   ├── curse_analytics.py
│   │   ├── __init__.py
│   │   └── test.csv
│   ├── __init__.py
│   └── mgmt
│       ├── charted
│       │   ├── charted.py
│       │   ├── context.py
│       │   └── __init__.py
│       ├── DataWaves
│       │   ├── context.py
│       │   ├── __init__.py
│       │   ├── lyrics.py
│       │   └── scrapeLyrics.py
│       ├── msd
│       │   ├── context.py
│       │   ├── display_song.py
│       │   ├── hdf5_getters.py
│       │   ├── __init__.py
│       │   ├── list_msd_.py
│       │   ├── map_msd_.py
│       │   └── msd_mxm.py
│       └── mxm
│           ├── context.py
│           ├── __init__.py
│           ├── intersect.py
│           ├── more0.py
│           ├── mxm_combine.py
│           ├── mxm_filter.py
│           └── mxm_main.py
└── settings
    ├── filemgmt.py
    ├── __init__.py
    ├── paths.py
    └── regexify.py

19 directories, 52 files
```
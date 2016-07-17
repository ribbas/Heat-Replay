# Datasets

The following datasets are publicly available:

- [Million Song Dataset](http://labrosa.ee.columbia.edu/millionsong/): audio features and metadata for one million contemporary popular music tracks
- [musiXmatch Dataset](http://labrosa.ee.columbia.edu/millionsong/musixmatch): lyrics mapping to 23.8% of the songs from the Million Song Dataset

## Structure of directory
```
data
│
├── archive; archived datasets (not to be modified after creation)
│   ├── charted; generated from HotSingles 
│   │   ├── charted_raw2.txt; charted songs from 2011 - 2015
│   │   └── charted_raw.txt; charted songs from 1961 - 2010
│   ├── curses;
│   │   └── google_twunter.txt; official list of curse words by Google
│   ├── msd;
│   │   ├── msd_raw; 1% of the entire MillionSongDataset
│   │   ├── msd_files.txt; paths to all the MSD files
│   │   ├── msd_tid.txt; tids mapped to the MSD files
│   │   └── msd_tid_year.txt; tids and year mapped to the MSD files
│   └── mxm;
│       └── mxm_raw; entire musiXmatch dataset
│           ├── mxm_779k_matches.txt; maps the 77.9% of the resolved MillionSongDataset
│           ├── mxm_dataset_test.txt; test set
│           ├── mxm_dataset_train.txt; training set
│           └── mxm.txt; joined set
│
├── final; final datasets to be used in the frontend analysis
│   ├── features
│   │   ├── adj.json; indexed adjectives in the bag of words
│   │   ├── curses.json; indexed curse words in the bag of words
│   │   ├── nouns.json; indexed nouns in the bag of words
│   │   ├── stopwords.json; indexed stopwords in the bag of words
│   │   ├── syllables.json; indexed syllables for the bag of words
│   │   └── verbs.json; indexed verbs in the bag of words
│   ├── bow.txt; bag of words used in the musiXmatch dataset
│   ├── charted.txt; tids, titles, lyrics and years of the charted songs
│   ├── final.csv; final dataset
│   └── uncharted.txt; tids, titles, lyrics and years of the uncharted songs
│
└── transitional; transitional datasets
    ├── charted;
    │   ├── charted_failed.txt; charted songs that did not have a tid
    │   ├── charted_mxm.txt; charted songs that did have a tid
    │   ├── charted_tid.txt; tids of the charted songs
    │   ├── charted_tid_title.txt; tids and titles of the charted songs
    │   └── charted_tid_year_title.txt; tids, titles and years of the charted songs
    ├── extra_db; extra databases compiled for very temporary uses
    │   ├── more0.txt; uncharted dataset temp
    │   ├── more0_failed.txt; uncharted dataset temp
    │   ├── more0_f.txt; uncharted dataset temp
    │   ├── more1.txt; charted dataset temp
    │   ├── more1_failed.txt; charted dataset temp
    │   ├── more1_f.txt; charted dataset temp
    │   └── uncharted_f.txt; uncharted dataset temp
    └── mxm;
        ├── MSD_mxm.txt; intersection of mxm and MSD
        ├── mxm_filtered_raw.txt; curtailed mxm
        ├── mxm_filtered.txt; curtailed mxm
        └── mxm_tid.txt; only tids of the entire set

11 directories, 36 files
```

## Diagram of the datasets

![](https://github.com/kug3lblitz/Heat-Replay/blob/master/static/db_diagram.png)
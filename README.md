# Heat Replay <img src="https://github.com/kug3lblitz/Heat-Replay/blob/master/src/assets/static/logo.png" width=100px>

A data science project that will attempt to determine if the lyrical content of a song can predict 
if it will hit the Billboard Year-End Hot 100 singles. The project will intersect several datasets to create a final
dataframe that will consist of songs that charted and those that did not chart, with each comprising almost 50% of 
the set, along with the bag of words version of their lyrics and the analyses on them, such as sentiment analysis, 
frequency of obscene words, frequency of words pertaining to certain themes, total number of unique words, etc. and 
the year they charted. The dataframe will also include the last column 'charted', a binary variable that corresponds
to the chart status of the song.

## Structure of features

1. Track information
  1. Year (int)
  2. Decade (int)

2.  Lyrical content
  1. Unique Words, w/o stopwords (int)
  2. Density, w/o stopwords (int)
  3. Unique Words, w/ stopwords (int)
  4. Density, w/ stopwords (int)
  5. Nouns (int)
  6. Verbs (int)
  7. Adjectives (int)
  8. Syllables (int)
  9. Most used term (string)
  10. Most used frequency (int)
  11. Curses (binary)
  12. Total curses (int)
  13. Reading score (float)
  14. Sentiment (float)

3.  Chart
  1.  Charted (binary)

## Structure of repository
```
src
├── data; the datasets for the project
├── code; scripts to build the datasets
└── assets; static files and docs

23 directories, 60 files
```

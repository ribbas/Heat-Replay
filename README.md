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

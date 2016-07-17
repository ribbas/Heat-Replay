from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

stry = 'love know like get see got feel want way take would ca babi thing caus think good ya much better mean lose enough touch sure ani chanc lot secret knock lovin thunder wood lightn frighten tranc spinnin'

print sid.polarity_scores(stry)['compound']

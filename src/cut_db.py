from settings import *

print DATA_DIR
RAW_DIR = DATA_DIR + 'mxm/{file}.txt'
MXM_PATH = RAW_DIR.format(file='mxm_779k_matches')

# LYRICS_DIR = '../lyrics/'
# LYRICS_PATH = LYRICS_DIR + '{year}/{file}.txt'

# LISTS_DIR = '../lists/'
# INIT_LIST_PATH = LISTS_DIR + 'songList.txt'
# FAILURE_PATH = LISTS_DIR + 'temp_failed.txt'
# QUEUE_PATH = LISTS_DIR + 'queue.txt'


def newFrame(start):

    with open(MXM_PATH) as lyricsFile:

        rawNewFrame = ''

        # to avoid the entire file from being read into memory
        # (enumerate(x) uses x.next)
        for lineNum, line in enumerate(lyricsFile):

            if lineNum >= start and lineNum <= (start + 100):
                rawNewFrame += line

    return filter(None, ['<SEP>'.join(row.split('<SEP>')[4:6])
                         for row in rawNewFrame.split('\n')])


# def __saveProgress(queue, success, failed):

#     newQueue = sorted(queue - success - failed)

#     fileManager(FAILURE_PATH, 'a', output='\n'.join(sorted(failed)))
#     fileManager(QUEUE_PATH, 'w', output='\n'.join(newQueue))

#     if len(newQueue):
#         exit('\n' + str(len(newQueue)) +
#              ' songs left.\nSaving progress.')

#     exit('Queue is empty, scraping completed!')


# def scrape():

#     rawFile = fileManager(path, 'r')
#     success = set()
#     failed = set()

#     for line in rawFile:

#         try:
#             song = Lyrics(line)
#             song.scrape()
#             lyrics = song.lyrics

#             if lyrics:
#                 fileManager(
#                     LYRICS_PATH.format(
#                         year=line.split('/')[0],
#                         file=song.name
#                     ), 'w', song.lyrics
#                 )
#                 success.add(line)

#             else:
#                 failed.add(line)

#         except KeyboardInterrupt:
#             break

#         except Exception as e:
#             print e
#             continue

#     __saveProgress(set(rawFile), success, failed)


print newFrame(18)

from settings import *

raw = True


def loadSet(fileName):

    setName = set()

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            if lineNum:
                setName.add(line)

    return setName

if __name__ == '__main__':

    chartedSet = loadSet(CHARTED)

    filteredMXM = [
        sep.join(col.split(sep)[1:3]) for col in loadSet(FILTERED_MXM_RAW)
    ]

    trackIDs = [col.split(sep)[0] for col in loadSet(FILTERED_MXM_RAW)]

    intersections = sorted(list(chartedSet & set(filteredMXM)))

    filteredTrackIDs = []

    for title in range(len(intersections)):
        if intersections[title] in filteredMXM:
            filteredTrackIDs.append(
                trackIDs[filteredMXM.index(intersections[title])]
            )

    # disjoints = sorted(list(loadSet(CHARTED) - loadSet(FILTERED_MXM)))

    fileManager(CHARTED_TIDS, 'w', '\n'.join(sorted(filteredTrackIDs)))
    # fileManager(CHARTED_FAIL, 'w', ''.join(disjoints))

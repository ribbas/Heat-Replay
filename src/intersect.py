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

    filteredMXMSet = [
        sep.join(col.split(sep)[1:3]) for col in loadSet(FILTERED_MXM_RAW)
    ]

    trackIDs = [col.split(sep)[0] for col in loadSet(FILTERED_MXM_RAW)]

    intersections = sorted(list(chartedSet & set(filteredMXMSet)))

    filteredTrackIDs = []

    for title in range(len(intersections)):
        if intersections[title] in filteredMXMSet:
            filteredTrackIDs.append(
                trackIDs[filteredMXMSet.index(intersections[title])]
            )

    disjoints = sorted(list(chartedSet - set(filteredMXMSet)))

    fileManager(CHARTED_TIDS, 'w', '\n'.join(sorted(filteredTrackIDs)))
    fileManager(CHARTED_MXM, 'w', ''.join(intersections))
    fileManager(CHARTED_FAIL, 'w', ''.join(disjoints))

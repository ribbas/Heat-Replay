from context import settings
from settings.filemgmt import fileManager
from settings.paths import CHARTED, CHARTED_FAIL, CHARTED_MXM, \
    CHARTED_TIDS, FILTERED_MXM_RAW, sep


def loadSet(fileName):

    setName = set()

    with open(fileName) as lyricsFile:

        # to avoid the entire file from being read into memory
        for line in lyricsFile:
            setName.add(line)

    return setName


def phaseOne():

    chartedSet = loadSet(CHARTED)

    filteredMXMSet = [
        sep.join(col.split(sep)[1:3]) for col in loadSet(FILTERED_MXM_RAW)
    ]

    return filteredMXMSet, chartedSet


def phaseTwo():

    chartedSet = [
        col.replace(' ', '')
        for col in loadSet(CHARTED_FAIL)
    ]

    filteredMXMSet = [
        sep.join(col.replace(' ', '').split(sep)[1:3])
        for col in loadSet(FILTERED_MXM_RAW)
    ]

    return filteredMXMSet, set(chartedSet)


def choosePhase(phase):

    filteredTrackIDs = []
    filteredMXMSet = ''
    chartedSet = ''

    trackIDs = [col.split(sep)[0] for col in loadSet(FILTERED_MXM_RAW)]

    if phase == 1:
        filteredMXMSet = phaseOne()[0]
        chartedSet = phaseOne()[1]
    elif phase == 2:
        filteredMXMSet = phaseTwo()[0]
        chartedSet = phaseTwo()[1]

    disjoints = sorted(list(chartedSet - set(filteredMXMSet)))

    intersections = sorted(list(chartedSet & set(filteredMXMSet)))

    for title in range(len(intersections)):
        if intersections[title] in filteredMXMSet:
            filteredTrackIDs.append(
                trackIDs[filteredMXMSet.index(intersections[title])]
            )

    intersections = ''.join(intersections)
    disjoints = ''.join(disjoints)
    filteredTrackIDs = '\n'.join(sorted(filteredTrackIDs))

    fileManager(CHARTED_MXM, 'w', intersections)
    fileManager(CHARTED_FAIL, 'w', disjoints)
    fileManager(CHARTED_TIDS, 'a', filteredTrackIDs)


if __name__ == '__main__':

    choosePhase(1)

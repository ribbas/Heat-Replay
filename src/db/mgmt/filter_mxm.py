from settings.filemgmt import fileManager
from settings.paths import FILTERED_MXM_RAW, MXM_INDEX, sep
from settings.regexify import compileTitleRe, regexify


def newFrame(colStart, colEnd, raw=False):

    newFrame = []
    compileTitleRe()

    with open(MXM_INDEX) as lyricsFile:

        rawNewFrame = ''
        start = 18

        # to avoid the entire file from being read into memory
        for lineNum, line in enumerate(lyricsFile):

            if lineNum >= start:
                rawNewFrame += line

    for row in rawNewFrame.split('\n'):

        try:

            rowSplit = sep.join(
                [row.split(sep)[0]] +
                [regexify(col)
                 for col in row.split(sep)[colStart:colEnd]]
            ) if raw else sep.join(
                [regexify(col)
                 for col in row.split(sep)[colStart:colEnd]]
            )

            newFrame.extend([rowSplit])

        except Exception:
            continue

    return '\n'.join(sorted(set(filter(None, newFrame))))

fileManager(FILTERED_MXM_RAW, 'w', newFrame(4, 6, True))

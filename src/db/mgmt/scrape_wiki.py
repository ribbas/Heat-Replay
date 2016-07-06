from bs4 import BeautifulSoup
from requests import get

from context import settings
from settings.filemgmt import fileManager
from settings.paths import CHARTED2, sep
from settings.regexify import *

WIKI_URL = 'https://en.wikipedia.org/'
BASE_URL = WIKI_URL + 'wiki/Billboard_Year-End_Hot_100_singles_of_{year}'

titleTag = r'<a.*?>(.+?)</a>'
titleTagRe = compile(titleTag)
falseTag = r'<td>\d+</td>'
falseTagRe = compile(falseTag)

__sep = ''


def iterateYears(begin, end):

    chartRange = xrange(begin, end + 1)

    scrapedHTML = []

    for year in chartRange:
        html = get(BASE_URL.format(year=str(year)))
        if html.status_code == 200:
            scrapedHTML.append(html.text)

    return scrapedHTML


def soupify(html, charted):

    compileTitleRe()

    soup = BeautifulSoup(html, 'html.parser')

    songs = []

    for entrySoup in soup.find_all('table', {'class': 'wikitable sortable'}):
        for songSoup in entrySoup.find_all('tr'):

            mixedSoup = songSoup.find_all('td')

            try:

                titles = titleTagRe.findall(mixedSoup[1].encode('utf-8')) \
                    if falseTagRe.findall(mixedSoup[0].encode('utf-8')) \
                    else titleTagRe.findall(mixedSoup[0].encode('utf-8'))

                artists = titleTagRe.findall(mixedSoup[2].encode('utf-8')) \
                    if falseTagRe.findall(mixedSoup[0].encode('utf-8')) \
                    else titleTagRe.findall(mixedSoup[1].encode('utf-8'))

                if charted == 1:

                    __sep = sep
                    songs.append(
                        __sep.join(
                            regexify(song) for song in
                            [artists[0]] + [titles[0]]
                        )
                    )

                elif charted == 2:

                    __sep = '-'
                    songs.append(
                        '2060/' +
                        '-lyrics-'.join(
                            regexify(song) for song in
                            [titles[0]] + [artists[0]]
                        ).replace(' ', __sep).partition('-featuring')[0]
                    )

            except IndexError:
                continue

            except Exception as e:
                print e
                continue

    return songs


if __name__ == '__main__':

    charts = iterateYears(2011, 2015)

    charted = []

    for chart in charts:
        charted.extend(song for song in soupify(chart, 1) if __sep in song)

    charted = '\n'.join(sorted(set(charted)))

    fileManager(CHARTED2, 'w', charted)

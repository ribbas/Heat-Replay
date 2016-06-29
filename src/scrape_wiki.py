from re import compile

from bs4 import BeautifulSoup
from requests import get

from settings import *

WIKI_URL = 'https://en.wikipedia.org/'
BASE_URL = WIKI_URL + 'wiki/Billboard_Year-End_Hot_100_singles_of_{year}'
titleTag = r'<a.*?>(.+?)</a>'
titleTagRe = compile(titleTag)
falseTag = r'<td>\d+</td>'
falseTagRe = compile(falseTag)


def iterateYears(begin, end):

    chartRange = xrange(begin, end + 1)

    scrapedHTML = []

    for year in chartRange:
        html = get(BASE_URL.format(year=str(year)))
        if html.status_code == 200:
            scrapedHTML.append(html.text)

    return scrapedHTML


def soupify(html):

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

                songs.append(
                    '<SEP>'.join(
                        song.lower() for song in [artists[0]] + [titles[0]]
                    )
                )

            except IndexError:
                continue

            except Exception as e:
                print e
                continue

    return songs


if __name__ == '__main__':

    charts = iterateYears(1961, 2010)

    charted = []

    for chart in charts:
        charted.extend(song for song in soupify(chart) if '<SEP>' in song)

    fileManager('charted.txt', 'w', '\n'.join(sorted(set(charted))))

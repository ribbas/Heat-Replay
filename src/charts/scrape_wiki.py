from re import compile

from bs4 import BeautifulSoup
from requests import get

WIKI_URL = 'https://en.wikipedia.org/'
BASE_URL = WIKI_URL + 'wiki/Billboard_Year-End_Hot_100_singles_of_{year}'
titleTag = r'<a.*?>(.+?)</a>'
titleTagRe = compile(titleTag)


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
            yoSoup = songSoup.find_all('td')
            try:
                songs.append('<SEP>'.join(titleTagRe.findall(str(yoSoup[1])) +
                                          titleTagRe.findall(str(yoSoup[0]))))
            except Exception as e:
                print e
                continue

    print songs

test = iterateYears(1960, 1980)

for i in test:
    soupify(i)

# soupify(test)

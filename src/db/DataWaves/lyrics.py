#!/usr/bin/env python

from lxml.html import fromstring
from requests import get

BASE_URL = 'http://www.metrolyrics.com/{url}.html'


class Lyrics:

    def __init__(self, url):

        self.lyrics = None
        self.name = url

        self._url = BASE_URL.format(url=url)

    def scrape(self):
        """Load the lyrics from MetroLyrics.
        """

        print "Scraping lyrics for", self.name
        page = get(self._url)

        if page.status_code != 404:
            print 'Page found for', self.name
            page = fromstring(page.text)

            try:
                lyric_div = page.get_element_by_id('lyrics-body-text')
                verses = [c.text_content().encode("utf-8") for c in lyric_div]
                self.lyrics = '\n\n'.join(verses)

            except Exception as e:
                print e
                self.lyrics = ''

        else:
            print 'Page not found'

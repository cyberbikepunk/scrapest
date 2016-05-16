""" This module adds and removes webpages from the tests. """

from hashlib import sha1
from logging import getLogger
from os.path import join, isfile

from bs4 import BeautifulSoup
from requests import get
from slugify import slugify

from scrapest.scaffolding import scaffold

log = getLogger(__name__)

XML_PARSER = 'lxml'


class WebpageError(Exception):
    pass


class WebPage(object):
    def __init__(self, url, encoding='utf-8', *parsers):
        self.url = url
        self.parsers = parsers
        self.encoding = encoding
        self.response = None
        self.source = None
        self.soup = None

    def add(self):
        self._download()
        self._soupify()
        self._save_to_cache()

    def _download(self):
        self.response = get(self.url)
        if not self.response.status_code == 200:
            message = 'Could not download %s (%s)' % (self.url, self.response.status_code)
            raise WebpageError(message)
        else:
            log.debug('Downloaded %s', self.url)

    def _soupify(self):
        # TODO: Choose a specific parser and stick to it.
        # TODO: Raise a more specific exception when running into parsing problems
        # noinspection PyBroadException
        try:
            self.soup = BeautifulSoup(self.response.text, XML_PARSER)
            self.source = self.soup.prettify()
            log.debug('Soupified %s', self.title)
        except Exception:
            raise WebpageError('Could not parse %s' % self.url)

    def _save_to_cache(self):
        if self.is_cached:
            log.warn('Overwriting %s', self.filepath)
        with open(self.filepath, 'w+') as file:
            file.write(self.source)
            log.debug('Saved %s to cache', self.filepath)

    @property
    def is_cached(self):
        return isfile(self.filepath)

    @property
    def filepath(self):
        if not scaffold.is_created:
            raise WebpageError('Run init sub-command first')
        return join(scaffold.cache_dir, slugify(self.title) + '.html')

    @property
    def id(self):
        return sha1(self.url).digest(digest_size=7)

    @property
    def title(self):
        return self.scrub(self.soup.find('title').string)

    @staticmethod
    def scrub(text):
        return text.replace('\n', '').strip()

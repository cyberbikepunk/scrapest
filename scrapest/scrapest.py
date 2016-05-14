"""Scrapest is a testing framework for Scrapy.

Usage:
    scrapest
    scrapest init
    scrapest add URL
    scrapest remove URL

"""

from __future__ import print_function
from docopt import docopt
from logging import basicConfig, getLogger, DEBUG


basicConfig(format='[%(module)s] %(message)s', level=DEBUG)
log = getLogger(__name__)


def scrub_keys(raw_kwargs):
    return {
        key.lower().lstrip('--').lstrip('<').rstrip('>'): value
        for key, value in raw_kwargs.items()
        }


def build_scaffolding():
    log.debug('Building test scaffolding')


def cache_webpage(url):
    log.debug('Caching %s', url)


def uncache_webpage(url):
    log.debug('Uncaching %s', url)


def dispatch_command(init=False, add=False, remove=False, url=None):
    if init:
        build_scaffolding()
    elif add:
        cache_webpage(url)
    elif remove:
        uncache_webpage(url)
    else:
        print(__doc__)


if __name__ == '__main__':
    kwargs = scrub_keys(docopt(__doc__))
    log.debug('Command line arguments = %s', kwargs)
    dispatch_command(**kwargs)

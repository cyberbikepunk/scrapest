""" Scrapest is a testing framework for Scrapy.

Usage:
    scrapest init
    scrapest add URL
    scrapest remove URL

"""

from __future__ import print_function
from docopt import docopt
from logging import basicConfig, getLogger, DEBUG


basicConfig(format='[%(module)s] %(message)s', level=DEBUG)
log = getLogger(__name__)


def scrub_keys(raw_args):
    return {
        key.lower().lstrip('--').lstrip('<').rstrip('>'): value
        for key, value in raw_args.items()
    }


if __name__ == '__main__':
    args = scrub_keys(docopt(__doc__))
    log.debug('Command line arguments = %s', args)

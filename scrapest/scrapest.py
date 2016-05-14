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


def parse_args(args):
    return {k.lower(): v for k, v in args.items()}


if __name__ == '__main__':
    cli_args = parse_args(docopt(__doc__))
    log.debug('%s', dict(cli_args))


""" Scrapest is a testing framework for Scrapy.

Usage:
    scrapest init
    scrapest add URL
    scrapest remove URL

"""

from __future__ import print_function

from docopt import docopt

args = docopt(__doc__)
print(args)


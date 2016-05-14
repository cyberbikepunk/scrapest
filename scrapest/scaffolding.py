""" The scaffolder module builds the skeleton for the test framework."""


from logging import getLogger
from os import getcwd, listdir, makedirs
from os.path import abspath, join, isdir
from sys import exit


log = getLogger('scrapest.scaffolding')

test_dir = 'tests'
cache_dir = 'scrapest_cache'
cache_path = join(test_dir, cache_dir)


class ScaffoldingError(Exception):
    pass


def build_scaffolding():
    """ Build a skeleton for test framework.

    The skeleton consists of:
        1. A cache for web-pages
        2. A pytest module ready to go

    The function assumes a standard Scrapy file structure.

    """

    current_dir = abspath(getcwd())
    subdirectories = listdir(current_dir)

    log.debug('Building test scaffolding')
    log.debug('Current directory is %s', current_dir)
    log.debug('Subdirectories: %s', list(subdirectories))

    # TODO: write pytests for the folder creation logic

    if '.git' not in subdirectories:
        raise ScaffoldingError('scrapest must be run from the root of the Scrapy project')

    if isdir(cache_path):
        log.info('Test scaffold already exists: exiting')
        exit(0)

    if isdir(test_dir):
        log.debug('Using existing directory "%s"', test_dir)

    try:
        makedirs(cache_path)
        log.debug('Created the cache %s', cache_path)
    except IOError:
        raise ScaffoldingError('I/O problem creating %s', cache_path)

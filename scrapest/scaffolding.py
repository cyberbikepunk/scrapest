""" The scaffolder module builds the skeleton for the test framework."""


from logging import getLogger


log = getLogger('scrapest.scaffolding')


def build_scaffolding():
    """ Build a skeleton for test framework.

    The skeleton consists of:
        1. A cache for web-pages
        2. A pytest module ready to go

    The function assumes a standard Scrapy file structure.

    """
    log.debug('Building test scaffolding')

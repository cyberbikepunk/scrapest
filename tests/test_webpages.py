""" Unit-tests for the Webpage class. """

from pytest import fixture

from scrapest.webpages import WebPage

TEST_PAGE = 'http://blog.cyberpunk.bike/blog/learning-python-the-social-way'


@fixture
def webpage():
    return WebPage(TEST_PAGE)


# noinspection PyShadowingNames
def test_filepath(webpage):
    assert webpage.filepath == 'learning-python-the-social-way.html'

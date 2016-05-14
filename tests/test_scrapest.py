""" The test module (pytest + tox). """


from scrapest.scrapest import scrub_keys


def test_scrub_keys():
    values = ['foo', 'bar', 'spam', 'eggs']
    args_in = dict(zip(['--foo', 'BAR', '<spam>', 'eggs'], values))
    args_out = dict(zip(['foo', 'bar', 'spam', 'eggs'], values))
    assert scrub_keys(args_in) == args_out

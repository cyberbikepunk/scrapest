""" The test module (pytest + tox). """

from __future__ import print_function
from mock import patch
from pytest import mark
from scrapest.scrapest import scrub_keys, dispatch_command, __doc__ as docstring


def test_scrub_keys():
    values = ['foo', 'bar', 'spam', 'eggs']
    args_in = dict(zip(['--foo', 'BAR', '<spam>', 'eggs'], values))
    args_out = dict(zip(['foo', 'bar', 'spam', 'eggs'], values))
    assert scrub_keys(args_in) == args_out


dispatching_tests = [
    ({'init': True, 'add': False, 'remove': False, 'url': None},
     'build_scaffolding', [], {}),
    ({'init': False, 'add': True, 'remove': False, 'url': 'http://dummy.com'},
     'cache_webpage', ['http://dummy.com'], {}),
    ({'init': False, 'add': False, 'remove': True, 'url': 'http://dummy.com'},
     'uncache_webpage', ['http://dummy.com'], {})
]


# noinspection PyShadowingNames
@mark.parametrize('params, function_name, args, kwargs', dispatching_tests)
def test_dispatch_command(params, function_name, args, kwargs):
    function_path = 'scrapest.scrapest.%s' % function_name
    with patch(function_path, return_value=None) as function:
        dispatch_command(**params)
        function.assert_called_once_with(*args, **kwargs)


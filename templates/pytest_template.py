# # coding=utf-8
# """ Unittests for the hhgregg spider. """
#
# from loic_scrapinghub_trial.items import ProductLoader, Product
# from loic_scrapinghub_trial.spiders.hhgregg import ProductParser
# from loic_scrapinghub_trial.tests.cache.canon_9543B001 import URL, HTML, SCRAPED_FIELDS, UNSCRAPED_FIELDS
# from pytest import fixture, mark, raises
# from scrapy import Request
# from scrapy.http import HtmlResponse
#
#
# class BootstrapedParser(ProductParser):
#     # noinspection PyShadowingNames
#     def __init__(self, url, html):
#         self.url = url
#         self.html = html
#         self.request = Request(url=url)
#         self.response = HtmlResponse(self.url, body=self.html, request=self.request, encoding=self.encoding)
#         self.product = ProductLoader(item=Product(), response=self.response)
#         super(BootstrapedParser, self).__init__(self.response)
#
#     def __repr__(self):
#         return '<Bootstraped ProductParser (%s)>' % self.url
#
#
# @fixture
# def product_item():
#     parser = BootstrapedParser(URL, HTML)
#
#     parser.parse_website_info()
#     parser.parse_prices()
#     parser.parse_basic_product_info()
#     parser.parse_specifications()
#     parser.parse_image_links()
#     parser.parse_features()
#     parser.parse_hidden_product_info()
#
#     return parser.product.load_item()
#
#
# # noinspection PyShadowingNames
# @mark.parametrize('field_name, expected_value', SCRAPED_FIELDS)
# def test_input_output_processors(product_item, field_name, expected_value):
#     assert product_item[field_name] == expected_value
#
#
# # noinspection PyShadowingNames
# @mark.parametrize('field_name', UNSCRAPED_FIELDS)
# def test_unscraped_fields(product_item, field_name):
#     with raises(KeyError):
#         assert product_item[field_name]

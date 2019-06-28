# -*- coding: utf-8 -*-
import scrapy


class MotorhomesSpider(scrapy.Spider):
    name = 'motorhomes'
    allowed_domains = ['https://newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/rva?postedToday=1']

    def parse(self, response):
        pass

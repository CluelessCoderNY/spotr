# -*- coding: utf-8 -*-
import scrapy


class MotorhomesSpider(scrapy.Spider):
    name = 'motorhomes'
    allowed_domains = ['https://newyork.craigslist.org']
    start_urls = ['https://newyork.craigslist.org/search/rva?postedToday=1']

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            date = listing.xpath(
                './/*[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath(
                './/a[@class="result-title hdrlnk"]/@href').extract_first()
            text = listing.xpath(
                './/a[@class="result-title hdrlnk"]/text()').extract_first()

            yield {
                'date': date,
                'link': link,
                'text': text
            }

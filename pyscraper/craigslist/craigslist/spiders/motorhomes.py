# -*- coding: utf-8 -*-
import scrapy


class MotorhomesSpider(scrapy.Spider):
    name = 'motorhomes'

    # todo: get all active start urls
    start_urls = ['https://newyork.craigslist.org/search/rva?postedToday=1']

    def parse(self, response):
        listings = response.xpath('//li[@class="result-row"]')
        for listing in listings:
            date = listing.xpath(
                './/*[@class="result-date"]/@datetime').extract_first()
            link = listing.xpath(
                './/a[@class="result-title hdrlnk"]/@href').extract_first()
            listingTitle = listing.xpath(
                './/a[@class="result-title hdrlnk"]/text()').extract_first()

            yield scrapy.Request(link,
                                 callback=self.parse_listing,
                                 meta={
                                     "date": date,
                                     "link": link,
                                     "listingTitle": listingTitle})

        # next_page_url = response.xpath(
        #     '//a[text()="next > "]/@href').extract_first()
        # if next_page_url:
        #     yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse, dont_filter=True)

    def parse_listing(self, response):
        date = response.meta["date"]
        link = response.meta["link"]
        listingTitle = response.meta["listingTitle"]

        listingAttrs = response.xpath(
            '//*[@class="attrgroup"]/span/b/text()').extract()

        images = response.xpath('//*[@id="thumbs"]//@src').extract()
        images = [image.replace("50x50c", "600x450") for image in images]

        rawDescriptions = response.xpath(
            '//*[@id="postingbody"]/text()').extract()

        description = ""

        for desc in rawDescriptions:
            description += desc.replace('\n', '')

        # todo: put current start url in this object
        yield{
            "date": date,
            "link": link,
            "listingTitle": listingTitle,
            "listingAttrs": listingAttrs,
            "images": images,
            "description": description
        }

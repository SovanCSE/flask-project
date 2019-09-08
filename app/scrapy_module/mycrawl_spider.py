# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MycrawlSpiderSpider(CrawlSpider):
    name = 'mycrawl_spider'
    allowed_domains = ['www.tripadvisor.in']
    start_urls = ['https://www.tripadvisor.in/Tourism-g2-Asia-Vacations.html']
    #
    # rules = (
    #     Rule(LinkExtractor(), callback='parse_item', follow=False),
    # )

    def parse_item(self, response):
        item = {"img": response.xpath('.//img').get()}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield item

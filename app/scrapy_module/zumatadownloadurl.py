#scrapy module
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess


class DownloadInventorySpider(CrawlSpider):
    name = 'download_zumatainver'
    # allow_domains = ['dev.zumata.com']

    def start_requests(self):
        yield scrapy.Request('dev.zumata.com/athena/index.html', callback=self.parse,  errback=self.your_errorback)

    def parse(self, response):
        print("pppp", response.request.url)
        download_url = response.xpath('//a[contains(@href,"zumata_active_properties_list")]/@href').extract()
        print("download_url", download_url)

    def your_errorback(self, response):
        print("oooo", response)



if __name__ == '__main__':
    process = CrawlerProcess()

    process.crawl(DownloadInventorySpider)
    process.start()
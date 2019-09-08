# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
import MySQLdb
from scrapy.crawler import CrawlerProcess


class MyItem(scrapy.Item):
    status = scrapy.Field()



class YatrapiSpider(CrawlSpider):
    name = 'yatrapi'
    allowed_domains = ['hotel.yatra.com']

    def start_requests(self):
        headers = {'Content-Type':'application/json', 'X-API-KEY':'JN9aWyj7hJ1ZrExC7Ozo', 'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
        hotelid_list = self.get_hotelidlist()

        for hotelid in hotelid_list:
            yield scrapy.Request('https://hotel.yatra.com/tgapi/hotels/v1/hotels/{}'.format(hotelid), headers=headers)

    def parse(self, response):
       print("Existing settings: %s" % self.settings)
       hotel_reponse = json.loads(response.text)
       item = MyItem()
       item['status'] = hotel_reponse.get('meta', {}).get('status','Failed')
       yield {'status': hotel_reponse.get('meta', {}).get('status','Failed')}
       # yield hotel_reponse

    @staticmethod
    def get_hotelidlist():
        try:
            db_connection = MySQLdb.connect('localhost', 'root', 'welcome', 'hotel_livedb')
            cursor = db_connection.cursor()
            sql = 'select hotel_unique_id from desiya_hotels'
            cursor.execute(sql)
            records = cursor.fetchall()
            hotelid_list = [record[0] for record in records]
            hotelid_list = ['00000002', '00000004', '00000005', '00000007', '00000010', '00000011', '00000012', '00000013', '00000014', '00000015']
            return hotelid_list
        except Exception as e:
            print("Error to connect db")


if __name__ == '__main__':
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'items.json',
        'CONCURRENT_REQUESTS': '1',
        'DOWNLOAD_DELAY':'5',
        'ITEM_PIPELINES':{
            'pipelines.MySQLStorePipeline': 1,
        }
    })

    process.crawl(YatrapiSpider)
    process.start()

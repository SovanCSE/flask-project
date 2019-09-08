from app import app
from app.scrapy_module.yatrapi import YatrapiSpider
from scrapy.crawler import CrawlerProcess
import os

@app.route('/')
def hello():
    os.system('python3 app/scrapy_module/yatrapi.py')
    return "hello sovan"

if __name__ == '__main__':
    app.run()


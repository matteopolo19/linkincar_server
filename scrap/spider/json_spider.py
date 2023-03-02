import json
import operator
import scrapy
from scrapy.http import Request

class JsonSpider(scrapy.Spider):
    name = "json_spider"
    def start_requests(self):
        print('start_requests - json_spider', self.url)
        yield Request(self.url)

    def parse(self, response):
        data = json.loads(response.body.decode('utf-8'))
        print("data found len", len(data.get(self.keyObject)))
        for i, car in enumerate(data.get(self.keyObject)):
            yield {
                'id':car.get("i"),
                'value':car.get("n"),
            }
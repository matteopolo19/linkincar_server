import json
import scrapy
from scrapy.http import Request

class AutoscoutSpider(scrapy.Spider):
    name = "autoscout"
    def start_requests(self):
        print('start_requests', self.url)
        yield Request(self.url)

    def parse(self, response):
        jdata = json.loads(response.css('script#__NEXT_DATA__::text').extract_first())
        for i, cars in enumerate(jdata["props"]["pageProps"]["listings"]):
            yield {
                "index": i,
                'id': cars["id"],
                'title': cars["vehicle"]['make']+" "+cars["vehicle"]['model']+" - "+cars["vehicle"]['modelVersionInput'] or None,
                'price': int(cars["tracking"]['price']) or None,
                'link': "https://www.autoscout24.fr"+cars['url'] or None,
                'kilometer': cars["vehicleDetails"][0] or None,
                'registration': cars["vehicleDetails"][1] or None,
                'power': cars["vehicleDetails"][2] or None,
                'status': cars["vehicleDetails"][3] or None,
                'gear': cars["vehicleDetails"][5] or None,
                'energy': cars["vehicleDetails"][6] if type(cars["vehicleDetails"][6]) == str else "",
                'consumption': cars["vehicleDetails"][7]["data"] or None,
                'emission': cars["vehicleDetails"][8]["data"] or None,
                'imgPath': cars["images"][0].replace('/250x188.webp','') if len(cars["images"]) else None,
                'webSite': "autoscout",
                "pages": int(response.css('ul li.pagination-item *::text').extract()[-1])
            }
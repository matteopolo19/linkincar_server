import json
import re
import scrapy
from scrapy.http import Request
from dict_deep import deep_get
class SubitoSpider(scrapy.Spider):
    name = "subito"
    def start_requests(self):
        print('start_requests - subito', self.url)
        yield Request(self.url)

    def parse(self, response):
        jdata = json.loads(response.css('script#__NEXT_DATA__::text').extract_first())
        result = jdata["props"]["state"]["items"]
        for i, cars in enumerate(result["list"]):
            car = cars["item"]
            features = car["features"]
            try:
                image = car["images"][0]["cdnBaseUrl"]+"?rule=card-desktop-new-large-1x-auto"
            except KeyError:
                print("error KeyError")
                image = None
            yield {
                "index": i,
                'id': car["urn"],
                'title': car["subject"] or None,
                'price': int(self.getObject(features, "/price.values", "key")),
                'link': car['urls']['default'] or None,
                'kilometer': self.getObject(features, "/mileage_scalar.values", "key"),
                'registration': self.getObject(features, "/register_date.values", "key"),
                'power': self.getObject(features, "/power.values", "value"),
                'status': self.getObject(features, "/vehicle_status.values", "value"),
                'gear': self.getObject(features, "/gearbox.values", "value"),
                'energy': self.getObject(features, "/fuel.values", "value"),
                'emission': self.getObject(features, "/pollution.values", "value"),
                'consumption': None,
                'imgPath': image,
                'webSite': "subito",
                "pages": result["totalPages"]
            }
    
    def getObject(self, obj, keys, lastKey):
        value = deep_get(obj, keys, list_of_len_one_as_value=True)
        if value != None and lastKey != None:
            return value[lastKey]
        return value
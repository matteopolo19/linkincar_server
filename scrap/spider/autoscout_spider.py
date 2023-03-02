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
            details = cars.get("vehicleDetails", [])
            vehicle = cars.get("vehicle")
            yield {
                "index": i,
                'id': cars["id"],
                'title': vehicle.get("make")+" "+vehicle.get("model")+" - "+vehicle.get("modelVersionInput") if vehicle != None else None,
                'price': int(cars.get("tracking").get("price")) or None,
                'link': "https://www.autoscout24.fr"+cars['url'] or None,
                'kilometer': self.getDataString(details[0]),
                'registration': self.getDataString(details[1]),
                'power': self.getDataString(details[2]),
                'status': self.getDataString(details[3]),
                'gear': self.getDataString(details[5]),
                'energy': self.getDataString(details[6]),
                'consumption':  self.getConsumption(details),
                'emission': self.getEmission(details),
                'imgPath': cars.get("images")[0].replace('/250x188.webp','') if len(cars["images"])>0 else None,
                'webSite': "autoscout",
                "pages": int(response.css('ul li.pagination-item *::text').extract()[-1])
            }

    def getDataString(self, obj):
        if(type(obj) == str):
            return obj
        elif obj != None:
            return obj.get('data')
        else: 
            return None

    def getConsumption(self, obj):
        value = obj[7].get('data') if obj[7] != None else None
        if type(value) == str:
            consum = value.split("|")
            return consum[1] if len(consum) >1 else None
        return value
    
    def getEmission(self, obj):
        value = obj[7].get('data') if obj[7] != None else None
        if type(value) == str:
            return value.split("|")[0] or None
        return value
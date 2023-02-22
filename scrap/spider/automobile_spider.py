import json
import re
import scrapy
from scrapy.http import Request

class AutomobileSpider(scrapy.Spider):
    name = "automobile"
    def start_requests(self):
        print('start_requests - automobile', self.url)
        yield Request(self.url)

    def parse(self, response):
        jdata = json.loads(response.css('script#__NEXT_DATA__::text').extract_first())
        result = jdata["props"]["pageProps"]["apiResults"]["result"]
        for i, cars in enumerate(result["resultList"]):
            try:
                image = cars["pictures"][0]["sizes"]["ORIG"]["href"],
            except KeyError:
                print("error KeyError")
                image = None
            yield {
                "index": i,
                'id': cars["id"],
                'title': cars["title"] or None,
                'price': int(re.sub(r'€ |\.','',cars["formattedPrice"])) or None,
                'link': "https://www.automobile.it" + cars['url'] or None,
                'kilometer': cars["details"]["formattedKm"] or None,
                'registration': cars["details"]["registration"] or None,
                'power': cars["details"]["formattedPower"] or None,
                'status': cars["channel"] or None,
                'gear': cars["details"]["shift"] or None,
                'energy': cars["details"]["fuelEmissions"] or None,
                'consumption': None,
                'emission': None,
                'imgPath': image[0],
                'webSite': "automobile",
                "pages": result["page"]["totalPages"]
            }
            
import scrapy
from scrapy.http import Request


class MobileSpider(scrapy.Spider):
    name = "mobile"
    def start_requests(self):
        print('start_requests - mobile', self.url)
        yield Request(self.url)

    def parse(self, response):
        print("response", response.body)
        for car in response.css('div.cBox--resultList'):
            print("car", car)
            yield {
                'id': car.css('a::attr(data-listing-id)').extract_first(),
                # 'title': cars["title"] or None,
                # 'price': int(re.sub(r'€ |\.','',cars["formattedPrice"])) or None,
                # 'link': "https://www.automobile.it" + cars['url'] or None,
                # 'kilometer': cars["details"]["formattedKm"] or None,
                # 'registration': cars["details"]["registration"] or None,
                # 'power': cars["details"]["formattedPower"] or None,
                # 'status': cars["channel"] or None,
                # 'gear': cars["details"]["shift"] or None,
                # 'energy': cars["details"]["fuelEmissions"] or None,
                # 'consumption': None,
                # 'emission': None,
                # 'imgPath': image[0],
                # 'webSite': "automobile",
                # "pages": result["page"]["totalPages"]
            }
            
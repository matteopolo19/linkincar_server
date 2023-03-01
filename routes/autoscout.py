from scrap.scrapy_process import  TwistedRunner, getSpiderResult
from scrap.spider.autoscout_spider import AutoscoutSpider

def autoscout(request):
    """Serve request for scrape"""
    Runner = TwistedRunner()
    url= "https://www.autoscout24.fr/lst"
    url += addArgumentToUrl('/', request.args.get(b'brand'))
    url += addArgumentToUrl('/',request.args.get(b'model'))
    url += '?sort=price&desc=0&damaged_listing=exclude'
    url += addArgumentToUrl('&pricefrom=',request.args.get(b'minPrice'))
    url += addArgumentToUrl('&priceto=',request.args.get(b'maxPrice'))
    url += addArgumentToUrl('&kmfrom=',request.args.get(b'minKm'))
    url += addArgumentToUrl('&kmto=',request.args.get(b'maxKm'))
    url += addArgumentToUrl('&page=',request.args.get(b'page'), '&page=1')
    print("autoscout :: url", url)
    a = Runner.crawl(AutoscoutSpider, url=url)
    a.addCallback(getSpiderResult)
    return a


def addArgumentToUrl(pre_string, argument, defaultValue=""):
    if(argument is None):
        return defaultValue
    else:
        return pre_string+argument[0].decode()
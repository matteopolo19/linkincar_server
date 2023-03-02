from scrap.scrapy_process import  TwistedRunner, getSpiderResult
from scrap.spider.mobile_spider import MobileSpider

def mobile(request):
    """Serve request for scrape"""
    Runner = TwistedRunner()
    url= "https://suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&ms=1900;8;;;&ref=dsp&s=Car&vc=Car"
    # url += addArgumentToUrl('/', request.args.get(b'brand'))
    # url += addArgumentToUrl('/',request.args.get(b'model'))
    # url += '?order=priceasc'
    # url += addArgumentToUrl('&o=',request.args.get(b'page'), '&o=1')
    # url += addArgumentToUrl('&ps=',request.args.get(b'minPrice'))
    # url += addArgumentToUrl('&pe=',request.args.get(b'maxPrice'))
    # url += addArgumentToUrl('&ms=',request.args.get(b'minKm'))
    # url += addArgumentToUrl('&me=',request.args.get(b'maxKm'))
    print("mobile :: url", url)
    a = Runner.crawl(MobileSpider, url=url)
    a.addCallback(getSpiderResult)
    return a


def addArgumentToUrl(pre_string, argument, defaultValue="", post_string=""):
    if(argument is None):
        return defaultValue
    else:
        return pre_string+argument[0].decode()+post_string
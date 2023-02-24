from scrap.scrapy_process import  TwistedRunner, getSpiderResult
from scrap.spider.subito_spider import SubitoSpider

def subito(request):
    """Serve request for scrape"""
    Runner = TwistedRunner()
    url= "https://www.subito.it/annunci-italia/vendita/auto"
    url += addArgumentToUrl('/', request.args.get(b'brand'))
    url += addArgumentToUrl('/',request.args.get(b'model'))
    url += '?order=priceasc'
    url += addArgumentToUrl('&o=',request.args.get(b'page'), '&o=1')
    url += addArgumentToUrl('&ps=',request.args.get(b'minPrice'))
    url += addArgumentToUrl('&pe=',request.args.get(b'maxPrice'))
    url += addArgumentToUrl('&ms=',request.args.get(b'minKm'))
    url += addArgumentToUrl('&me=',request.args.get(b'maxKm'))
    a = Runner.crawl(SubitoSpider, url=url)
    a.addCallback(getSpiderResult)
    return a


def addArgumentToUrl(pre_string, argument, defaultValue="", post_string=""):
    if(argument is None):
        return defaultValue
    else:
        return pre_string+argument[0].decode()+post_string
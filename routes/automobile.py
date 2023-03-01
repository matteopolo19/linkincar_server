from scrap.scrapy_process import  TwistedRunner, getSpiderResult
from scrap.spider.automobile_spider import AutomobileSpider

def automobile(request):
    """Serve request for scrape"""
    Runner = TwistedRunner()
    url= "https://www.automobile.it"
    url += addArgumentToUrl('/', request.args.get(b'brand'))
    url += addArgumentToUrl('-',request.args.get(b'model'))
    url += addArgumentToUrl('/page-',request.args.get(b'page'), '/page-1')
    url += '?tipo_di_veicolo=usate,nuove,km0'
    url += addArgumentToUrl('&prezzo_da=',request.args.get(b'minPrice'))
    url += addArgumentToUrl('&prezzo_a=',request.args.get(b'maxPrice'))
    url += addArgumentToUrl('&km_min=',request.args.get(b'minKm'), '', '_km')
    url += addArgumentToUrl('&km_max=',request.args.get(b'maxKm'), '', '_km')
    print("automobile :: url", url)
    a = Runner.crawl(AutomobileSpider, url=url)
    a.addCallback(getSpiderResult)
    return a


def addArgumentToUrl(pre_string, argument, defaultValue="", post_string=""):
    if(argument is None):
        return defaultValue
    else:
        return pre_string+argument[0].decode()+post_string
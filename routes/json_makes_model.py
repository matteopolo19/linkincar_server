from scrap.scrapy_process import  TwistedRunner, getSpiderResult
from scrap.spider.json_spider import JsonSpider

def jsonMakes():
    Runner = TwistedRunner()
    url= "https://m.mobile.de/svc/r/makes/Car?_lang=en"
    print("jsonMakes :: url", url)
    a = Runner.crawl(JsonSpider, url=url, keyObject="makes")
    a.addCallback(getSpiderResult)
    return a

def jsonModel(brand):
    Runner = TwistedRunner()
    url= "https://m.mobile.de/svc/r/models/"
    url += '/'+brand+"?_lang=en"
    print("jsonModel :: url", url)
    a = Runner.crawl(JsonSpider, url=url, keyObject="models")
    a.addCallback(getSpiderResult)
    return a
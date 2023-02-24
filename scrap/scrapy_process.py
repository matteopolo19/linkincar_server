import json
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy import signals

from .settings import settings

class TwistedRunner(CrawlerRunner):

    def crawl(self, Spider, *args, **kwargs):
        self.items = []

        # create spider instance
        crawler = self.create_crawler(Spider)
        crawler.signals.connect(self.storeItem, signals.item_scraped)

        # create deferred crawler-object and register callback
        deferred = self._crawl(crawler, *args, **kwargs)
        deferred.addCallback(self.getItems)
        return deferred

    def storeItem(self, item):
        self.items.append(item)

    def getItems(self, item):
        return self.items

def getSpiderResult(output):
    """Format spider result"""
    return json.dumps([dict(item) for item in output])
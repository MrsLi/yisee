# coding=utf-8
from scrapy.linkextractors import  LinkExtractor
from scrapy.spider import CrawlSpider,Rule
from yisee.items import YiseeItem
import  scrapy
from scrapy.selector import Selector
from scrapy.http import Request
class MyCrawlSpider(CrawlSpider):
    name = "yisee"
    host = "http://www.yi-see.com/"
    allowed_domains = ["yi-see.com"]
    start_urls = ["http://www.yi-see.com/artlist_1.html"]
    itemList = []
    length = 0

    link_extractor = LinkExtractor(restrict_xpaths=("//table//td[4]/div[@class='NEXT']/a/@href"))

    rules =[
        Rule(link_extractor,callback="",follow=True)
    ]
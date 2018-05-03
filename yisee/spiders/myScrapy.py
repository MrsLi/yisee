# coding=utf-8
import  scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from yisee.items import YiseeItem
class YiSee(scrapy.Spider):
    name = "yisee"
    host = "http://www.yi-see.com/"
    allowed_domains = ["yi-see.com"]
    start_urls = ["http://www.yi-see.com/artlist_1.html"]
    itemList = []
    length= 0

    # headers = {
    #     "Host": "onlinelibrary.wiley.com",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Referer": "http://onlinelibrary.wiley.com/journal/10.1002/(ISSN)1521-3773",
    #     "Cookie": "EuCookie='this site uses cookies'; __utma=235730399.1295424692.1421928359.1447763419.1447815829.20; s_fid=2945BB418F8B3FEE-1902CCBEDBBA7EA2; __atuvc=0%7C37%2C0%7C38%2C0%7C39%2C0%7C40%2C3%7C41; __gads=ID=44b4ae1ff8e30f86:T=1423626648:S=ALNI_MalhqbGv303qnu14HBk1HfhJIDrfQ; __utmz=235730399.1447763419.19.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; TrackJS=c428ef97-432b-443e-bdfe-0880dcf38417; OLProdServerID=1026; JSESSIONID=441E57608CA4A81DFA82F4C7432B400F.f03t02; WOLSIGNATURE=7f89d4e4-d588-49a2-9f19-26490ac3cdd3; REPORTINGWOLSIGNATURE=7306160150857908530; __utmc=235730399; s_vnum=1450355421193%26vn%3D2; s_cc=true; __utmb=235730399.3.10.1447815829; __utmt=1; s_invisit=true; s_visit=1; s_prevChannel=JOURNALS; s_prevProp1=TITLE_HOME; s_prevProp2=TITLE_HOME",
    #     "Connection": "keep-alive"
    # }

    def parse(self, response):
        #do something
        sel = Selector(response)
        sites = sel.xpath("//table//div[@class='T1']")
        next = sel.xpath("//table//td[4]/div[@class='NEXT']/a/@href").extract()[0]
        nextPageUrl = self.host+next
        length = len(sites)
        print(length)
        for site in sites:
            contentUrl = site.xpath("a/@href").extract()[0]
            contentNextUrl = self.host +contentUrl
            yield Request(contentNextUrl,callback=self.parse_content)
        yield scrapy.Request(nextPageUrl,callback=self.parse)

    #详情章节页
    def parse_content(self,response):
        print("爬去章节...")
        sel = Selector(response)

        selector = sel.xpath("//table//td[@valign='top']/a")
        for item in selector:
            yiseeItem = YiseeItem()
            yiseeItem['title'] = sel.xpath("//table//span[@class='T1']/b/text()").extract()[0]
            yiseeItem['author'] = sel.xpath("//table//span[@class='TA']/text()").extract()[0]
            zhangjieContent = item.xpath("@href").extract()[0]
            zhangjie = item.xpath("text()").extract()[0]
            zhangjieContentUrl = self.host+zhangjieContent
            yiseeItem['zhangjie'] = zhangjie
            yield scrapy.Request(zhangjieContentUrl,meta={'yiseeItem':yiseeItem},callback=self.parse_zhangjie_content)



    #章节内容
    def parse_zhangjie_content(self,response):
        print('爬去内容...')
        yiseeItem = response.meta['yiseeItem']
        sel = Selector(response)
        content = sel.xpath("//div[@class='ART']")[0].xpath('string(.)').extract()[0]
        yiseeItem['content'] = content
        yield yiseeItem



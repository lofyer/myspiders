from scrapy.selector import HtmlXPathSelector

from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from dirbot.items import Website

class DmozSpider(Spider):
    name = "chuzu"
    allowed_domains = ["xiaoji001.com"]
    start_urls = ["http://www.xiaoji001.com/gamelist-PS.html"]
    for i in range(2,112):
        new_page="http://www.xiaoji001.com/gamelist-PS-%s.html" %(i)
        start_urls.append(new_page)
    #rules = (
    #    Rule(LinkExtractor(restrict_xpaths='//div[@class="pager/a[@class="next"]'),
    #    callback = 'parse', follow = True)
    #)

    def parse(self, response):
        sel = HtmlXPathSelector(response)
        sites = sel.xpath("//ul[@class='xjlist']/li")
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath(".//div[@class='gameinfo']/p[@class='title']/a/text()").extract()
            item['url'] = site.xpath(".//div[@class='gameinfo']/p[@class='title']/a/@href").extract()
            item['info'] = site.xpath(".//div[@class='gameinfo']/p[@class='info']/text()").extract()
            items.append(item)

        return items

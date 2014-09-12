from scrapy.selector import HtmlXPathSelector

from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from dirbot.items import Website

class DmozSpider(Spider):
    name = "chuzu"
    allowed_domains = ["58.com"]
    start_urls = ["http://sh.58.com/chuzu/"]
    for i in range(2,70):
        new_page="http://sh.58.com/chuzu/pn%s" %(i)
        start_urls.append(new_page)
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pager/a[@class="next"]'),
        callback = 'parse', follow = True)
    )

    def parse(self, response):
        sel = HtmlXPathSelector(response)
        sites = sel.xpath("//table[@class='tbimg']/tr")
        items = []

        for site in sites:
            item = Website()
            item['description'] = site.xpath(".//td[@class='t qj-rentd']/h1/a[@class='t']/text()").extract()
            item['location'] = site.xpath(".//td[@class='t qj-rentd']/p[@class='qj-renaddr']/a[@class='a_xq1']/text()").extract()
            item['price'] = site.xpath(".//td[3]/b[@class='pri']/text()").extract()
            item['room'] = site.xpath(".//td[3]/span[@class='showroom']/text()").extract()
            item['url'] = site.xpath(".//td[@class='t qj-rentd']/h1/a[@class='t']/@href").extract()
            items.append(item)

        return items

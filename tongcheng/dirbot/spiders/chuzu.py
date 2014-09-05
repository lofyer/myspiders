from scrapy.selector import HtmlXPathSelector
from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from dirbot.items import Website


class DmozSpider(Spider):
    name = "chuzu"
    allowed_domains = ["58.com"]
    start_urls = ["http://sh.58.com/chuzu/"]
    for i in range(2,50):
        new_page="http://sh.58.com/chuzu/pn%s" %(i)
        start_urls.append(new_page)
    rules = (
        Rule(SgmlLinkExtractor(restrict_xpaths='//div[@class="pager/a[@class="next"]'),
        callback = 'parse', follow = True)
    )

    def parse(self, response):
        sel = HtmlXPathSelector(response)
        sites = sel.xpath("//table[@class='tbimg']/tr")
        items = []

        for site in sites:
            item = Website()
            item['description'] = site.xpath(".//td[@class='t qj-rentd']/h1/a[@class='t']/text()").extract()
            #item['url'] = site.xpath('a/@href').extract()
            #item['description'] = site.xpath('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        return items

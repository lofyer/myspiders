# -*- coding:utf-8 -*-
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

host='http://www.zhihu.com'

class ZhihuUserSpider(CrawlSpider):
	name = 'zhihu'
	allowed_domains = ['zhihu.com']
	start_urls = ["http://www.zhihu.com/lookup/people",]
	#使用rule时候，不要定义parse方法
	rules = (
		Rule(SgmlLinkExtractor(allow=("/lookup/class/[^/]+/?$", )), follow=True,callback='parse_item'),
		Rule(SgmlLinkExtractor(allow=("/lookup/class/$", )), follow=True,callback='parse_item'),
		Rule(SgmlLinkExtractor(allow=("/lookup/people", )),  callback='parse_item'),
	)

	def __init__(self,  *a,  **kwargs):
		super(ZhihuLoginSpider, self).__init__(*a, **kwargs)

	def start_requests(self):
		return [FormRequest(
			"http://www.zhihu.com/login",
			formdata = {'email':'XXXXXX',
			'password':'XXXXXX'
			},
		callback = self.after_login
		)]

	def after_login(self, response):
		for url in self.start_urls:
			yield self.make_requests_from_url(url)

	def parse_item(self, response):
		selector = Selector(response)
		for link in selector.xpath('//div[@id="suggest-list-wrap"]/ul/li/div/a/@href').extract():
			#link  ===> /people/javachen
			yield Request(host+link+"/about", callback=self.parse_user)
	def parse_user(self, response):
		selector = Selector(response)
	#抓取用户信息，此处省略代码

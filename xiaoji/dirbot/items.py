from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    info = Field()
    url = Field()
    #download_url = Field()

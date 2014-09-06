from scrapy.item import Item, Field


class Website(Item):

    description = Field()
    location = Field()
    room = Field()
    price = Field()
    url = Field()

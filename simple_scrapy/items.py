import scrapy
from itemloaders.processors import MapCompose, TakeFirst


def remove_charater_price(value):
    return float(value.replace(u"\u00a0", '').replace(',', ''))


def remove_charater_title(value):
    return value.replace(u"\u2019", '\'').replace(u"\u201c", '').replace(u"\u2019", '')


class ClothItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(remove_charater_title),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_charater_price),
        output_processor=TakeFirst()
    )
    img_url = scrapy.Field(
        output_processor=TakeFirst()
    )
    category = scrapy.Field(
        output_processor=TakeFirst()
    )

import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[contains(@class, "quote")]'):
            yield {
                'text': quote.xpath('span[contains(@class, text)]/text()').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.xpath('//li[contains(@class, "next")]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

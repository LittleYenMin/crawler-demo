import json

import requests
import lxml.html

start_url = 'http://quotes.toscrape.com'


def parse_quotes(response: requests.Response):
    tree = lxml.html.fromstring(response.content.decode('utf-8'))
    quotes = tree.xpath('//div[contains(@class, "quote")]')
    for quote in quotes:
        yield {
            'text': quote.xpath('./span[contains(@class, text)]/text()')[0],
            'author': quote.xpath('./span/small/text()')[0],
        }
    next_page = tree.xpath('//li[contains(@class, "next")]/a/@href')
    if next_page is not None and len(next_page) > 0:
        next_page = next_page[0]
        yield from parse_quotes(requests.get('{start_url}{sub_path}'.format(start_url=start_url, sub_path=next_page)))


def write_to_json(data):
    with open('common_demo.json', 'w', encoding='utf-8') as f:
        # set indent to 4 to output data beautifully.
        json.dump(data, f, indent=4)


def parse(url: str):
    response = requests.get(url)
    quotes = []
    for quote in parse_quotes(response):
        quotes.append(quote)
    write_to_json(quotes)


if __name__ == '__main__':
    parse('{}/tag/humor/'.format(start_url))

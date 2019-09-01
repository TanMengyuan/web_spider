import scrapy

class DmozSpider(scrapy.Spider):
    name = "tmy"
    start_urls = [
        "http://tmy.ink/?page_id=13"
    ]

    def parse(self, response):
        titles = response.xpath1('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())
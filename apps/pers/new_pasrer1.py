import scrapy


class BlogSpider(scrapy.Spider):
    name = 'gos'
    start_urls = ['http://zakupki.gov.kg/popp/view/plan/before-sign.xhtml', ]

    def parse(self, response):
        for div in response.text('//div'):
            yield { 'div_text': div.text('.//tr/td').get() }



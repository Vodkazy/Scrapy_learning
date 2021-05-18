import scrapy
from ..items import FactoryspiderItem


class FactorySpider(scrapy.Spider):
    name = 'factory'
    start_urls = ['http://xxxxxxxxxxx']

    def parse(self, response):
        factory_links = response.xpath('//*[@id="news"]/div[*]/div/div[1]/a/@href')
        yield from response.follow_all(urls=factory_links, callback=self.parse_fac)

        next_page_url = response.xpath('//*[@id="news"]/div[*]/ul[@class="pagination"]/ul/li[last()]/a/@href').get()
        if next_page_url is not None:
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_fac(self, response):
        item = FactoryspiderItem()
        item['name'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[1]/span/a/text()').get(default='').strip(),
        item['location'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[1]/p[2]/text()').get(default='').strip(),
        item['login_money'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[1]/p[4]/span/text()').get(default='').strip(),
        item['order_type'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[2]/p[2]/text()').get(default='').strip(),
        item['scale'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[3]/p[2]/text()').get(default='').strip(),
        item['main_category'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[4]/p[2]/a/text()').get(default='').strip(),
        item['type'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[5]/p[2]/span/text()').get(default='').strip(),
        item['product_level'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[5]/p[4]/span/text()').get(default='').strip(),
        item['produce_time'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div/div[2]/ul/li[5]/p[6]/span/text()').get(default='').strip(),
        item['img'] = response.xpath('//*[@id="small-banner"]/div/div[*]/a/img/@src').getall()
        yield item
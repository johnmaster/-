import scrapy

class CoursesSpider(scrapy.Spider):
    name = 'courses'

    start_urls = ['https://www.imooc.com/course/list']

    def parse(self, response):
        for course in response.xpath('//div[@class="course-card-container"]'):
            yield{
                'name':course.xpath('.//h3[@class="course-card-name"]/text()').extract_first(),
                'description':course.xpath('.//p[@class="course-card-desc"]/text()').extract_first(),
                'image_url':course.xpath('.//img/@src').extract_first()
                }
        for url in response.xpath('//a[10]/@href'):
            yield response.follow(url, callback=self.parse)


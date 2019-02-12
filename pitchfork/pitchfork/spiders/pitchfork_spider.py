# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy import Spider
from pitchfork.items import PitchforkItem
from scrapy import Request

    #def start_requests(self,response):

    # result_urls = ['https://pitchfork.com/reviews/albums/?page='].format(x) for x in range(1,number_pages+1)]
    # for now to test number_pages = 10

class PitchforkSpider(Spider):
    name = 'pitchfork_spider'
    allowed_urls = ['https://www.pitchfork.com/'] #could have multiple elements
    start_urls = ['https://pitchfork.com/reviews/albums/']

    def parse(self, response):
        number_pages = 1745
        result_urls = ['https://pitchfork.com/reviews/albums/?page={}'.format(x) for x in range(1,number_pages+1)]
        for url in result_urls:
            yield Request(url=url,callback=self.parse_result)

    def parse_result(self,response):
        review_urls = response.xpath('//div[@class="review"]/a/@href').extract()
        for url in review_urls:
            print(url)
            yield Request(url='https://www.pitchfork.com/' + url, callback=self.parse_review)





    def parse_review(self, response):
        artist = response.xpath('//ul[@class="artist-links artist-list single-album-tombstone__artist-links"]/li/a/text()').extract()
        print(artist)
        album = response.xpath('//h1[@class="single-album-tombstone__review-title"]/text()').extract()
        print(album)
        score = response.xpath('.//span[@class="score"]/text()').extract()
        print(score)
        genre = response.xpath('//a[@class="genre-list__link"]/text()').extract()
        print(genre)
        date = response.xpath('//time[@class="pub-date"]/text()').extract()
        print(date)
        content = response.xpath('//div[@class="contents dropcap"]/p/text()').extract()
        print(content)
        label = response.xpath('//li[@class="labels-list__item"]/text()').extract()
        print(label)

        item = PitchforkItem()
        item['artist'] = artist
        item['album'] = album
        item['score'] = score
        item['genre'] = genre
        item['date'] = date
        item['content'] = content
        item['label'] = label

        yield item

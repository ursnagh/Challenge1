import scrapy


class Book2scrapeSpider(scrapy.Spider):
    name = "book2scrape"
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    base_url = 'http://books.toscrape.com/'

    def parse(self, response):
        books = response.css('.col-lg-3')
        for book in books:
            url = book.css('h3 a::attr(href)').extract_first()
            img_url = book.css('a img::attr(src)').extract_first()
            book_title = book.css('h3 a::attr(title)').extract()
            book_price = book.css('div.product_price p.price_color::text').extract()
            if 'catalogue/' not in url:
                url = 'catalogue/' + url
            book_page_url = self.base_url + url
            full_image_url = self.base_url + img_url.replace('../','')
            yield {
                'Book Title' : book_title,
                'Product Price' : book_price,
                'Image URL' : full_image_url,
                'Book URL': book_page_url,
                }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)
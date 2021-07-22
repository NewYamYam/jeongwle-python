import scrapy

# URL = 'http://prod.danawa.com/list/?cate=11338057'

class titlespider(scrapy.Spider):
    name = 'title'
    # def start_requests(self):
    start_url = 'http://prod.danawa.com/list/?cate=11338057'
    custom_settings = {
    'DOWNLOADER_MIDDLEWARES': {
        'switchtitle.middlewares.SwitchtitleDownloaderMiddleware': 100
        }
    }

    def parse(self, response):
        print(response.text)
        print("----------")

        # headers = {
        #     'Host': 'www.danawa.com',    
        #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        # }
        # yield scrapy.Request(url=start_url, callback=self.parse, headers=headers)

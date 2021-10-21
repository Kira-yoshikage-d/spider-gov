import scrapy
from fake_useragent import UserAgent
import re

ua = UserAgent()

class LiuzhouSpider(scrapy.Spider):
    name = 'Liuzhou'
    allowed_domains = ['liuzhou.gov.cn']
    start_urls = ['http://www.liuzhou.gov.cn/']
    api = 'http://www.liuzhou.gov.cn/search/search?page={page}&channelid=269666&searchword={keyword}&keyword={keyword}&orderby=-DOCRELTIME&was_custom_expr=%28{keyword}%29&perpage=10&outlinepage=10&searchscope=&timescope=&timescopecolumn=&orderby=-DOCRELTIME&dates=&datee='
    #提取最后一页的链接的xpath：//div[@class="sz123"]/a[@class="last-page"]/@href
    #标题的xpath：//tbody/tr[2]/td/span[@class="js_zi2"]/a/text()
    #链接的xpath：//tbody/tr[2]/td/span[@class="js_zi2"]/a/@href
    #更新时间xpath：//tbody/tr[4]/td/text()
    #预浏览xpath：//tbody/tr[3]/td/text()
    keywords = ['碳管理']

    def start_requests(self):
        keywords = self.keywords
        if not keywords:
            raise Exception("no keywords provided")
        for keyword in keywords:
            req = scrapy.Request(
                url = self.api.format(page=1, keyword=keyword),
                headers = {"User-Agent": "Google"},
                callback = self.parse
            )
            req.cb_kwargs['keyword'] = keyword
            req.cb_kwargs['page'] = 1
            yield req


    def parse(self, response, keyword, page):
        yield from self.parse_items(response, keyword, page)
        all_page = self.parse_page(response)

        self.logger.debug("Total Page {}".format(all_page))
        for p in range(2, all_page + 1):
            req = scrapy.Request(
                url=self.api.format(page=p, keyword=keyword),
                headers={"User-Agent": ua.random},
                callback=self.parse_items
            )
            req.cb_kwargs['keyword'] = keyword
            req.cb_kwargs['page'] = p
            self.logger.info("爬取 查询 关键词：{} 页面：{}".format(keyword, p))
            yield req


    def parse_page(self, response):
        page_info = response.xpath('//div[@class="sz123"]/a[@class="last-page"]/@href').get()
        page = re.compile('search\?page=(.*?)&').findall(page_info)[0]
        return int(page)

    def parse_items(self, items, keyword=None, page=None):
        items_box = items.xpath('//div[@class="classify project"]/table')
        #items_box = items.css('tbody.xh-highlight')
        return (self.parse_item(item, keyword, page) for item in items_box)

    def parse_item(self, item, keyword, page):
        meta_info = {
            "title": item.xpath('//span[@class="js_zi2"]/a/text()').get(),
            "url": item.xpath('//span[@class="js_zi2"]/a/@href').get(),
            "pre_content": item.xpath('//td[@class="news"]/text()').get(),
            "date": item.xpath('//td[@class="js_zi1"]/text()').re(".*更新日期：(.*)")[0],
            "keyword": keyword,
            "page": page
            # "title": item.css('tr > td > span.js_zi2 > a::text').get(),
            # "url": item.css('tr > td > span.js_zi2 > a::attr(href)').get(),
            # "pre_content": item.css('tr > td.news::text').get(),
            # "date": item.css('tr > td.js_zi1::text').get(),
            # "keyword": keyword,
            # "page": page
        }
        return meta_info


import scrapy
from scrapy.responsetypes import Response
from search_engine.basepro import ZhengFuBaseSpider


class ChengduSpider(ZhengFuBaseSpider):
    """TODO Cookie 反扒"""
    name = 'Chengdu'
    allowed_domains = ['http://www.chengdu.gov.cn/']
    start_urls = ['http://http://www.chengdu.gov.cn//']
    method = 'GET'
    api = 'http://www.chengdu.gov.cn/guestweb4/s?searchWord={' \
          'keyword}&column=%E5%85%A8%E9%83%A8&wordPlace=0&orderBy=0&startTime=&endTime=&pageSize=10&pageNum={' \
          'page}&timeStamp=0&siteCode=5101000028&sonSiteCode=5101000028&checkHandle=0&strFileType=&govWorkBean=%7B%7D' \
          '&sonSiteCode=5101000028&areaSearchFlag=-1&secondSearchWords=&topical=&pubName=&countKey=0&uc=0 '
    cookie = "azSsQE5NvspcS=5ijlygeJZlg_cda6DOLREfd5uaT0fKOUb2z0ZCld7HyUEwCiFti6605pwPFSD.bmONZcc.tb3szk8xAcMU9J4Ma; yfx_c_g_u_id_10000057=_ck22070409482216175118643636553; yfx_f_l_v_t_10000057=f_t_1656899302606__r_t_1656899302606__v_t_1656899302606__r_c_0; Hm_lvt_a458cc5cc881b98da2a16b6c121539a2=1656899303; Hm_lpvt_a458cc5cc881b98da2a16b6c121539a2=1656899303; azSsQE5NvspcT=537xApDhcVmaqqqDrSaB3PG3Tz8mGq_5LkJIsTMsxHJqaWpBSjKuTt_U5nujNo.029INhT_GpHI9F15CllUv1d0Km8dS1YGVVrlUJddcUaHQbrlFC9oIOznIYyIEBiDFr9FYApq5M6T2_AOpYialzyyHToUbiqoW7wdcGB07GA3fri6eZBeSWqxUflDBt6dgEElQdt1JtHHMlYDm8ZROFSjNe3BW40W0ZxpT84xhr8SzjGyoUqniZWfrtmqHnbFupI9wsxdVofXjJsys_wK9lA_"
    start_page = 0

    def edit_items_box(self, response: Response):
        return response.css("body > div.resultTotalBox.clearfix > div.resultList.fl > div.pubResultList")

    def edit_item(self, item: scrapy.Selector):
        result = {'url': item.css("div.addSourceDateBox a::attr(href)").get()}
        return result

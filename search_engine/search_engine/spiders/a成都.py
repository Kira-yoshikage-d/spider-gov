from typing import Any, Generator, Iterable, List, Optional, Union

from search_engine.basepro import ZhengFuBaseSpider
from scrapy.responsetypes import Response
from scrapy import Selector


class A成都Spider(ZhengFuBaseSpider):
    name: str = '成都'
    api: str = 'http://www.chengdu.gov.cn/guestweb4/s?searchWord={keyword}&column=%E5%85%A8%E9%83%A8&wordPlace=0&orderBy=0&startTime=&endTime=&pageSize=10&pageNum={page}&timeStamp=0&siteCode=5101000028&sonSiteCode=5101000028&checkHandle=1&strFileType=&govWorkBean=%7B%7D&sonSiteCode=5101000028&areaSearchFlag=-1&secondSearchWords=&topical=&pubName=&countKey=0&uc=0'
    method: str = 'GET'
    data: dict[str, Any] = {}
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    cookie = "azSsQE5NvspcS=5JXWSe7eh0t2qgby94RE4Rv0d3B._tmxlHoZ_o22keNS_aaWUgfxUV2bBeAIo.zisC1vZ7YJCERjEm9Qois3B_A; Hm_lvt_a458cc5cc881b98da2a16b6c121539a2=1681218123; yfx_c_g_u_id_10000057=_ck23041121042616642265643307943; yfx_f_l_v_t_10000057=f_t_1681218266661__r_t_1681218266661__v_t_1681218266661__r_c_0; Hm_lpvt_a458cc5cc881b98da2a16b6c121539a2=1681218267; azSsQE5NvspcT=5RkYQPbATUhLqqqDoQomdVG9TffTqknjI.2Kh.7BTbczVw23tLSSeiGNNuItEryXijXDurXH62PoAddInLRVoLFf64Cd6eOvR3Gw6P7TXgLJh0V1gs_qLX92ITaVi3t4m345KEn7essQcFyeY5HLrEBf5r3htWwshFUSQTBuJ77Y6I1bun1rnfXnLdfakgT20vB4EDL5EIRDPXJB.3l5TuMyzJcyrTY61buJb5wgLnI4smhCc.nVkjpQpC0I0.S4nxJ_Vmc0GpZQFNmnw719EYBzk6MHeo7XMeJWq.twAPmyei68bI6aktWILnTaYN6rf7"
    start_page = 0
    debug: bool = False


    def edit_page(self, response: Selector) -> int:
        """
        input: response
        return: int
        """
        return int(response.css("div.totalNmu > span::text").re("(\d+)")[0])

    def edit_items_box(self, response: Selector) -> Union[Any, Iterable[Any]]:
        """
        从原始响应解析出包含items的容器
        input: response
        return: items_box
        """
        return response.css("body > div.resultTotalBox.clearfix > div.resultList.fl > div.pubResultListCon > div.pubResultList")

    def edit_items(self, items_box: Any) -> Iterable[Any]:
        """
        从items容器中解析出items的迭代容器
        input: items_box
        return: items
        """
        return items_box

    def edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]:
        """
        将从items容器中迭代出的item解析出信息
        input: items
        return: item_dict
        """
        result = {
            'title': item.css("div.tit a::attr(title)").get(),
            'url': item.css("div.tit a::attr(href)").get(),
            'source':  item.css("div.addSourceDateBox div.pubSourceDate span::text").getall()[1],
            'date': item.css("div.addSourceDateBox div.pubSourceDate span::text").getall()[0],
        }
        return result


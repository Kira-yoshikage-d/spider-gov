# README

__本项目用于学术研究自用，请勿用于违法行为，否则后果自负。__

## TODO

- [ ] 完善文档(WORKING)
- [ ] 重构代码，让爬虫再通用，稳健，易用一些(WORKING)
- [ ] 编写接口，把两个独立模块合并

## 项目架构

search_engine 爬取索引 + article_crawler 爬取正文

### search_engine 用于编写网站对应的搜索引擎

#### 配置

1. 数据库配置

    你需要安装最新的MongoDB与pymongo库.

    在search_engine项目的settings.py同级目录下新建文件db.py， 或者你也可以直接将模板文件db.py_bak重命名为db.py
    常规的配置如下：

    ```python3
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 数据库地址
    MONGODB_URI = 'mongodb://localhost:27017'
    # 数据库名
    MONGODB_DATABASE = 'scrapy_gov'

    # 邮件配置
    STATSMAILER_RCPTS = ['xxxxxxxx@gamil.com']
    MAIL_FROM = 'xxxxxxxx@gamil.com'
    MAIL_HOST = 'xxxxxxxx@gamil.com'
    MAIL_PORT = 111
    MAIL_USER = 'xxxxxxxx@gamil.com'
    MAIL_PASS = 'pass'
    MAIL_SSL = True
    ```

    ⚠️：该文件包含隐私信息，请勿添加到VCS中！

2. 关键字配置

    - 关键字

        关键字集中保存在scrapy.cfg文件同级的keywords.json文件中，其结构如下：

        ```json
        {
            'keywords_set_1': {
                'city_1': '...',
                'city_2': '...',
                'city_3': '...',
            },
            'keywords_set_2': {
                'city_1': '...',
                'city_2': '...',
                'city_3': '...',
            },
            ...
        }
        ```

        文件描述了若干个关键字集，通常你有多个不同主题的关键字搜索时会用到；

        每个关键字集中city_x为爬虫名称，其后紧接由`、`分隔的，该爬虫应该搜索的若干关键字。如：

        ```json
        '黄山': '关键字_1、关键字_2、关键字_3'
        ```

        目前你还不可以自定义分隔符。

    - 关键字集

        此外，你还需要在settings.py中指明当前使用的关键字集。例如：

        ```python3
        SEARCH_ENGINE_KEYWORDS_SET = '政府工具'
        ```

### article_crawler 用于爬取文章内容

TODO

## API

### 如何使用 ZhengFuBaseSpider

#### 属性

- name: str

    蜘蛛名称，scrapy以此检索蜘蛛；

- allowed_domains: List[str]

    爬取域名范围，在allowed_domains内的链接才会被抓取；

- start_urls: List[str]

    起始爬取链接

- keywords: List[str]

    搜索关键词

- api: str

    api 搜索接口，通常需要 {keyword} 和 {page} 作为格式化参数

- method: str {"GET/POST"}

    爬取数据的方法， "GET" 或 "POST"

- headers: dict

    爬取使用的头，默认使用chrome浏览器的头

- parse_first: Boolean

    是否解析 index 页，默认为 True

- start_page: int

    起始页的值

- data: dict

    当 method 为 "POST" 时，POST的数据表单模板

- batch: bool

    是否启用批量搜索模式，默认为 False

- debug: bool

    是否启用debug模式，默认为 False

#### 方法

- edit_data(self, data: dict, keyword: str, page: int, **kwargs) -> dict[str, Any]

    当爬虫method为POST时，对模板表单的修改函数；

    data: 表单模板

    keyword: 当前关键词

    page: 当前页数

    ⚠️注意: 若表单模板符合规范，则不需要重写此方法，父类会自动格式化模板；

- edit_items_box(self, response: Response) -> Union[Any, Iterable[Any]]

    该函数从被scrapy Response包装的原始请求中提取包含目标数据的容器；

    该函数设计的目的是：有些政府网站的数据并不是按照序列组织的，有些是交错的，有些甚至是嵌套的；
    该函数将包含数据的最小容器解析出来，以供 edit_items 函数重新组织数据结构；

    response: 当前搜索结果页面的scrapy Response封装；

- edit_items(self, items_box: Any) -> Iterable[Any]

    该函数返回可迭代对象；其中可迭代对象的迭代单位应当为最小目标数据，
    在本项目中，最小目标数据应当为包含一条政府数据搜索索引的容器；

    items_box: 由edit_items_box返回的容器；

    ⚠️注意：若在 edit_items_box 中已经实现了上述标准，则该方法可以不用重写；

- edit_item(self, item: Any) -> Optional[dict[str, Union[str, int]]]

    该函数从最小容器中抽取目标数据，并将数据作为字典返回；

    item: edit_items 为中的迭代单位；

- edit_page(self, response: Response) -> int

    该函数从搜索第一页解析出当前关键词的搜索总页数；

    response: 爬虫搜索的第一页结果的scrapy Response封装；

#### ZhengFuBaseSpider 是怎样运行的

    1. 类的入口为 start_requests

    start_requests 只会运行一次，

    该方法会先检查各个 变量时候存在，以及其合法性。

    检查的变量有 

    keywords: 指明搜索关键词

    api: 指明搜索用的 api

    method: 指明类运行的逻辑

    该类依照 method 的值，选定运行逻辑，之后抛出初始 requests。

    这些 requests 的构造委托给 method 对应的方法

    "GET" 则 委托给 start_get_requests

    "POST" 则 委托给 start_post_requests

    这些 requests 的回调函数为 spider.parse_index，因此之后的控制流程交给 spider.parse_index

    2. 解析当前关键字的元信息（页数）并进一步的抛出后续 requests

    parse_index 负责从 response 中解析当前关键字的总页数，以便抛出后续 requests。

    其中有一个问题，即，由 start_requests 抛出的 requests 而返回的 responses 中是否包含我们需要的信息。简单的说，就是我们爬取的 index 页是否有我们需要的信息。

    如果 index 页包含我们需要的信息，那我们需要解析 index 页，解析并将这些信息抛给 engine。之后的 requests 的 page 范围应该为 2 - MaxPage；相反的，如果 index 页只包含页数信息，而不包含我们需要爬取的信息，那么我们不需要解析 index 页——只要提取出 总页数 即可，之后的 requests 的 page 范围应该为 1 - MaxPage。

    究竟采取哪一套逻辑，我们使用成员变量 parse_first 来决定。

    默认 parse_first 为 Ture，这意味着总是解析 index 页，也就是第一套逻辑；当 设为 False 时，采用第二套逻辑。

    从 index 页面解析出 总页数 后，该方法会抛出后续的 requests，此时已经不再需要解析页数了，因此，这些 requests 的回调函数为 sepider.parse_items，将控制流程交给 spider.parse_items。

    3. 解析 items

    parse_items 是一个生成器，它会将最终解析的 items 抛给 engine

    该函数将具体的逻辑交给三个函数，通常用户需要实现这三个函数。

    这三个函数会以此调用，它们是:

    - edit_items_box

    - edit_items

    - edit_item

    之所以分出三个函数，是出于代码可读性的考虑。

    - edit_items_box 用于从总 response 中限制 items 的范围。这个函数，应当返回一个包含 items 的迭代结构。

    - edit_items 指明了如何从 items_box 这个迭代结构中，对数据进行迭代，这个函数应该实现为一个生成器，或返回生成器的函数，或迭代item的结构。

    - edit_item 指明了，从items_box 中迭代出的item还需要怎样的预处理，通常来说会需要重新构造新的数据。

    4. "POST" 时，构造提交的 data

    委托给函数 edit_data

    该函数拷贝一份模板 data，并动态返回需要提交的表单数据。

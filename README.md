# README

__本项目用于研究自用，请勿用于违法行为，否则后果自负。__

## TODO

- [ ] 完善文档
- [ ] 重构代码，让爬虫再通用，稳健，易用一些
- [ ] 编写接口，把两个独立模块合并

## search_engine 用于编写网站对应的搜索引擎

TODO

## article_crawler 用于爬取文章内容

TODO

## API

### 如何使用 ZhengFuBaseSpider

#### 属性

    - name: str

      定义 蜘蛛名称
    
    - allowed_domains: List[str]
    
      定义 爬取域名范围
    
    - start_urls: List[str]
    
      定义 起始点

    + keywords: List[str]
    
      定义 搜索关键词
    
    + api: str
    
      定义 api 搜索接口，通常需要 {keyword} 和 {page} 作为格式化参数
    
    + method: str {"GET/POST"}
    
      定义 爬取数据的方法， "GET" 或 "POST"
     
    + headers: dict
    
      定义 爬取使用的头，默认使用谷歌爬虫机器人的头
    
    - parse_first: Boolean
    
      是否解析 index 页，默认为 True
      
    - start_page: int
    
      page 的起始值

    - data: dict
    
      当 method 为 "POST" 时的 表格数据

#### 方法

    - edit_data(self, data, keyword, pagej)
    
      实现一个函数，返回一个 dict
    
    - edit_items_box(self, response)
    
      实现一个函数，返回 item 的集合 的 迭代数据结构
    
    - edit_items(self, items_box)
    
      实现一个生成器
      
      或
      
      实现一个函数，返回生成器
      
      或
      
      实现一个函数，返回一个迭代数据结构
    
    - edit_item(self, item)
    
      实现一个函数，返回值为 dict
    
    - edit_page(self, response)
      
      实现为一个函数，返回值为 int

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
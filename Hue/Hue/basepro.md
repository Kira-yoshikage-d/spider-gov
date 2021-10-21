# README

## 1. 如何使用 ZhengFuBaseSpider

### 属性

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

    - data: dict
    
      当 method 为 "POST" 时的 表格数据

### 方法

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

## 2. ZhengFuBaseSpider 是怎样运行的


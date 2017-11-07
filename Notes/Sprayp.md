### 安装

### 开始
- 新建一个项目  
`scrapy startproject name`
- 新建一个任务  
`scrapy genspider quotes quotes.toscrape.com`
- 查询任务  
`scrapy list`
- 运行  
`scrapy crawl quotes`   
- 以Scrapy spider获取到的形式展现url   
`scrapy view http://www.baidu.com/`
- 命令行模式  
`scrapy shell http://www.baidu.com`
- 保存运行结果  
`scrapy crawl quotes -o quotes.json`

- 运行一个编写在Python文件中的spider  
`scrapy runspider <spider_file.py>`
- 查看版本
`scrapy version -v`
- 部署

- 运行benchmark测试
`scrapy bench`
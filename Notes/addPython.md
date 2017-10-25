

### 安装 [Anaconda](https://www.continuum.io/)
python集成环境

### 安装 [python](https://www.python.org/)

`brew install python3`
`sudo apt-get install python3`  
`sudo apt-get install python3-pip`

### 安装 [mongdb](https://www.mongodb.com/)
`sudo apt-get install mongodb` 
####启动
`mongdo`

### 安装 [redis](https://redis.io/)
`sudo apt-get isntall redis`
### 启动
`redis-cli`
### 安装 redis GUI
`brew cask install rdm`

### 安装 [mysql]()
`sudo apt-get install mysql-server mysql-client`

### brew

- 正在运行的服务 `brew services list`
- 启动服务 `brew services start mongodb`
- 停止服务 `brew services stop mongodb`
- 重启服务 `brew services restart mongodb`

### 请求库的安装
- `pip3 install requests`
- `pip3 install selenium`
- [Geckodriver](https://github.com/mozilla/geckodriver)
- [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver)
- [PhantomJS](http://phantomjs.org)
- `pip3 install aiohttp`
- `pip3 install cchardet aiodns`

### 配置环境变量
`$vim ~/.bash_profile`
添加下面语句保存
`export PATH="$PATH:/Users/xxx/phantomjs-2.1.1-macosx/bin"`
在执行
`$source ~/.bash_profile`
如果出现命令丢失,则执行
`export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin`

### 解析库
- `pip3 install lxml`
- `pip3 install beautifulsoup4`
- `pip3 install pyquery`
- [Tesserocr](https://github.com/sirfz/tesserocr)
### 数据库
- `brew install mysql`
- `brew install mongodb`
- `brew install redis`
### 储存库
- `pip3 install pymysql`
- `pip3 install pymongo`
- `pip3 install redis`
- [RedisDump](http://www.ruby-lang.org/zh_cn/documentation/installation)
- `gem install redis-dump`
### web 库
- `pip3 install flask`
- `pip3 install tornado`
### App 爬取库
- [Charles](https://www.charlesproxy.com)
- [MitmProxy](https://github.com/mitmproxy/mitmproxy)
- [Appium](https://github.com/appium/appium)
### 爬虫框架
- `pip3 install Scrapy`
- [ScrapySplash](https://github.com/scrapy-plugins/scrapy-splash)
- `pip3 install scrapy-splash`
- `pip3 install scrapy-redis`
### 部署
- [docker](https://www.docker.com)
- `pip3 install scrapyd`
- `pip3 install scrapyd-client`
- `pip3 install python-scrapyd-api`
- `pip3 install scrapyrt`
- `pip3 install gerapy`
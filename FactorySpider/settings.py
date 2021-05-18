# Scrapy settings for FactorySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 此Scrapy项目实施的bot的名称（也称为项目名称）。这将用于默认情况下构造User-Agent，也用于日志记录，默认scrapybot
BOT_NAME = 'FactorySpider'

# Scrapy将寻找爬虫的模块列表
SPIDER_MODULES = ['FactorySpider.spiders']
# 模块在哪里使用genspider命令创建新的爬虫
NEWSPIDER_MODULE = 'FactorySpider.spiders'

# 导出的Encoding
FEED_EXPORT_ENCODING = 'utf-8'

# 包含要使用的项目管道及其顺序的字典。顺序值是任意的，但通常将它们定义在0-1000范围内。值越小，优先级越高
ITEM_PIPELINES = {
    'FactorySpider.pipelines.FactoryspiderPipeline': 300
}

# 检索时使用的默认用户代理，除非被覆盖。默认"Scrapy/VERSION (+http://scrapy.org)"
# USER_AGENT = 'FactorySpider (+http://www.yourdomain.com)'

# 如果启用，Scrapy会尊重robots.txt政策，默认False
ROBOTSTXT_OBEY = True

# 将由Scrapy下载程序执行的并发（即同时）请求的最大数量，默认16
# CONCURRENT_REQUESTS = 32

# 下载器在从同一网站下载连续页面之前应等待的时间（以秒为单位）。这可以用于限制爬行速度，以避免击中服务器太难。支持小数。默认0
DOWNLOAD_DELAY = 1

# 将对任何单个域执行的并发（即同时）请求的最大数量。默认8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 将对任何单个IP执行的并发（即同时）请求的最大数量。如果非零，忽略CONCURRENT_REQUESTS_PER_DOMAIN，而改为使用此设置。默认0
# CONCURRENT_REQUESTS_PER_IP = 16

# 是否启用Cookies，默认True
COOKIES_ENABLED = False

# 是否启用telnet控制台，默认True
# TELNETCONSOLE_ENABLED = False

# 包含在您的项目中启用的爬虫中间件的字典及其顺序
# SPIDER_MIDDLEWARES = {
#    'FactorySpider.middlewares.FactoryspiderSpiderMiddleware': 543,
# }

# 包含项目中启用的扩展名及其顺序的字典
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

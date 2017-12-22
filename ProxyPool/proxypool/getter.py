


class ProxyMetaclass(type):

    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

class FreeProxyGetter(object, metaclass=ProxyMetaclass):

    def get_raw_proxies(self, callback):
        proxies = []
        print('Callback', callback)
        for proxy in eval('self.{}()'.format(callback)):
            print('Getting', proxy, 'from', callback)
            proxies.append(proxy)
        return proxies

    def crawl_ip181(self):
        start_url = 'http://www.xicidaili.com/'



import requests
from bs4 import BeautifulSoup

iplist = []
html = requests.get('http://www.66ip.cn/index.html', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'})
ips = BeautifulSoup(html.text, 'lxml').find('div',class_='containerbox boxindex').find('table').find_all('tr')
for ip in ips:
    # i = ip.td.get_text()
    i = ip.find_all('td')[0].get_text() + ':' + ip.find_all('td')[1].get_text()

    iplist.append(i.strip())

print(u'代理有', iplist)

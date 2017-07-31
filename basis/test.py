#coding:utf-8

import requests



url = "http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;szzf;pn50;ddesc;qsd20160720;qed20170720;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}


html = requests.get(url, headers=headers)
print(html.text)
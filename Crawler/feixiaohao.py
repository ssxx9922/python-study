#coding:utf-8

import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/data')
def index():
    data = parseData('http://www.feixiaohao.com/')
    j = json.dumps(data)
    return j

def parseData(url):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    content = requests.get(url,headers=headers)
    bs = BeautifulSoup(content.text,'lxml').find('table',id='table').find_all('tr')
    datas = []
    for item in bs:
        tds = item.find_all('td')
        data = {}
        for index,item in enumerate(tds):
            name = item.get_text().strip()
            if index == 0:
                       data['number'] = name
            elif index == 1:
                data['name'] = name
            elif index == 2:
                data['marketValue'] = name
            elif index == 3:
                data['price'] = name
            elif index == 4:
                data['marketAmount'] = name
            elif index == 5:
                data['turnover'] = name
            elif index == 6:
                data['increase'] = name
            elif index == 7:
                data['trend'] = name
        datas.append(data)
    responseData = {'code':'OK','data':datas}
    return responseData


if __name__ == '__main__':
    app.run(debug=True)


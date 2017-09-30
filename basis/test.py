#coding:utf-8

from bs4 import BeautifulSoup
import re

html = open('book-1000001.html')

h = BeautifulSoup(html, 'lxml')

title = h.find('div', id='wrapper').find('h1')

print(title.get_text())

info = h.find('div', id='info')

author = info.find('span').find('a')

print(author.get_text().strip())

con = re.sub('<a.*?>|</a>', '', str(info))

con1 = re.sub('</span>', '', con)

con2 = re.sub('\s', '', con1)

results = re.findall('<spanc.*?>(.*?):(.*?)<b.*?>', con2, re.S)

dic = {}

for result in results:
    key = result[0]
    value = result[1]
    dic[key] = value

print(dic)

score = h.find('strong', class_='ll rating_num ')
if not score:
    print(score.get_text().strip())

people = h.find('a', class_='rating_people')

try:
    print(people.find('span').get_text())
except Exception as e:
    pass

tags = h.find_all('a', class_='tag')

tagList = []
for tag in tags:
    tagList.append(tag.get_text())
print(tagList)

intro = h.find('div', class_='intro').find('p')

print(intro.get_text())


def list(age):
    l = [a for a in range(1, 100, age)]
    for i in l:
        yield i


for l in list(10):
    print(l)
import requests
import re

def Dircetory():
    response = requests.get('http://es6.ruanyifeng.com/sidebar.md')
    regex = re.findall('1. \[.*?]\(#(.*?)\)', response.text, re.S)
    for result in regex:
        yield result

def Info(paths):
    for path in paths:
        url = 'http://es6.ruanyifeng.com/' + path + '.md'
        response = requests.get(url)
        wrtie_to_file(response.text)

def wrtie_to_file(content):
    with open('ES6.md', 'a', encoding='utf-8') as f:
        f.write(content + '\n')
        f.close()

if __name__ == '__main__':
    paths = Dircetory()
    Info(paths)



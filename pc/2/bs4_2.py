#__author: xlu.com
#date : 2018/8/8

from bs4 import BeautifulSoup
import lxml
import requests
import json
import re

def getContentByUrl(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content.decode('gbk'),features='lxml')
    # els = html.select('.bd3r .co_area2 tr')
    ret_list = []
    for item in html.select('.bd3r .co_area2 table tr'):
        # print(item.get_text('|',strip=True))
        it = []
        for i in item.stripped_strings:
            it.append(i)
        ret_list.append(it)
    print(ret_list)
    print(json.dumps(ret_list))

def getbb(url):
    resp = requests.get(url)
    html = BeautifulSoup(resp.content.decode('gbk'),features='lxml')
    ret_list = []
    tt = html.find_all(class_= re.compile('co_content'))
    # print(len(tt))
    index = 0
    for itt in tt:
        ttt = itt.find_all('a',href=True)
        for it2 in ttt:
            print('http://www.dytt8.net'+it2['href'])
            index+=1
        # print(itt.ul.a)
        # exit()
    print(index)
    exit()
    for item in html.select('.bd3r .co_area2 '):
        # print(item.get_text('|',strip=True))
        it = []
        for i in item.stripped_strings:
            it.append(i)
        ret_list.append(it)
    print(ret_list)
    print(json.dumps(ret_list))

if __name__ == '__main__':
    url = 'http://www.dytt8.net/'
    # getContentByUrl(url)
    getbb(url)

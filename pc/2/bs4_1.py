#__author: xlu.com
#date : 2018/8/8

from bs4 import BeautifulSoup
# import html5lib
import requests

def get_CountentByUrl(url):
    res = requests.get(url)
    html = res.content.decode('gbk')
    bss = BeautifulSoup(html,features="lxml")
    # list_a = bss.find_all('a',attrs={'href':True})
    list_a = bss.find('div',class_='bd3r').find_all('div',class_='co_area2')
    ret_list = []
    for item in list_a:
        for con in item.find_all('tr'):
            # it = con.get_text('|',strip=True)//获取标签内的所有字符串 以|隔开
            it = [];
            for string in con.stripped_strings:
                it.append(string)
            ret_list.append(it)
            print(it)
    print(ret_list)
if __name__ == '__main__':
    get_CountentByUrl('http://www.dytt8.net/')

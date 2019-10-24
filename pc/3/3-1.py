#__author: xlu.com
#date : 2018/10/28
import threading
from queue import Queue
import os
from lxml import etree
import re
import requests
from urllib import request

class Pro(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Pro, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def  run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.pase_page(url)

    def pase_page(self,url):
        heads = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            # 'Referer': 'http://www.doutula.com/photo/list/?page=2',
            # 'Host': 'www.doutula.com',
            # 'Cookie': '__cfduid=d41bbd5c2a4b2b886859b91e0ea89c6691540733649; UM_distinctid=166bae1c6d424f-0514cd04c324aa-333b5402-100200-166bae1c6d5199; CNZZDATA1256911977=794445147-1540728812-%7C1540728812; _ga=GA1.2.1174860913.1540733651; _gid=GA1.2.139224841.1540733651; yjs_id=0b2dc6843bedc42e7bd4641265f3abf7; ctrl_time=1; XSRF-TOKEN=eyJpdiI6ImZORllsMGNWSm9CUUF5eGhPNCtjanc9PSIsInZhbHVlIjoieGlsSjVQSkhKbnZ5M2lYUXZFdWtibkZNbWpcL2FLZ3lGem5OTkM4dmJTTEEzamNTOHpVRXMybGhxWlZ3U2szMUx5MlBvUkpLUU5reko4UGhmVFNEc0FnPT0iLCJtYWMiOiIxZWUzY2U5N2ZiNjRmYmNiYjNhM2VjOThlY2EwZGM1YTA5NTY0NDA1MGUyODExOTUxNjJlM2UyNWVkYWY0MDQyIn0%3D; doutula_session=eyJpdiI6Inl3Q2RPK0llTHlZYUV6MndBOWwwRnc9PSIsInZhbHVlIjoieHVBNjdxbit0aWpnKzVKN1Y0YTlRejdobkkzUXV3QnBPK2FQcGlSMHMzdXFzSVppRmJsZ3BwTUttYmptTTZmZ0t4cTI2V3d0dGNxUjBNazVzTGFnQnc9PSIsIm1hYyI6ImY1M2FmYmNiNDg1MTA2NWM1NmZjZDMzZGUwYjc3NTk0MDU5ZjA5MTc1ZGNmYzE5ZDc3NmNmNTMzMjBiOTUzYWQifQ%3D%3D'
        }
        res = requests.get(url,headers=heads)
        html = etree.HTML(res.text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            src = img.get('data-original')
            name = img.get('alt')
            name = re.sub(r'[\?？\.！!\*]','',name) #过滤掉文件名中非法字符
            names = os.path.splitext(src)
            fix = names[1].split('!')[0]
            save_name = name+fix
            self.img_queue.put((src,'images/'+save_name))#将要下载的路径放入im队列

class cous(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(cous, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def  run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            url,name = self.img_queue.get()#消费
            request.urlretrieve(url,name)
            print('%s下载完成后'%(name))

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for pag in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d'%(pag)
        page_queue.put(url)

    for pro_idx in range(3):
        t = Pro(page_queue,img_queue)
        t.start()

    for cous_idx in range(10):
        t1 = cous(page_queue,img_queue)
        t1.start()
if __name__ == '__main__':
    main()
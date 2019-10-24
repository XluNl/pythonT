#__author: xlu.com
#date : 2018/8/10

import requests
import re
import json

# 使用re抽取内容
def getContentByUrl(url):
    resp = requests.get(url)
    html = resp.content.decode('utf-8')
    # 匹配出名字
    titles = re.findall(r'<div class="sons">.*?<p>.*?<b>(.*?)</b>',html,re.DOTALL)
    # print(titles)
    # 一次性匹配出朝代和作者
    chaodais = re.findall(r'<div class="sons">.*?<p class="source"><a .*?>(.*?)</a>.*?<a .*?>(.*?)</a>',html,re.DOTALL)
    # print(chaodais)
    # 单独匹配出作者
    # chaodais = re.findall(r'<div class="sons">.*?<p class="source"><a .*?>.*?</a>.*?<a .*?>(.*?)</a>',html,re.DOTALL)
    # print(type(chaodais))
    # 匹配出正文
    # pat = re.compile(r"""
    #         <div class="sons"> #入口
    #         .*? #
    #         <div class="contson" .*?> #
    #         (.*?) #正文部分
    #         </div>
    # """,re.VERBOSE)
    # ccontents = pat.findall(html,re.DOTALL)
    contents = re.findall(r'<div class="sons">.*?<div class="contson" .*?>(.*?)</div>',html,re.DOTALL)
    # print(contents)
    ret = []
    for item in zip(titles,chaodais,contents):
        title,chaodai,content = item
        it = {}
        it['title'] = title
        it['chaodai'] = chaodai[0]
        it['zuozhe'] = chaodai[1]
        it['content'] = str.strip(re.sub(r'<br />',' ',content))
        ret.append(it)
    print(len(ret))
    return ret
    # print(ret)

def main():
    # url = 'https://www.gushiwen.org/default_.aspx'
    # urls = []
    ress = []
    for i in range(1,101):
        url = 'https://www.gushiwen.org/default_%d.aspx' % (i)
        res = getContentByUrl(url)
        ress.append(res)
    f=open("./gsw.txt","w")
    json.dump(ress,f)

if __name__ == '__main__':
    main()

    # re.findall() //
    # re.search()  //返回匹配到的第一个对象，使用group获取结果
    # re.match()  //只从开头匹配，返回一个对象，通过group获取结果
    # re.split('[s,e]','absdef') //切割的顺序，先使用s分割成两部分，然后e再分别对s分完的结果进行分
    # res = re.search('(?P<id>\d{3})/(?P<name>\d{3})','adb123/000');#(?P<id>内容)固定写法-》为这个组起个名字
    # print(res)
    # print(res.group('id')) #根据名字获取
    # print(res.group('name')) #根据名字获取
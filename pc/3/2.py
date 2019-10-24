#__author: xlu.com
#date : 2018/8/10

import requests
import re
import json
import pymysql
# from pymysql import connections

# 使用re抽取内容
def getContentByUrl(url):
    resp = requests.get(url)

    html = resp.content.decode('utf-8')
    # 试着一次抽取全部内容
    contents = re.findall(r'<div class="sons">.*?<p>.*?<b>(.*?)</b>.*?<p class="source"><a .*?>(.*?)</a>.*?<a .*?>(.*?)</a>.*?<div class="contson" .*?>(.*?)</div>',html,re.DOTALL)
    # print(contents)
    # exit()
    ret = []
    for item in contents:
        it = {}
        it['title'] = item[0]
        it['chaodai'] = item[1]
        it['zuozhe'] = item[2]
        it['content'] = str.strip(re.sub(r'<br />|<span .*>|</span>|<p>|</p>|\n',' ',item[3]))
        ret.append(it)
        # print(len(ret))
    return ret

def main():
    # url = 'https://www.gushiwen.org/default_.aspx'
    # urls = []
    ress = []
    for i in range(303,383):
        # url = 'https://www.gushiwen.org/default_%d.aspx' % (i)
        url = 'https://so.gushiwen.org/authors/authorvsw.aspx?page=%d&id=85097dd0c645' % (i)
        res = getContentByUrl(url)
        # ress.append(res)
        for it in res:
            ress.append(it)
        # map(lambda data:ress.append(data),res)
    # f=open("./gsw1.txt","w")
    db = pymysql.connect(host='127.0.0.1',user='root',password='chenlip',database='jjccdb',port=3306)
    cur = db.cursor()
    insert = """insert into pc_gsw(title,zuozhe,chaodai,content) values"""

    # 拼接插入数据sql
    for item in ress:
        insert+='("%s","%s","%s","%s"),' % (item['title'],item['zuozhe'],item['chaodai'],item['content'])
    # 注意去掉最后一个逗号（,）
    cur.execute(insert[:-1])
    db.commit()

    # 写入本地文件
    # json.dump(ress,open("./gsw1.txt","w",encoding='utf-8'))

if __name__ == '__main__':
    main()
    # str = json.load(open("./gsw1.txt","r"))
    # print(str)

    # arr = [1,2,3,4,5]
    # arr1 = []
    # new_arr= map(lambda x:x+1,arr)
    # print(arr1)
    # for x in new_arr:
    #     print(x)
    # db = pymysql.connect(host='127.0.0.1',user='root',password='chenlip',database='jjccdb',port=3306)
    # cur = db.cursor()
    # cur.execute('select * from tp_admin_user')
    # res =cur.fetchall()
    # print(res)

    # # // 插入操作
    # insert = """insert into pc_gsw(title,zuozhe,chaodai,content) values('ww','eee','444','rrr'),('ww','eee','444','rrr')"""
    # res = cur.execute(insert)
    # db.commit()
    # print(res)
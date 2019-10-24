#__author: xlu.com
#date : 2018/11/2

import requests
from urllib import request
import re
import pymysql
import os


db = pymysql.connect(host='127.0.0.1',user='root',password='chenlip',database='jjccdb',port=3306)
# db = pymysql.connect(host='39.107.239.18',user='root',password='wdtx.2016',database='vd_moli_test',port=3306)
cur = db.cursor()


#包含utf8mb4的字符
data = '☺、��、@所有人 周日有组团爬香山去吗？已经有两人了'

# insert = """insert into char_utf8mb4(text_varchar,text_utf8mb4) values("%s","%s")""" % (data,data)
insert = """insert into char_utf8(text_utf8mb4,text_utf8) values("%s","%s")""" % (data,data)
cur.execute(insert)
cur.execute("select last_insert_id();")
data = cur.fetchall()
mainid = data[0][0]
db.commit()
print(mainid)
# exit()
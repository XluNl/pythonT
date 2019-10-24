#__author: xlu.com
#date : 2018/8/10
import pymongo

client = pymongo.MongoClient(host='127.0.0.1',port=27017)
# 这里相当于创建一个xlu的数据库
db  = client.xlu
print(db)
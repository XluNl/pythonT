print('json-序列化')

import json

#json 序列化
dic = {'name':'clp','age':18}
print(dic)
f = open('E:\python_text\jsontext','w')
f.write(json.dumps(dic))
f.close()
#简便方法 相当于上两句
#json.dump(dic,f)

# 反序列化json
f = open('E:\python_text\jsontext','r')
data = f.read()
json = json.loads(data)
#data = json.loads(f)
print(data)


import shelve
# 编辑字典
f = shelve.open('E:\python_text\shelve_text')
f['info'] = {'name':'clp','age':18}
f['ccc'] =['1,2,3,4']
# 读取
data = f.get('info')
data1 = f.get('ccc')
print(data,data1)

# 插曲
dic = {'name':'clp','age':18}
data = dic.get('name','没有哦') #字典通过键的名字去取值,如果有就返回取到的,没有就返回"没有哦"
print(data)
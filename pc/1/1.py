#__author: xlu.com
#date : 2018/7/31

from urllib import request,parse

url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())
# exit()
# 创建一个代理
handler = request.ProxyHandler({"http":"223.241.78.43:8010"})
# 构建一个opener
opener = request.build_opener(handler)
rsp = opener.open(url)
print(rsp.read())

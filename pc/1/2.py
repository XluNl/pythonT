#__author: xlu.com
#date : 2018/8/1

from urllib import request,parse
import json

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'
data = {
    "first": "true",
    "pn": 1,
    "kd": "Python"
}
headers = {
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    # "Accept-Encoding": 'gzip, deflate, br',
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Connection": "keep-alive",
    # "Content-Length": "25",
    # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie"    :"JSESSIONID=ABAAABAAAGGABCB041F729A2E63BB20D084D3E0BF533FCF; _ga=GA1.2.346600186.1533054133; _gat=1; user_trace_token=20180801002431-34055f02-94de-11e8-a085-5254005c3644; LGSID=20180801002431-3405603a-94de-11e8-a085-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20180801002431-340561f7-94de-11e8-a085-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533054133; _gid=GA1.2.783471249.1533054133; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_navigation; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1533054142; LGRID=20180801002440-39696027-94de-11e8-ac4b-525400f775ce; SEARCH_ID=404b0b3f2bc541739ec2cb3a4eefa6a7",
    # "Host"      :"www.lagou.com",
    # "Origin"    :"https://www.lagou.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Referer"   :"https://www.lagou.com/jobs/list_Python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=",
    # "X-Anit-Forge-Code": "0",
    # "X-Anit-Forge-Token": "None",
    # "X-Requested-With"  : "XMLHttpRequest"
}
req = request.Request(url,headers=headers,data=parse.urlencode(data).encode("utf-8"),method="POST")
# req = request.Request(url,headers=headers,data=data,method="POST")
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
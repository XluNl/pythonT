#__author: xlu.com
#date : 2018/8/2
import requests

resp = requests.get('http://jjcc-backend.xiaositv.com/api2/index/indextop/user_id/17116')
print(type(resp.content))
print(resp.content.decode('utf-8'))
exit()